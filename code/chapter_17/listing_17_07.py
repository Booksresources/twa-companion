# Listing 17.7: Extracting salaries and computing a within-city pay index
SALARY = r"(?P<cur>[A-Z]{3}) (?P<low>[\d,]+) - (?P<high>[\d,]+) per year"
pay = jobs["description"].str.extract(SALARY)
jobs["salary_mid"] = (pay["low"].str.replace(",", "").astype(float)
                      + pay["high"].str.replace(",", "").astype(float)) / 2
print(f"Salary stated in {jobs['salary_mid'].notna().mean():.0%} of postings")

# Compare roles within each city, so that currencies and living costs cancel out
jobs["pay_index"] = jobs["salary_mid"] / jobs.groupby("city")[
    "salary_mid"
].transform("median")
print(jobs.groupby(["role", "senior"])["pay_index"].median().unstack().round(2))
