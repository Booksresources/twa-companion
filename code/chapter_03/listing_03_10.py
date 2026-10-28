# Listing 3.10: A SQLite page cache for resumable collection
import sqlite3
import hashlib
from datetime import datetime, timezone

class PageCache:
    """Stores every downloaded page so that crawls can resume and be repeated."""
    def __init__(self, path="page_cache.db"):
        self.db = sqlite3.connect(path)
        self.db.execute("""CREATE TABLE IF NOT EXISTS pages (
            url TEXT PRIMARY KEY, status INTEGER, fetched_at TEXT,
            sha256 TEXT, body TEXT)""")
        self.hits = self.downloads = 0

    def get(self, session, url, delay=1.0):
        row = self.db.execute(
            "SELECT body FROM pages WHERE url = ?", (url,)
        ).fetchone()
        if row:
            self.hits += 1
            return row[0]
        response = polite_get(session, url, delay=delay)
        body = response.text
        self.db.execute(
            "INSERT OR REPLACE INTO pages VALUES (?, ?, ?, ?, ?)",
            (
                url,
                response.status_code,
                datetime.now(timezone.utc).isoformat(),
                hashlib.sha256(body.encode()).hexdigest(),
                body,
            ),
        )
        self.db.commit()
        self.downloads += 1
        return body
