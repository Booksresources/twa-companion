# Listing 13.7: Evaluating an A/B test of conversion rates
from math import sqrt
from scipy.stats import norm

def ab_test(conv_a, n_a, conv_b, n_b, alpha=0.05):
    p_a, p_b = conv_a / n_a, conv_b / n_b
    pooled = (conv_a + conv_b) / (n_a + n_b)
    se_pooled = sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
    z = (p_b - p_a) / se_pooled
    p_value = 2 * (1 - norm.cdf(abs(z)))
    se_diff = sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
    margin = norm.ppf(1 - alpha / 2) * se_diff
    print(
        f"Control: {p_a:.1%}   Variant: {p_b:.1%}   Difference: "
        f"{100 * (p_b - p_a):+.1f} points"
    )
    print(
        f"95% CI: [{100 * (p_b - p_a - margin):+.1f}, "
        f"{100 * (p_b - p_a + margin):+.1f}] points"
    )
    print(f"z = {z:.2f}, p-value = {p_value:.4f}")

# Mobile sessions that reached checkout during a four-week experiment
ab_test(conv_a=412, n_a=1480, conv_b=511, n_b=1495)
