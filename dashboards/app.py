import streamlit as st
from scripts.run_pipeline import run

st.title("Onchain Whale Tracker")

if st.button("Run Analysis"):
    run()
