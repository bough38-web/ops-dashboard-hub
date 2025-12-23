import streamlit as st

def check_role():
    return st.selectbox(
        "역할 선택",
        ["ops", "cs", "strategy", "sales", "security"],
        index=0
    )