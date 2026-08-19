import os, re
import supermemory
from groq import Groq
import streamlit as st

from dotenv import load_dotenv
load_dotenv("notebooks/.env", override=True)

mem = supermemory.Supermemory(api_key=os.getenv("SUPERMEMORY_API_KEY"))

def recall(query, app_id, k=1):
    client = mem
    out = []
    for r in client.search.memories(q=query, container_tag="loan_applicants", filters={"key": "Applicant ID", "value": app_id }, limit=k).results:
        if getattr(r, "memory", None):
            out.append(((r.metadata or {}).get("Applicant ID", "?"), r.memory, float(r.similarity or 0.0)))
    if not out:
        for r in client.search.documents(q=query, container_tags=["loan_applicants"], filters={"key": "Applicant ID", "value": app_id}, limit=k).results:
            text = " ".join(c.content for c in (r.chunks or []) if c and c.content).strip()
            if text:
                out.append(((r.metadata or {}).get("Applicant ID", "?"), text, float(r.score or 0.0)))
    return out[0] if out else (None, None, 0.0)

with st.sidebar:
    # clear session button
    if st.button("Clear Conversation"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
st.title("Your Assistant")
st.caption("🚀 A Streamlit chatbot powered by Groq")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if "client" not in st.session_state:
    st.session_state.client = Groq(api_key= os.getenv("GROQ_API_KEY"))

if prompt := st.chat_input():
    client = st.session_state.client
    st.chat_message("user").write(prompt)

    result = re.search(r"(\w+-\w+-\d+)", prompt)
    if result:
        applicant_id = result.group(1)
        mem_applicant_id, text, score = recall(f"Applicants search by ID", applicant_id, k=1)
        if mem_applicant_id == applicant_id:
            prompt = prompt + f"\n\n[Memory]: {text}"

    st.session_state.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(model="groq/compound-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
