"""Synthetic social media posts about the launch of a bus rapid transit (BRT) line in the fictional city of Novaterra."""
import random, json, datetime as dt
random.seed(11)
start = dt.datetime(2025, 5, 5, 6, 0)
users = [f"user{i:03d}" for i in range(600)]
influencers = ["novaterra_transit", "citydesk_news", "amara_reports", "greenways_ngo", "dev_and_data"]
bots = [f"promo_deals{i}" for i in range(4)] + [f"brt_alerts_x{i}" for i in range(2)]
pos = ["Loving the new #NovaBRT line, my commute is {n} minutes shorter!", "The #NovaBRT stations look great and the buses are clean",
       "Took the new bus with my kids today, smooth ride #NovaBRT #CommuteDiaries", "Finally a fast way across town #NovaBRT",
       "Me encanta el nuevo #NovaBRT, llegué al trabajo en {n} minutos", "Ônibus novo muito bom, viagem rápida #NovaBRT"]
neu = ["Anyone know the #NovaBRT schedule for Sunday?", "Map of the new #NovaBRT stations here", "Is the #NovaBRT card the same as the metro card?",
       "First week of #NovaBRT data: ridership update from the city", "¿A qué hora pasa el #NovaBRT por la estación central?"]
neg = ["Stuck for {n} minutes, no bus in sight #NovaBRT #BusDelay", "Breakdown on the #NovaBRT line again, terrible communication",
       "Why is nobody telling us what is happening? #BusDelay #NovaBRT", "Crowded platform, no updates, very frustrating #BusDelay",
       "Ônibus quebrado de novo, ninguém informa nada #BusDelay"]
spam = ["Best deals on phone cases today only!!! #NovaBRT #BusDelay #deals", "Click here for free travel credit #NovaBRT #win"]
posts = []; pid = 0
def add(t, u, text, repost_of=None):
    global pid; pid += 1
    posts.append({"id": pid, "time": t.isoformat(), "user": u, "text": text, "repost_of": repost_of})
    return pid
originals = []
for h in range(7*24):
    t0 = start + dt.timedelta(hours=h); hour = t0.hour
    base = [0.2,0.1,0.1,0.1,0.2,0.6,1.5,3,4,2.5,1.5,1.5,2,1.5,1.5,2,3,4,3,2,1.5,1,0.6,0.4][hour]
    disruption = 52 <= h <= 58                              # day 3, 10:00-16:00: line breakdown
    n = int(random.gauss(base*(16 if disruption else 4.5), 1.5))
    for _ in range(max(n, 0)):
        t = t0 + dt.timedelta(minutes=random.randint(0, 59))
        u = random.choice(users + influencers*12)
        r = random.random()
        if disruption: tpl = random.choice(neg) if r < 0.75 else random.choice(neu)
        else: tpl = random.choice(pos) if r < 0.55 else (random.choice(neu) if r < 0.85 else random.choice(neg))
        text = tpl.format(n=random.choice([10, 15, 20, 25, 40]))
        if u in influencers and random.random() < 0.5: text = text + f" @{random.choice(['novaterra_transit','citydesk_news'])}"
        pid_ = add(t, u, text); originals.append((pid_, u, t))
        k = random.randint(5, 40) if u in influencers else (random.randint(3, 15) if disruption and random.random() < 0.3 else (random.randint(0, 3) if random.random() < 0.3 else 0))
        for _ in range(k):
            add(t + dt.timedelta(minutes=random.randint(1, 240)), random.choice(users), "", repost_of=pid_)
for b in bots:                                              # bots: frequent, regular, repetitive
    t = start + dt.timedelta(minutes=random.randint(0, 50))
    while t < start + dt.timedelta(days=7):
        add(t, b, random.choice(spam)); t += dt.timedelta(minutes=random.choice([45, 45, 46, 44]))
posts.sort(key=lambda p: p["time"])
json.dump(posts, open("posts.json", "w"), ensure_ascii=False)
print(len(posts), "posts")
