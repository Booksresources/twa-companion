# Listing 16.7: Estimating the cost of large-scale LLM processing
def estimate_cost(n_texts, avg_words, prompt_words, output_words,
                  price_in_per_m, price_out_per_m, tokens_per_word=1.4):
    """Rough cost in currency units; prices are per million tokens."""
    tokens_in = n_texts * (avg_words + prompt_words) * tokens_per_word
    tokens_out = n_texts * output_words * tokens_per_word
    return tokens_in / 1e6 * price_in_per_m + tokens_out / 1e6 * price_out_per_m

# Hypothetical prices for a small and a large model; check current rates
for name, p_in, p_out in [
    ("small model", 0.25, 1.25),
    ("large model", 5.0, 25.0),
]:
    cost = estimate_cost(
        n_texts=100_000,
        avg_words=80,
        prompt_words=150,
        output_words=25,
        price_in_per_m=p_in,
        price_out_per_m=p_out,
    )
    print(f"{name:12} about {cost:,.0f} for 100,000 reviews")
