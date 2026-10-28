# Listing 16.5: The retrieval half of a RAG system
from nltk.corpus import reuters
from nltk.tokenize import sent_tokenize

# 1. Split documents into passages of up to three sentences
passages = []
for fid in reuters.fileids("crude"):
    sents = sent_tokenize(" ".join(reuters.raw(fid).split()))
    passages += [(fid, " ".join(sents[i:i + 3])) for i in range(0, len(sents), 3)]

# 2. Index the passages
rag_vec = TfidfVectorizer(stop_words="english", sublinear_tf=True).fit(
    [p for _, p in passages]
)
P = rag_vec.transform([p for _, p in passages])

def retrieve(question, k=4):
    sims = cosine_similarity(rag_vec.transform([question]), P).ravel()
    return [
        (passages[i][0], passages[i][1], sims[i])
        for i in sims.argsort()[::-1][:k]
    ]

# 3. Build a grounded prompt with numbered sources
def rag_prompt(question, k=4):
    hits = retrieve(question, k)
    sources = "\n\n".join(
        f"[{n}] ({fid}) {text}" for n, (fid, text, _) in enumerate(hits, 1)
    )
    prompt = (
        "Answer the question using only the sources below. Cite sources as [1], "
        "[2], ... "
        "If the sources do not contain the answer, say "
        f"so.\n\nSources:\n{sources}\n\n"
        f"Question: {question}"
    )
    return prompt, hits

prompt, hits = rag_prompt("Why did Ecuador want a higher OPEC quota?")
print(len(passages), "passages indexed")
for fid, text, score in hits:
    print(f"{score:.2f}  {fid}  {text[:60]}...")
print(f"Prompt length: {len(prompt.split())} words")
