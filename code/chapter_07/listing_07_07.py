# Listing 7.7: Saving, loading, and applying a trained model
import joblib

best = search.best_estimator_
joblib.dump(best, "reuters_topic_model.joblib")

model = joblib.load("reuters_topic_model.joblib")
headlines = ["Central bank raises key lending rate by half a point",
             "Company agrees to buy rival in two billion dollar deal",
             "OPEC members discuss output cuts as oil prices slide"]
for h, topic in zip(headlines, model.predict(headlines)):
    print(f"{topic:9} {h}")
