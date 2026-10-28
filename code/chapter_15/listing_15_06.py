# Listing 15.6: Fine-tuning a transformer classifier
# pip install transformers datasets torch evaluate
import numpy as np
from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)
from sklearn.metrics import f1_score

checkpoint = "distilbert-base-multilingual-cased"
data = load_dataset("csv", data_files={"train": "train.csv", "test": "test.csv"})
labels = sorted(set(data["train"]["label"]))
label2id = {l: i for i, l in enumerate(labels)}

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
def encode(batch):
    enc = tokenizer(batch["text"], truncation=True, max_length=256)
    enc["labels"] = [label2id[l] for l in batch["label"]]
    return enc
data = data.map(encode, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(
    checkpoint, num_labels=len(labels),
    id2label={i: l for l, i in label2id.items()}, label2id=label2id)

def metrics(pred):
    return {"macro_f1": f1_score(pred.label_ids, np.argmax(pred.predictions, -1),
                                 average="macro")}

args = TrainingArguments("model_out", num_train_epochs=3, learning_rate=2e-5,
                         per_device_train_batch_size=16, eval_strategy="epoch",
                         save_strategy="epoch", load_best_model_at_end=True,
                         metric_for_best_model="macro_f1", seed=42)
trainer = Trainer(model=model, args=args, train_dataset=data["train"],
                  eval_dataset=data["test"], processing_class=tokenizer,
                  compute_metrics=metrics)
trainer.train()
print(trainer.evaluate())
