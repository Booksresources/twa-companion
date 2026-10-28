# Listing 15.7: Counting the parameters of transformer encoders
def encoder_parameters(vocab=30522, d=768, layers=12, ff=3072, max_pos=512):
    # tokens, positions, segments, norm
    embeddings = vocab * d + max_pos * d + 2 * d + 2 * d
    # Q, K, V, output + norm
    attention = 4 * (d * d + d) + 2 * d
    # two linear layers + norm
    feed_forward = (d * ff + ff) + (ff * d + d) + 2 * d
    pooler = d * d + d
    return embeddings + layers * (attention + feed_forward) + pooler

for name, cfg in {
    "BERT-base": dict(),
    "BERT-large": dict(d=1024, layers=24, ff=4096),
    "Small (6 layers)": dict(d=384, layers=6, ff=1536),
}.items():
    n = encoder_parameters(**cfg)
    print(f"{name:17} {n / 1e6:6.1f} million parameters  "
          f"~{n * 4 / 1e9:.2f} GB in 32-bit floats")
