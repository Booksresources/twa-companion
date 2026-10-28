# Listing 3.2: Searching an open API
params = {
    "action": "query",
    "list": "search",
    "srsearch": "text mining",
    "srlimit": 5,
    "format": "json",
}
session = make_session()
response = polite_get(session, "https://en.wikipedia.org/w/api.php",
                      params=params)
data = response.json()

for item in data["query"]["search"]:
    print(item["title"], "|", item["wordcount"], "words")
