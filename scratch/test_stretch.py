import streamlit as st
import plotly.express as px

try:
    fig = px.line(x=[1], y=[1])
    st.plotly_chart(fig, width="stretch")
    print("SUCCESS: width='stretch' works for plotly_chart!")
except Exception as e:
    print(f"FAILED: {e}")
