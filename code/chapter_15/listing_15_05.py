# Listing 15.5: Ready-made pipelines for common tasks
from transformers import pipeline

ner = pipeline("ner", model="Davlan/xlm-roberta-base-ner-hrl",
               aggregation_strategy="simple")
print(ner("Wangari Maathai founded the Green Belt Movement in Nairobi."))

zero_shot = pipeline("zero-shot-classification",
                     model="joeddav/xlm-roberta-large-xnli")
print(zero_shot("The bus was forty minutes late again this morning.",
      candidate_labels=["punctuality", "price", "cleanliness", "safety"]))

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print(summarizer(long_article, max_length=80, min_length=30)[0]["summary_text"])
