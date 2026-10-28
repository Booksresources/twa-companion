# Listing 9.6: Topic prevalence and the topic mixture of one article
import pandas as pd

labels = ["Currency markets", "Trade policy", "Oil and energy",
          "Quarterly earnings", "Economic indicators", "Agricultural commodities",
          "Corporate deals", "Banking and money", "Share offers",
          "Metals and commodities", "Dividends (mixed)", "Finance ministers"]

shares = pd.Series(doc_topics.mean(axis=0), index=labels).sort_values(
    ascending=False
)
print((shares * 100).round(1).head(6).to_string())

fileids = reuters.fileids()
i = fileids.index("test/16762")            # an article about oil exports
print(
    "\nArticle",
    fileids[i],
    "tagged by Reuters as",
    reuters.categories(fileids[i]),
)
mix = pd.Series(doc_topics[i], index=labels).sort_values(ascending=False)
print((mix.head(3) * 100).round(1).to_string())
