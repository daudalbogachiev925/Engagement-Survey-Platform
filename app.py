import streamlit as st
import plotly.express as px
from src.data import generate_responses
from src.analytics import category_scores, team_heatmap
from src.enps import compute_enps, categorize
import numpy as np

st.title("💬 Engagement Survey Platform")

@st.cache_data
def load():
    return generate_responses()

df = load()

st.subheader("eNPS")
scores = np.random.randint(0, 11, 200).tolist()
enps = compute_enps(scores)
st.metric("eNPS", enps)
st.json(categorize(scores))

st.subheader("Средние по вопросам")
st.bar_chart(category_scores(df))

st.subheader("Heatmap по командам")
st.dataframe(team_heatmap(df).style.background_gradient(cmap="RdYlGn"))

st.subheader("Распределение по категориям")
cat = df.groupby("category")["score"].mean().reset_index()
st.plotly_chart(px.bar(cat, x="category", y="score", color="score"),
                use_container_width=True)
