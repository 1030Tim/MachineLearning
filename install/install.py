import pandas as pd
url = "https://raw.githubusercontent.com/ShiYu0318/SCIST_2025_WC_AI/main/study_hours_scores.csv"
data = pd.read_csv(url)
data.to_csv("Study_Hourse_and_Scorse.csv",index=False)
