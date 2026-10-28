# Listing 16.1: A prompt template for classification
CATEGORIES = {
    "delivery": "late, lost, or damaged parcels; courier problems",
    "product_quality": "defects, poor materials, items not as described",
    "billing": "charges, refunds, invoices, payment errors",
    "account": "login, password, profile, or app access problems",
    "other": "anything that fits none of the categories above",
}

def build_prompt(message):
    category_list = "\n".join(
        f"- {name}: {desc}" for name, desc in CATEGORIES.items()
    )
    return f"""You classify customer support messages for an online retailer.

Categories:
{category_list}

Instructions:
- Choose exactly one category.
- The message may be in any language; do not translate it in your answer.
- Respond only with JSON:
  {{"category": "<name>", "confidence": <0 to 1>, "reason": "<one sentence>"}}

Message:
<<<{message}>>>"""

print(build_prompt("Mi pedido llegó roto y nadie responde mis correos."))
