# Listing 3.1: Reusable tools for polite, robust requests
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def make_session(contact="your.email@example.org"):
    session = requests.Session()
    session.headers["User-Agent"] = f"TWA-Book-Bot/1.0 (educational; {contact})"
    retry = Retry(total=3, backoff_factor=1.0,
                  status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def polite_get(session, url, delay=1.0, **kwargs):
    time.sleep(delay)                      # pause between requests
    response = session.get(url, timeout=10, **kwargs)
    response.raise_for_status()            # raise an error for 4xx/5xx codes
    return response
