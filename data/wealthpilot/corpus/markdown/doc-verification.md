# Document Verification and Fraud Screening Procedure

# ASHVA CAPITAL INTERNAL CREDIT POLICY MANUAL
## SECTION 4: DOCUMENT VERIFICATION AND FRAUD DETECTION PROCEDURES
**Document ID:** CP-SME-04-REV4.2  
**Effective Date:** 14 January 2025  
**Applies To:** All Credit Underwriters, Fraud Analysts, and Credit Managers  

---

### 4.1 MANDATORY DOCUMENT SET FOR SME APPLICATIONS

Every Small and Medium Enterprise (SME) credit application submitted to Ashva Capital must contain the complete mandatory document set listed below before underwriting commences. Incomplete files shall be rejected automatically by the loan origination system (LOS) on Day 0.

1. **KYC and Legal Entity Documentation:**
   * Certificate of Incorporation and Memorandum/Articles of Association (or equivalent partnership deed/LLP agreement).
   * Permanent Account Number (PAN) card of the business entity and all guarantors/directors holding $\ge 25\%$ equity.
   * Proof of Principal Place of Business (utility bill not older than 60 days, or registered lease agreement).
   * Valid Goods and Services Tax Identification Number (GSTIN) registration certificate.

2. **Financial Records:**
   * Audited financial statements (Balance Sheet, Profit & Loss Statement, Cash Flow Statement) for the last two (2) preceding financial years, bearing the UDIN (Unique Document Identification Number) where applicable.
   * Provisional financial statements for the current financial year-to-date (YTD), certified by a company director, if the application date is more than 180 days past the end of the last audited fiscal year.

3. **Tax and Statutory Filings:**
   * GST Returns (Form GSTR-3B and GSTR-1) for the last twelve (12) consecutive months.
   * Income Tax Returns (ITR) for the last two (2) assessment years along with official acknowledgement (ITR-V).

4. **Banking Records:**
   * Primary and secondary current account bank statements in native PDF format for the last twelve (12) consecutive months. Scanned copies, photocopies, or password-unlocked files originating from unverified sources are strictly prohibited.

---

### 4.2 VERIFICATION PROTOCOLS FOR FINANCIAL INSTRUMENTS

Underwriters must execute the following verification steps for all submitted financial instruments. Any deviation from these protocols must be documented in the audit trail.

#### 4.2.1 Bank Statements
1. **Source Authenticity:** Underwriters must pull bank statements directly via the Ashva Capital Account Aggregator (AA) framework or utilize API-driven direct bank feeds. If manual PDF upload is permitted under exception code `EX-BNK-09`, the underwriter must verify the digital signature embedded in the PDF properties.
2. **Transaction Integrity Check:** Automated parsing tools must verify that opening balances equal the prior day's closing balance across 100% of the 365-day period. Any sequence gap exceeding three (3) consecutive days requires a mandatory clarification from the applicant.
3. **Internal Cash Flow Scrub:** The underwriting system flags and deducts all contra-entries, inter-company transfers, unsecured loan inflows, and artificial round-tripping from the calculated Adjusted Gross Turnover (AGT).

#### 4.2.2 GST Returns (GSTR-3B vs. GSTR-1)
1. **Portal Reconciliation:** Underwriters must cross-reference GSTR-3B (tax liability paid) and GSTR-1 (outward supplies reported) against direct data fetched via the GST Network (GSTN) Application Programming Interface (API).
2. **Turnover Cross-Check:** The total taxable turnover declared in GSTR-3B must be reconciled against the credit entries in the operational bank statements. A variance exceeding $15\%$ between total GST turnover and total banking credit inflows requires documented justification and submission of debtor aging reports.

#### 4.2.3 Audited Financials
1. **Regulatory Cross-Verification:** Underwriters must verify the auditor’s membership credentials via the relevant statutory registry (e.g., ICAI register). 
2. **Schedule Validation:** Financial line items must be reconciled line-by-line against the notes to accounts, specifically verifying trade receivables, trade payables, and contingent liabilities. Depreciation schedules must match the Income Tax computation of income.

---

### 4.3 REVENUE DISCREPANCY TOLERANCE THRESHOLDS

Underwriters must compare the gross annual revenue declared by the applicant in the application form against the verified revenue derived from the triangulation of Bank Statements, GST Returns, and Audited Financials.

