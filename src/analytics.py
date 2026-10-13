import pandas as pd

def category_scores(df):
    """df: employee_id, team, q_id, score"""
    return df.groupby("q_id")["score"].mean().round(2)

def team_heatmap(df):
    return df.pivot_table(index="team", columns="q_id", values="score", aggfunc="mean").round(2)

def trend(df, q_id):
    return df[df["q_id"] == q_id].groupby("date")["score"].mean()
