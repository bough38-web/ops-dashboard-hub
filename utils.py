import streamlit as st
from datetime import datetime

def render_status_badge(status):
    colors = {
        "ok": "🟢 정상",
        "warning": "🟠 주의",
        "danger": "🔴 위험"
    }
    st.markdown(f"**상태:** {colors.get(status, '⚪ 알수없음')}")

def log_access(role):
    st.caption(f"접속 기록: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | role={role}")