# Listing 6.5: Comparing readability scores
import textstat

texts = {
    "Plain notice": "Your parcel is on its way. It will arrive on Friday. "
    "Please be at home to sign for it.",
    "Policy text": "Notwithstanding the aforementioned provisions, beneficiaries "
    "shall demonstrate continuous eligibility through "
    "comprehensive "
    "documentation substantiating their circumstances.",
}
for name, text in texts.items():
    print(f"{name:13} Flesch ease={textstat.flesch_reading_ease(text):6.1f}  "
          f"grade={textstat.flesch_kincaid_grade(text):5.1f}")
