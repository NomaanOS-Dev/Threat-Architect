import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Threat Architect", page_icon="🛡️", layout="wide")

st.title("🛡️ Threat Architect - Defensive Threat Modeling Platform")
st.caption("AI-Powered Threat Vector Analysis & MITRE ATT&CK Mapping | Built by NomaanOS-Dev")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.info("Input system components to model security risks, identify attack vectors, and generate hardening controls.")

arch_input = st.text_area(
    "Describe System Architecture / Tech Stack:",
    height=180,
    placeholder="e.g., AWS Hosted Web App using React frontend, Node.js backend, PostgreSQL database, S3 buckets, and exposed REST APIs..."
)

if arch_input:
    if openai_api_key:
        if st.button("Generate Threat Model & Hardening Plan"):
            with st.spinner("Analyzing architecture, mapping MITRE ATT&CK vectors, and building defensive controls..."):
                os.environ["OPENAI_API_KEY"] = openai_api_key
                
                prompt_template = (
                    "You are a Senior Security Architect and Threat Modeling Expert.\n"
                    "Analyze the following system architecture and generate a comprehensive Defensive Threat Model report.\n\n"
                    "Include the following sections clearly formatted in Markdown:\n"
                    "1. **Architecture Threat Summary**: Overview of potential attack surfaces.\n"
                    "2. **Identified Threat Vectors**: Specific risks (e.g., Data Leakage, Unauthorized Access, Injection).\n"
                    "3. **MITRE ATT&CK Mapping**: Map risks to relevant MITRE ATT&CK Tactics & Techniques.\n"
                    "4. **Defensive Hardening Controls**: Recommended security controls (NIST / CIS Benchmarks, Encryption, IAM Policies, Network Segmentation).\n\n"
                    "System Architecture:\n{architecture}"
                )
                
                prompt = ChatPromptTemplate.from_template(prompt_template)
                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
                chain = prompt | llm | StrOutputParser()
                
                report = chain.invoke({"architecture": arch_input})
                st.markdown(report)
    else:
        st.info("💡 Please enter your OpenAI API Key in the sidebar to generate threat models.")
else:
    st.info("👈 Describe your target system architecture above to generate defensive security modeling.")
