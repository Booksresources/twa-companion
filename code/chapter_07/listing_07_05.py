# Listing 7.5: The effect of balanced class weights
from sklearn.metrics import f1_score

for weight in [None, "balanced"]:
    pipe = Pipeline([("tfidf", TfidfVectorizer(stop_words="english", min_df=2,
                                               sublinear_tf=True)),
                     ("model", LinearSVC(class_weight=weight))])
    pipe.fit(train["text"], train["topic"])
    p = pipe.predict(test["text"])
    per_class = f1_score(
        test["topic"], p, average=None, labels=["interest", "money-fx"]
    )
    print(
        f"class_weight={str(weight):9} "
        f"macro-F1={f1_score(test['topic'], p, average='macro'):.3f}"
        f"  interest={per_class[0]:.3f}  money-fx={per_class[1]:.3f}"
    )
