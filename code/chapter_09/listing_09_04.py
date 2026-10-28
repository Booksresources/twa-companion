# Listing 9.4: Topic modeling with BERTopic (downloads an embedding model on first use)
# pip install bertopic
from bertopic import BERTopic

topic_model = BERTopic(embedding_model="paraphrase-multilingual-MiniLM-L12-v2",
                       min_topic_size=20)
topics, probs = topic_model.fit_transform(docs)

print(topic_model.get_topic_info().head(10))    # topic sizes and top words
print(topic_model.get_topic(0))                 # words and weights for topic 0
topic_model.visualize_barchart(top_n_topics=8)  # interactive Plotly chart
