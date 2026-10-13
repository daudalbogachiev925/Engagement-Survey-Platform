import pandas as pd
import numpy as np
from src.survey import DEFAULT_QUESTIONS

def generate_responses(n_employees=200, seed=42):
    np.random.seed(seed)
    teams = ["Backend", "Frontend", "Sales", "HR", "Design", "Support"]
    rows = []
    for emp in range(n_employees):
        team = np.random.choice(teams)
        base = np.random.normal(3.8, 0.7)
        for q in DEFAULT_QUESTIONS:
            score = np.clip(np.random.normal(base, 0.5), 1, 5)
            rows.append({
                "employee_id": f"E{emp:04d}",
                "team": team,
                "q_id": q.id,
                "category": q.category,
                "score": round(score, 1),
            })
    return pd.DataFrame(rows)
