# Listing 16.3: Validating model responses against a schema
import json
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class Classification(BaseModel):
    category: Literal[
        "delivery", "product_quality", "billing", "account", "other"
    ]
    confidence: float = Field(ge=0, le=1)
    reason: str

def parse_response(raw):
    text = raw.strip().removeprefix("```json").removesuffix("```").strip()
    try:
        return Classification.model_validate(json.loads(text)), None
    except (json.JSONDecodeError, ValidationError) as err:
        return None, type(err).__name__

# Example responses of the kinds models return (written for illustration)
responses = [
    '{"category": "delivery", "confidence": 0.92, "reason": "Parcel arrived '
    'broken."}',
    '```json\n{"category": "billing", "confidence": 0.8, "reason": '
    '"Double charge."}\n```',
    '{"category": "shipping", "confidence": 0.7, "reason": "Late ' 'parcel."}',
    'The message is about a delivery problem.',
]
for r in responses:
    result, error = parse_response(r)
    print(result.category if result else f"REJECTED ({error})")
