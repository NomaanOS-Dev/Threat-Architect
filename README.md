# 🛡️ Threat-Architect

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://threat-architect.streamlit.app/)

An **AI-Powered Defensive Threat Modeling & Security Architecture Hardening Platform** designed to analyze system stack descriptions, identify attack surfaces, map threat vectors to the **MITRE ATT&CK Framework**, and generate NIST/CIS hardening recommendations.

Developed by **[NomaanOS-Dev](https://github.com/NomaanOS-Dev)**.

---

## 🚀 Key Features

* **Architecture Threat Analyzer:** Evaluates system components to identify high-risk attack surfaces.
* **MITRE ATT&CK Mapping:** Maps vulnerabilities directly to standardized MITRE Tactics & Techniques.
* **Defensive Hardening Roadmap:** Generates actionable security controls based on NIST & CIS Benchmarks.
* **Interactive Reporting:** Clean, real-time threat modeling reports powered by GPT-4o-mini.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Engine:** OpenAI `gpt-4o-mini` & LangChain Core
* **UI Framework:** Streamlit
* **Security Frameworks:** MITRE ATT&CK, NIST, CIS Controls

---

## 📦 Local Installation & Setup

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/NomaanOS-Dev/Threat-Architect.git](https://github.com/NomaanOS-Dev/Threat-Architect.git)
   cd Threat-Architect
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application:**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ License
Open-source security architecture modeling utility built for defensive cybersecurity research and SOC operations.
