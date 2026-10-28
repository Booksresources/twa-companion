# Listing 7.9: Inspecting misclassified test articles
svm.fit(train["text"], train["topic"])
errors = test.assign(predicted=svm.predict(test["text"]))
errors = errors[errors["topic"] != errors["predicted"]]
print(len(errors), "errors out of", len(test))
for _, row in errors.sample(6, random_state=3).iterrows():
    headline = row["text"].strip().split("\n")[0].replace("&lt;", "<")[:56]
    print(f"{row['topic']:>9} -> {row['predicted']:<9} {headline}")
