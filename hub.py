import streamlit as st
from config import DASHBOARDS
from auth import check_role
from utils import render_status_badge, log_access

st.set_page_config(page_title="운영 대시보드 허브", page_icon="📊", layout="wide")

st.title("📊 운영 대시보드 허브")
st.caption("전사 운영 · 분석 · 보안 통합 포털")
st.divider()

role = check_role()
log_access(role)

st.markdown(f"### 현재 역할: `{role}`")
st.divider()

cols = st.columns(2)
idx = 0

for dash in DASHBOARDS:
    if role in dash["roles"]:
        with cols[idx % 2]:
            st.markdown(f"### {dash['name']}")
            render_status_badge(dash["status"])
            st.caption(dash["desc"])
            st.link_button("대시보드 열기", dash["url"], use_container_width=True)
        idx += 1

if idx == 0:
    st.warning("접근 가능한 대시보드가 없습니다.")