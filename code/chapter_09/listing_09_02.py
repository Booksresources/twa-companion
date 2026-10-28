# Listing 9.2: Displaying the top words of each topic
def show_topics(model, terms, n=8):
    for k, weights in enumerate(model.components_):
        top = terms[weights.argsort()[-n:][::-1]]
        print(f"Topic {k:2}: {' '.join(top)}")

show_topics(lda, terms)
