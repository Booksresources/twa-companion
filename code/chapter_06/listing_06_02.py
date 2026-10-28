# Listing 6.2: Measuring Zipf's law
import numpy as np

all_tokens = [w.lower() for w in brown.words() if w.isalpha()]
counts = np.array(sorted(Counter(all_tokens).values(), reverse=True))
ranks = np.arange(1, len(counts) + 1)

slope, intercept = np.polyfit(np.log10(ranks[:1000]), np.log10(counts[:1000]), 1)
print(f"Most frequent word appears {counts[0]:,} times")
print(f"Words appearing once (hapax legomena): {(counts == 1).sum():,}")
print(f"Fitted Zipf exponent: {-slope:.2f}")
