"""Synthetic online job postings for data roles in eight cities."""
import random, json
random.seed(5)
cities = {"Bengaluru": ("INR", 1_800_000, "lakh"), "Lagos": ("NGN", 9_000_000, None), "Nairobi": ("KES", 2_400_000, None),
          "São Paulo": ("BRL", 140_000, None), "Berlin": ("EUR", 62_000, None), "Toronto": ("CAD", 88_000, None),
          "Manila": ("PHP", 900_000, None), "Mexico City": ("MXN", 520_000, None)}
roles = {"Data Analyst": ["SQL", "Excel", "Power BI", "Tableau", "Python", "statistics"],
         "Data Scientist": ["Python", "machine learning", "SQL", "statistics", "scikit-learn", "NLP"],
         "Data Engineer": ["SQL", "Python", "Spark", "Airflow", "AWS", "Docker"],
         "ML Engineer": ["Python", "PyTorch", "Docker", "Kubernetes", "AWS", "NLP", "LLM"]}
extra = ["Git", "communication", "R", "Azure", "dbt", "Snowflake", "LLM", "Tableau"]
posts = []
for i in range(1200):
    city = random.choice(list(cities)); cur, base, _ = cities[city]
    role = random.choice(list(roles)); senior = random.random() < 0.35
    skills = random.sample(roles[role], k=random.randint(3, 5)) + random.sample(extra, k=random.randint(0, 2))
    if random.random() < 0.25 + 0.2 * (role in ("Data Scientist", "ML Engineer")): skills.append("LLM")
    skills = list(dict.fromkeys(skills))
    lo = int(base * (1.6 if senior else 1.0) * random.uniform(0.85, 1.15) * {"Data Analyst": 0.8, "Data Scientist": 1.1, "Data Engineer": 1.1, "ML Engineer": 1.25}[role])
    hi = int(lo * random.uniform(1.15, 1.35))
    salary = f"{cur} {lo:,} - {hi:,} per year" if random.random() < 0.7 else "Competitive salary"
    title = ("Senior " if senior else "") + role
    desc = (f"We are hiring a {title} in {city}. You will work with {', '.join(skills[:-1])} and {skills[-1]}. "
            f"Salary: {salary}. {'Hybrid' if random.random() < 0.5 else 'On-site'} role.")
    posts.append({"id": i + 1, "title": title, "city": city, "description": desc})
json.dump(posts, open("jobs.json", "w"), ensure_ascii=False)
print(len(posts), posts[0]["description"])
