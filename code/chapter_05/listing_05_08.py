# Listing 5.8: Multilingual sentence embeddings (downloads a model on first use)
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
sentences = ["The parcel arrived late.",
             "My delivery was delayed.",
             "El paquete llegó tarde.",          # Spanish
             "The screen is very bright."]
embeddings = model.encode(sentences, normalize_embeddings=True)
print(embeddings.shape)
print(cosine_similarity(embeddings).round(2))
