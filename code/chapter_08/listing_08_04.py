# Listing 8.4: Multilingual sentiment with a pretrained transformer
# pip install transformers torch
from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
texts = ["The new update is fantastic!",
         "La aplicación se cierra cada vez que la abro.",   # Spanish
         "Le service client était correct, sans plus."]     # French
for text, result in zip(texts, classifier(texts)):
    print(result["label"], round(result["score"], 2), "|", text)
