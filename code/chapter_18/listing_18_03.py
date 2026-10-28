# Listing 18.3: A review monitoring dashboard
"""dashboard.py: run with  streamlit run dashboard.py"""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Aurora X2 review monitor", layout="wide")
st.title("Aurora X2 review monitor")

summary = pd.read_csv("outputs/monthly_summary.csv")
aspect = st.selectbox("Aspect", ["battery", "sound", "connection"])

col1, col2, col3 = st.columns(3)
latest, previous = summary.iloc[-1], summary.iloc[-2]
col1.metric("Reviews this month", int(latest["reviews"]),
            int(latest["reviews"] - previous["reviews"]))
col2.metric("Average rating", f"{latest['avg_rating']:.2f}",
            f"{latest['avg_rating'] - previous['avg_rating']:+.2f}")
col3.metric(f"Mentioning {aspect}", f"{latest[aspect + '_share']:.0%}")

st.plotly_chart(
    px.line(
        summary,
        x="month",
        y=["avg_rating"],
        markers=True,
        title="Average rating by month",
    ),
    use_container_width=True,
)
st.plotly_chart(
    px.bar(
        summary,
        x="month",
        y=f"{aspect}_share",
        title=f"Share of reviews mentioning {aspect}",
    ),
    use_container_width=True,
)
st.caption(
    "Source: review_pipeline.py output. Shares are keyword-based estimates."
)
