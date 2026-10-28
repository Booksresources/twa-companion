# Listing 10.8: Extracting structured fields with regular expressions
import re

notice = (
    "Tender ref. NB-2025-0193 closes on 14/07/2025. Budget: EUR 1.2 million; "
    "queries to procurement@city.example.gov or +31 20 555 0147."
)
patterns = {
    "reference": r"\b[A-Z]{2}-\d{4}-\d{4}\b",
    "date": r"\b\d{2}/\d{2}/\d{4}\b",
    "amount": (r"\b(?:EUR|USD|GBP|INR|KES)\s?\d+(?:\.\d+)?"
               r"(?:\s(?:thousand|million|billion))?"),
    "email": r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",
    "phone": r"\+\d{1,3}(?:[\s-]?\d{2,4}){2,4}",
}
for field, pattern in patterns.items():
    print(f"{field:10} {re.findall(pattern, notice)}")
