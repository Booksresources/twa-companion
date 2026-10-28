# Listing 11.4: Clustering after latent semantic analysis
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline

lsa = make_pipeline(
    TruncatedSVD(n_components=100, random_state=42), Normalizer(copy=False)
)
Z = lsa.fit_transform(X)
print(
    "Variance kept by 100 components: "
    f"{lsa[0].explained_variance_ratio_.sum():.2f}"
)

for k in [4, 6, 8, 10]:
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(Z)
    print(f"k={k:2}  silhouette={silhouette_score(Z, labels):.3f}  "
          f"ARI={adjusted_rand_score(topics, labels):.3f}")
