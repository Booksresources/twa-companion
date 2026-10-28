"""Synthetic reviews of a fictional wireless earbud, 'Aurora X2', sold in several countries (12 months)."""
import random, datetime as dt, json
random.seed(21)
aspects = {
 "sound":   (["The sound is rich and clear", "Great bass and crisp sound", "Sound quality is excellent for the price"],
             ["Sound is tinny and flat", "The audio crackles at high volume"]),
 "battery": (["Battery easily lasts all day", "Battery life is impressive"],
             ["Battery drains in two hours now", "Since the update the battery dies very fast", "Battery life is terrible after the update"]),
 "comfort": (["Very comfortable even after hours", "They fit my ears perfectly"], ["They hurt my ears after an hour", "Keeps falling out when I run"]),
 "connection": (["Pairs instantly with my phone", "Bluetooth connection is stable"], ["Keeps disconnecting from my laptop", "Pairing is a nightmare"]),
 "delivery": (["Arrived quickly and well packed", "Fast delivery"], ["Delivery took three weeks", "Box arrived damaged"]),
}
es = {"good": ["Muy buen sonido, estoy contento", "La batería dura todo el día"], "bad": ["La batería se agota muy rápido después de la actualización", "Se desconecta todo el tiempo"]}
pt = {"good": ["Som excelente, recomendo", "Muito confortável"], "bad": ["A bateria acaba rápido depois da atualização", "Chegou com a caixa danificada"]}
countries = ["US", "GB", "IN", "NG", "KE", "PH", "MX", "ES", "BR", "AU"]
lang = {"MX": "es", "ES": "es", "BR": "pt"}
reviews = []; start = dt.date(2024, 7, 1)
for i in range(3000):
    d = start + dt.timedelta(days=random.randint(0, 364))
    month = (d.year - 2024) * 12 + d.month - 7          # 0..11
    after_update = month >= 7                            # firmware update in February 2025
    c = random.choice(countries); L = lang.get(c, "en")
    n_aspects = random.choice([1, 2, 2, 3])
    chosen = random.sample(list(aspects), n_aspects)
    if after_update and random.random() < 0.55 and "battery" not in chosen: chosen[0] = "battery"
    parts, score = [], 0
    for a in chosen:
        p_bad = 0.25 + (0.5 if a == "battery" and after_update else 0) + (0.05 if a == "connection" else 0)
        bad = random.random() < p_bad
        score += -1 if bad else 1
        if L == "en": parts.append(random.choice(aspects[a][1 if bad else 0]))
        else: parts.append(random.choice((es if L == "es" else pt)["bad" if bad else "good"]))
    rating = max(1, min(5, round(3 + score * 0.9 + random.gauss(0, 0.6))))
    reviews.append({"id": i + 1, "date": d.isoformat(), "country": c, "language": L,
                    "rating": rating, "text": ". ".join(parts) + "."})
json.dump(reviews, open("reviews.json", "w"), ensure_ascii=False)
print(len(reviews), "reviews")
