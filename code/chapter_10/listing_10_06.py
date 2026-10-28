# Listing 10.6: Inspecting a dependency parse
doc = nlp("Northwind Systems acquired a small robotics startup.")
for t in doc:
    print(f"{t.text:10} {t.dep_:8} head={t.head.text}")
