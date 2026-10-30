"""A FastMCP server exposing WealthPilot database tables over stdio."""

import sqlite3
import sys
from fastmcp import FastMCP

import os
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import hashlib, json, time
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv(".env", override=True)

QDRANT_URL    = os.getenv("QDRANT_URL")
QDRANT_KEY    = os.getenv("QDRANT_API_KEY")
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEYKEY")

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_KEY)
COLLECTION = "wealth_realdocs"
_base = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

CACHE_DIR = ".embcache"
os.makedirs(CACHE_DIR, exist_ok=True)

mcp = FastMCP("wealthpilot-workspace")

def _ckey(text):  return hashlib.sha1(("gemini-embedding-001::" + text).encode("utf-8")).hexdigest()
def _cget(text):
    p = os.path.join(CACHE_DIR, _ckey(text) + ".json")
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None
def _cput(text, vec):
    with open(os.path.join(CACHE_DIR, _ckey(text) + ".json"), "w") as f:
        json.dump(vec, f)

def _embed_query(text):
    v = _cget(text)
    if v is None:
        v = _base.embed_query(text)
        _cput(text, v)
    return v

def _connect():
    conn = sqlite3.connect("wealthpilot.db")
    conn.row_factory = sqlite3.Row
    return conn

@mcp.tool
def applicant_details(applicant_id: str) -> dict:
    """Retrieve applicant financial and operating fields for an applicant ID."""
    conn = _connect()
    row = conn.execute("""
        SELECT ebitda_inr, existing_debt_inr, sector, months_operating, annual_revenue_inr
        FROM applicants_table WHERE applicant_id = ?
    """, (applicant_id,)).fetchone()
    conn.close()
    if row is None:
        return {}
    return dict(row)

@mcp.tool
def loan_application_details(applicant_id: str) -> dict:
    """Retrieve loan and collateral fields for an applicant ID."""
    conn = _connect()
    row = conn.execute("""
        SELECT requested_amount_inr, requested_tenor_months,
               existing_annual_debt_service_inr, collateral_value_inr,
               current_assets_inr, current_liabilities_inr,
               declared_annual_revenue_inr
        FROM loan_applications_table WHERE applicant_id = ?
    """, (applicant_id,)).fetchone()
    conn.close()
    if row is None:
        return {}
    return dict(row)


@mcp.tool
def bureau_reports(applicant_id: str) -> dict:
    """Retrieve bureau score and adverse-credit fields for an applicant ID."""
    conn = _connect()
    row = conn.execute("""
        SELECT bureau_score, active_trade_lines, dpd_90_ever, written_off_amount_inr
        FROM bureau_table WHERE applicant_id = ?
    """, (applicant_id,)).fetchone()
    conn.close()
    if row is None:
        return {}
    return dict(row)


@mcp.tool
def risk_grades(dscr: float, bureau_score: int) -> dict:
    """Retrieve the risk grade for a DSCR and bureau score."""
    conn = _connect()
    row = conn.execute("""
        SELECT * FROM risk_grades_table
        WHERE ? >= min_dscr AND ? >= min_bureau_score
        ORDER BY grade ASC LIMIT 1
    """, (dscr, bureau_score)).fetchone()
    conn.close()
    if row is None:
        return {}
    return dict(row)


@mcp.tool
def sector_policies(sector_name: str) -> dict:
    """Retrieve the policy floor and tenor cap for a sector."""
    conn = _connect()
    row = conn.execute("""
        SELECT dscr_floor, max_tenor_months AS sector_max_tenor_months, at_sector_cap
        FROM sector_policies_table WHERE sector = ?
    """, (sector_name,)).fetchone()
    conn.close()
    if row is None:
        return {}
    return dict(row)

@mcp.tool
def query_knowledge_base(query, k=3, source=None):
    """Fetch information from the knowledge base which is based on the company internal documents"""
    qfilter = Filter(must=[FieldCondition(key="source", match=MatchValue(value=source))]) if source else None

    hits = client.query_points(collection_name=COLLECTION, query=_embed_query(query),
                               query_filter=qfilter, limit=k).points
    return [h.payload['text'] for h in hits]

if __name__ == "__main__":
    print("[wealthpilot_mcp_server] starting on stdio", file=sys.stderr)
    mcp.run(transport="stdio", show_banner=False)
