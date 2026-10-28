# Listing 15.4: Training a byte-pair encoding tokenizer
from nltk.corpus import brown
from tokenizers import Tokenizer, models, trainers, pre_tokenizers

tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
trainer = trainers.BpeTrainer(vocab_size=8000, special_tokens=["[UNK]", "[PAD]"])
sentences = (" ".join(s).lower() for s in brown.sents())
tokenizer.train_from_iterator(sentences, trainer)

for word in [
    "running",
    "unbelievable",
    "reinstallation",
    "decarbonization",
    "nairobi",
]:
    print(f"{word:16} -> {tokenizer.encode(word).tokens}")