1. **Accepted Variance:** If the declared revenue falls within **10 percent** ($\le 10\%$) of the verified revenue, the discrepancy is **accepted**, and underwriting proceeds using the verified figure.
2. **Reviewer Escalation:** If the absolute difference between declared and verified revenue exceeds $10\%$, the system automatically assigns reason code **`DOC_MISMATCH`**, halts automated processing, and routes the file to a human reviewer for discrepancy analysis.
3. **Fraud Hold Trigger:** If the absolute difference between declared and verified revenue exceeds **25 percent** ($> 25\%$), the system assigns reason code **`FRAUD_HOLD`** and immediately triggers a mandatory fraud hold, locking the application.

---

### 4.4 MANDATORY FRAUD RED FLAGS

The occurrence of any single red flag listed below mandates the immediate application of reason code `FRAUD_HOLD`, suspension of the credit workflow, and referral to the Fraud Risk Unit (FRU) managed by Head of Risk, Marcus Vance.

1. **Document Metadata Anomalies:** PDF property metadata indicates creation or modification using editing software (e.g., Adobe Acrobat Pro, PDF-XChange) after the closing date of the statement period.
2. **Font and Alignment Inconsistencies:** Mismatched font families, inconsistent character spacing, or misaligned columnar totals within bank statements or tax returns.
3. **Round-Sum Manipulation:** Presence of engineered, identical round-sum credit transactions occurring on identical calendar days across multiple months, indicative of artificial inflation of turnover.
4. **Circular Transactions:** Identification of immediate, matching outward and inward remittances between the applicant and shell entities sharing identical directors, registered addresses, or IP login signatures.
5. **Dormant-to-Active Spike:** A sudden, unexplainable $300\%$ or greater increase in monthly turnover volume occurring precisely in the three months prior to loan application, unsupported by historical growth or new asset acquisition.
6. **Statutory Non-Compliance:** Discrepancies where GSTR-3B filings show zero turnover while operational bank statements exhibit high-velocity transactional activity.

---

### 4.5 ESCALATION PATH AND EXCEPTION GOVERNANCE

When an application encounters a `DOC_MISMATCH` or `FRAUD_HOLD` status, or requires policy exceptions, the file must follow the strict escalation hierarchy defined below. Underwriters are prohibited from overriding system-generated flags without documented sign-off from the designated authority.

```
[System Flag: DOC_MISMATCH or FRAUD_HOLD]
                 │
                 ▼
     [Assigned Underwriter]
 (Gathers clarification / 48-hr SLA)
                 │
       ┌─────────┴─────────0
       ▼                   ▼
[Resolved ≤ 10%]    [Unresolved / > 10%]
       │                   │
       ▼                   ▼
[Resume Workflow]   [Senior Underwriter Review]
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
     [Credit Manager]            [Head of Risk (FRU)]
 (Approves Minor Exception)     (For all FRAUD_HOLD cases)
             │                           │
             └─────────────┬─────────────┘
                           ▼
                  [Chief Credit Officer]
              (Final Authority for Overrides)
```

1. **Level 1 – Underwriter Review:**
   * Upon receipt of code `DOC_MISMATCH`, the underwriter must issue a formal Document Discrepancy Notice to the applicant via the secure portal, granting a strict response deadline of **48 hours**.
   * If the applicant fails to provide satisfactory documentary justification within 48 hours, the application is declined under policy rule `PR-REV-01`.

2. **Level 2 – Senior Underwriter and Credit Manager Escalation:**
   * Files flagged with unresolved discrepancies between $11\%$ and $25\%$ require joint sign-off from the Senior Underwriter and the regional Credit Manager, Sarah Jenkins, accompanied by an Exception Memorandum detailing mitigating credit strengths.

3. **Level 3 – Fraud Risk Unit (FRU) Escalation:**
   * Any file carrying reason code `FRAUD_HOLD` (revenue variance $> 25\%$ or presence of Section 4.4 red flags) must be transferred to the Fraud Risk Unit within **2 hours** of generation.
   * The FRU lead, Marcus Vance, must complete a forensic review within **three (3) business days**. 
   * If fraud is substantiated, the application is rejected, the entity is listed on the Ashva Capital Internal Denied Party List (IDPL), and a Suspicious Transaction Report (STR) is filed with the national financial intelligence unit within the statutory window of **7 days**.

4. **Level 4 – Chief Credit Officer (CCO) Override:**
   * No underwriter, Credit Manager, or Fraud Analyst possesses the authority to clear a `FRAUD_HOLD` status. 
   * A `FRAUD_HOLD` can only be expunged and the application returned to active underwriting status via written, timestamped override approval executed exclusively by the Chief Credit Officer, Aris Thorne, following a formal exoneration report compiled by the FRU.

---
*End of Section 4. Compliance with these procedures is subject to mandatory quarterly internal audit review.*
