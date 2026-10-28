# Listing 11.3: Comparing clusters with known topics
table = pd.crosstab(pd.Series(topics, name="Reuters topic"),
                    pd.Series(km.labels_, name="cluster"))
print(table)
