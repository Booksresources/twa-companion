# Listing 17.6: Extracting skills from job postings
import re
import pandas as pd

jobs = pd.read_json("jobs.json")
jobs["role"] = jobs["title"].str.replace("Senior ", "", regex=False)
jobs["senior"] = jobs["title"].str.startswith("Senior")

SKILLS = {"Python": r"\bPython\b", "SQL": r"\bSQL\b", "R": r"\bR\b(?![-\w])",
          "Excel": r"\bExcel\b", "Power BI": r"Power ?BI", "Tableau": r"Tableau",
          "Spark": r"\bSpark\b", "Airflow": r"Airflow", "Docker": r"Docker",
          "Kubernetes": r"Kubernetes", "AWS": r"\bAWS\b", "Azure": r"Azure",
          "machine learning": r"machine learning", "NLP": r"\bNLP\b",
          "LLM": r"\bLLMs?\b", "PyTorch": r"PyTorch"}
for skill, pattern in SKILLS.items():
    jobs[skill] = jobs["description"].str.contains(pattern, regex=True)

demand = jobs.groupby("role")[list(SKILLS)].mean().mul(100).round(0).astype(int)
top = demand.T.sort_values("Data Scientist", ascending=False).head(8)
print(top)
