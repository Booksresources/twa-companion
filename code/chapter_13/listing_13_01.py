# Listing 13.1: Parsing a Combined Log Format file
import re
import pandas as pd

LOG = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) '
    r'\S+" '
    r'(?P<status>\d{3}) (?P<size>\d+) "(?P<referrer>[^"]*)" '
    r'"(?P<agent>[^"]*)"'
)

with open("access.log", encoding="utf-8") as f:
    rows = [m.groupdict() for line in f if (m := LOG.match(line))]
logs = pd.DataFrame(rows)
logs["time"] = pd.to_datetime(logs["time"], format="%d/%b/%Y:%H:%M:%S %z")
logs["status"] = logs["status"].astype(int)
print(
    len(logs),
    "requests from",
    logs["time"].min().date(),
    "to",
    logs["time"].max().date(),
)
print(logs[["time", "path", "status"]].head(3).to_string(index=False))
