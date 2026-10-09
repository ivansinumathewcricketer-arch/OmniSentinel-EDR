import streamlit as st
import sqlite3
import datetime
import time

st.set_page_config(
    page_title="OmniSentinel EDR | Enterprise Command",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(\"\"\"
    <style>
    .main { background-color: #07090e; color: #f1f5f9; }
    .stSidebar { background-color: #0d1117; border-right: 1px solid #1f2937; }
    .hero-card {
        background: linear-gradient(135deg, #111827 0%, #0b0f19 100%);
        border: 1px solid #1e3a8a; padding: 30px; border-radius: 16px;
        box-shadow: 0 0 30px rgba(30, 58, 138, 0.2); margin-bottom: 25px;
    }
    .module-card {
        background: #0f172a; border: 1px solid #334155; padding: 24px;
        border-radius: 12px; height: 100%; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    .card-title { font-size: 18px; font-weight: 700; color: #38bdf8; margin-bottom: 10px; }
    .card-desc { font-size: 14px; color: #94a3b8; line-height: 1.5; }
    .metric-box {
        background: #111827; border: 1px solid #1f2937; padding: 15px;
        border-radius: 10px; text-align: center;
    }
    .metric-label { font-size: 12px; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }
    .metric-val { font-size: 24px; font-weight: 800; color: #34d399; }
    .badge-live { background-color: #065f46; color: #34d399; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    </style>
\"\"\", unsafe_allow_html=True)

def init_db():
    conn = sqlite3.connect('omni_sentinel_audit.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS events (timestamp TEXT, event_type TEXT, severity TEXT, description TEXT)''')
    conn.commit()
    conn.close()

init_db()

st.sidebar.markdown("### 🛡️ OMNISENTINEL CORE")
st.sidebar.markdown("<span class='badge-live'>● SYSTEM ONLINE</span>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Threat Simulation Engine")

if st.sidebar.button("🚨 Trigger C2 Outbound Beacon"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('omni_sentinel_audit.db')
    c = conn.cursor()
    c.execute('INSERT INTO events (timestamp, event_type, severity, description) VALUES (?, ?, ?, ?)', 
              (timestamp, 'C2_SOCKET_INTERCEPT', 'CRITICAL', 'Outbound reverse shell TCP connection intercepted & severed.'))
    conn.commit()
    conn.close()
    st.sidebar.success("C2 Beacon Neutralized!")
    time.sleep(0.3)
    st.rerun()

if st.sidebar.button("🔒 Trigger VSS Ransomware Attack"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect('omni_sentinel_audit.db')
    c = conn.cursor()
    c.execute('INSERT INTO events (timestamp, event_type, severity, description) VALUES (?, ?, ?, ?)', 
              (timestamp, 'VSS_CANARY_TRIP', 'EMERGENCY', 'Blocked unauthorized Volume Shadow Copy purge attempt.'))
    conn.commit()
    conn.close()
    st.sidebar.error("Ransomware Shadow Copy Deletion Blocked!")
    time.sleep(0.3)
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Navigation Guidelines")
st.sidebar.markdown("* **Hero Overview:** Mission & identity.\\n* **Architecture Blocks:** Deep dive into FIM & VSS.\\n* **Telemetry Ledger:** Live audit logs.")

st.markdown(\"\"\"
    <div class="hero-card">
        <h1 style="color: #f8fafc; margin-bottom: 10px;">🛡️ OmniSentinel EDR Command Center</h1>
        <p style="color: #94a3b8; font-size: 16px; margin-bottom: 20px;">
            Next-generation automated endpoint threat detection, zero-trust behavioral correlation, and immutable forensic auditing.
        </p>
    </div>
\"\"\", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-box"><div class="metric-label">Active Nodes</div><div class="metric-val" style="color: #38bdf8;">1 Agent</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-box"><div class="metric-label">Canary Guards</div><div class="metric-val">ARMED</div></div>', unsafe_allow_html=True)
with m3:
    conn = sqlite3.connect('omni_sentinel_audit.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM events")
    count = c.fetchone()[0]
    conn.close()
    st.markdown(f'<div class="metric-box"><div class="metric-label">Threats Intercepted</div><div class="metric-val" style="color: #f59e0b;">{count}</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-box"><div class="metric-label">Security Posture</div><div class="metric-val" style="color: #ef4444;">DEFCON 2</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("## 🏛️ Core Security Architecture & Guidelines")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown('<div class="module-card"><div class="card-title">📁 File Integrity Monitoring (FIM)</div><div class="card-desc"><b>Guideline & Purpose:</b> Scans system directories.<br><br><b>How It Operates:</b> Computes cryptographic hashes in real time to catch unauthorized file modifications.</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="module-card"><div class="card-title">🛡️ VSS Canary Guards</div><div class="card-desc"><b>Guideline & Purpose:</b> Shields system backup states.<br><br><b>How It Operates:</b> Deploys digital traps intercepting shadow copy purges via vssadmin.</div></div>', unsafe_allow_html=True)
with col_b:
    st.markdown('<div class="module-card"><div class="card-title">🌐 C2 Behavioral Correlation</div><div class="card-desc"><b>Guideline & Purpose:</b> Intercepts rogue outbound telemetry.<br><br><b>How It Operates:</b> Analyzes active socket patterns against threat signatures.</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="module-card"><div class="card-title">🗄️ SQLite Forensic Audit Ledger</div><div class="card-desc"><b>Guideline & Purpose:</b> Maintains immutable local event logs.<br><br><b>How It Operates:</b> Timestamp-stamps and severity-tags every anomaly into a secure ledger.</div></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 📋 Live Threat Telemetry & Forensic Audit Ledger")

conn = sqlite3.connect('omni_sentinel_audit.db')
cursor = conn.cursor()
cursor.execute("SELECT timestamp, event_type, severity, description FROM events ORDER BY rowid DESC")
rows = cursor.fetchall()
conn.close()

if rows:
    table_data = [{"Timestamp": r[0], "Event Type": r[1], "Severity": r[2], "Description": r[3]} for r in rows]
    st.dataframe(table_data, use_container_width=True)
else:
    st.info("No security incidents recorded yet. Use the sidebar simulation buttons to trigger live telemetry!")
