# Listing 18.8: Automated tests for the redaction and validation functions
"""test_pipeline.py: run with  pytest -q"""
import pandas as pd
import pytest
from redact import redact
from review_pipeline import validate

@pytest.mark.parametrize("text, expected", [
    ("Write to ana.silva@example.com", "Write to [EMAIL]"),
    ("Call +254 20 555 0199 today", "Call [PHONE] today"),
    ("Card 5500 0000 0000 0004 declined", "Card [CARD] declined"),
    ("Thanks @lee_j!", "Thanks [USER]!"),
    ("No personal data here.", "No personal data here."),
])
def test_redact(text, expected):
    assert redact(text) == expected

def test_validate_accepts_good_data():
    df = pd.DataFrame({"id": [1, 2], "rating": [5, 1], "text": ["Great", "Bad"]})
    assert validate(df) == []

def test_validate_reports_problems():
    df = pd.DataFrame({"id": [1, 1], "rating": [6, 3], "text": ["Fine", None]})
    assert set(validate(df)) == {
        "missing text",
        "rating out of range",
        "duplicate ids",
    }


@pytest.mark.xfail(
    reason="pattern-based redaction cannot detect names (Section 18.4)"
)
def test_redact_names():
    assert "Ana Silva" not in redact("Please contact Ana Silva about the refund")
