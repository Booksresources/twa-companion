# Listing 10.10: Testing person-name recognition across name origins
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")
NAMES = {"West Africa": ["Chinedu Okafor", "Aminata Diallo", "Kwame Mensah",
                         "Folake Adeyemi", "Ousmane Traoré", "Ama Owusu"],
         "East Africa": ["Wanjiru Kamau", "Tesfaye Bekele", "Amina Hassan",
                         "Baraka Otieno", "Nyokabi Mwangi", "Yohannes Haile"],
         "South Asia": ["Priya Raghavan", "Arjun Mehta", "Farhana Akter",
                        "Nimal Perera", "Sunita Thapa", "Imran Qureshi"],
         "East Asia": ["Wei Zhang", "Yuki Tanaka", "Min-jun Park", "Mei Lin",
                       "Haruto Sato", "Seo-yeon Kim"],
         "Southeast Asia": ["Nguyen Thi Lan", "Siti Rahmawati", "Juan dela Cruz",
                            "Somchai Srisuk", "Dewi Lestari", "Tran Van Minh"],
         "Latin America": ["Camila Rodríguez", "Mateus Oliveira",
                           "Valentina Gómez", "Diego Fernández", "Lucía Morales",
                           "Thiago Souza"],
         "Middle East and North Africa": ["Layla Haddad", "Omar Benali",
                                          "Fatima Zahra", "Yousef Al-Masri",
                                          "Nour Khalil", "Karim Mansour"],
         "Europe and North America": ["Emma Schmidt", "Lucas Martin",
                                      "Sophie Dubois", "James Walker",
                                      "Anna Kowalski", "Oliver Hansen"]}
TEMPLATES = ["{n} spoke at the opening of the new library yesterday.",
             "The award was presented to {n} for her work on water quality.",
             "According to {n}, the project will finish next year."]

rows = []
for region, names in NAMES.items():
    for name in names:
        for t in TEMPLATES:
            doc = nlp(t.format(n=name))
            found = any(e.text == name and e.label_ == "PERSON" for e in doc.ents)
            rows.append({"region": region, "found": found})
recall = pd.DataFrame(rows).groupby("region")["found"].mean().sort_values()
print((recall * 100).round(0).astype(int).to_string())
print(
    f"\nOverall: {pd.DataFrame(rows)['found'].mean():.0%} of {len(rows)} mentions"
)
