# Listing 16.2: A wrapper for calling a hosted LLM (requires an API key)
import os
import anthropic   # pip install anthropic; other providers have similar libraries

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def call_llm(prompt, model="MODEL_NAME", max_tokens=300, temperature=0.0):
    response = client.messages.create(
        model=model, max_tokens=max_tokens, temperature=temperature,
        messages=[{"role": "user", "content": prompt}])
    return response.content[0].text

raw = call_llm(build_prompt("Mi pedido llegó roto y nadie responde mis correos."))
