# Listing 2.11: Fixing random seeds for repeatable results
import numpy as np
import pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)

reviews = pd.DataFrame({"id": range(1, 1001),
                        "rating": rng.integers(1, 6, size=1000)})
sample = reviews.sample(n=5, random_state=SEED)
print(sample)
