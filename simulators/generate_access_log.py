"""Generate a synthetic web server access log for an online bookstore (Combined Log Format)."""
import random, datetime as dt
random.seed(7)
start = dt.datetime(2025, 3, 3, 0, 0, 0)
UAS = {"desktop": ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 Version/17.3 Safari/605.1.15"],
       "mobile": ["Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/122.0 Mobile Safari/537.36",
                  "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"]}
BOTS = ["Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"]
CATS = ["fiction", "science", "travel", "children", "languages"]
QUERIES = ["python", "data science", "harry potter", "atlas", "spanish course", "cookbook", "kids books",
           "machine learning", "swahili dictionary", "graphic novels", "japanese grammar", "poetry", "climate"]
ZERO = {"swahili dictionary", "graphic novels", "japanese grammar"}
UTC_OFFSETS = {"IN": 5, "BR": -3, "DE": 1, "NG": 1, "US": -5, "ID": 7, "MX": -6, "KE": 3}
lines = []
def ip(): return f"{random.randint(11,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
def log(t, addr, path, status, size, ref, ua):
    lines.append((t, f'{addr} - - [{t.strftime("%d/%b/%Y:%H:%M:%S")} +0000] "GET {path} HTTP/1.1" {status} {size} "{ref}" "{ua}"'))
for v in range(4200):
    device = "mobile" if random.random() < 0.58 else "desktop"
    ua = random.choice(UAS[device]); addr = ip(); country = random.choice(list(UTC_OFFSETS))
    nsess = 1 if random.random() < 0.75 else 2
    for s in range(nsess):
        day = random.randint(0, 13)
        local_hour = random.choices(range(24), weights=[1,1,1,1,1,2,3,5,7,8,8,8,9,9,8,8,8,9,10,11,11,9,6,3])[0]
        t = start + dt.timedelta(days=day, hours=(local_hour - UTC_OFFSETS[country]) % 24, minutes=random.randint(0, 59), seconds=random.randint(0,59))
        ref = random.choice(["https://www.google.com/", "https://www.google.com/", "-", "https://www.facebook.com/", "https://news.example.net/"])
        path = "/"; page = 0
        while True:
            log(t, addr, path, 200, random.randint(4000, 30000), ref, ua)
            if random.random() < 0.8: log(t + dt.timedelta(seconds=1), addr, "/static/app.js", 200, 81234, "-", ua)
            ref = "https://shop.example.com" + path; page += 1
            t += dt.timedelta(seconds=random.randint(8, 240))
            if path == "/":
                if random.random() < 0.38: break
                r = random.random()
                path = f"/category/{random.choice(CATS)}" if r < 0.6 else f"/search?q={random.choice(QUERIES).replace(' ', '+')}"
            elif path.startswith("/search"):
                q = path.split("=")[1].replace("+", " ")
                if q in ZERO:
                    if random.random() < 0.7: break
                    path = "/"
                else:
                    path = f"/product/{random.randint(100, 160)}" if random.random() < 0.7 else "/"
                    if random.random() < 0.15: break
            elif path.startswith("/category"):
                if random.random() < 0.3: break
                path = f"/product/{random.randint(100, 160)}"
            elif path.startswith("/product"):
                r = random.random()
                if r < 0.35: break
                elif r < 0.6: path = "/cart"
                elif r < 0.85: path = f"/product/{random.randint(100, 160)}"
                else: path = "/"
            elif path == "/cart":
                if random.random() < 0.3: break
                path = "/checkout"
            elif path == "/checkout":
                p = 0.55 if device == "desktop" else 0.27      # planted problem: mobile checkout
                if random.random() < p: path = "/confirmation"
                else: break
            elif path == "/confirmation":
                break
            if page > 25: break
# bots and errors
for b in range(900):
    t = start + dt.timedelta(seconds=random.randint(0, 14*86400))
    log(t, ip(), random.choice(["/", f"/product/{random.randint(100,160)}", f"/category/{random.choice(CATS)}", "/robots.txt"]), 200, 5000, "-", random.choice(BOTS))
for e in range(120):
    t = start + dt.timedelta(seconds=random.randint(0, 14*86400))
    log(t, ip(), random.choice(["/old-offers", "/product/999", "/wp-login.php"]), 404, 512, "-", random.choice(UAS["desktop"]))
lines.sort(key=lambda x: x[0])
open("access.log", "w").write("\n".join(l for _, l in lines) + "\n")
print(len(lines), "lines")
