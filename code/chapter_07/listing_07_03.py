# Listing 7.3: The most influential words for each topic
import numpy as np

vec, lr = clf.named_steps["tfidf"], clf.named_steps["model"]
terms = vec.get_feature_names_out()
for topic, weights in zip(lr.classes_, lr.coef_):
    top = terms[np.argsort(weights)[-6:][::-1]]
    print(f"{topic:9} {', '.join(top)}")
