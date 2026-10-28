# Listing 3.8: Saving records as JSON Lines and in SQLite
import sqlite3
import pandas as pd

books = pd.DataFrame({
    "title": ["A Light in the Attic", "Tipping the Velvet", "Soumission"],
    "price": [51.77, 53.74, 50.10],
    "rating": [3, 1, 1],
    "collected_at": pd.Timestamp("2025-06-01T10:00:00Z"),
})

books.to_json("books.jsonl", orient="records", lines=True, date_format="iso")

with sqlite3.connect("collection.db") as conn:
    books.to_sql("books", conn, if_exists="replace", index=False)
    result = pd.read_sql("SELECT title, price FROM books WHERE rating >= 3", conn)
print(result)
