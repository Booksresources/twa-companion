# Listing 16.6: Comparing LLM labels with human labels
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    cohen_kappa_score,
    confusion_matrix,
)

def evaluate_labels(gold, predicted, labels):
    print(f"Accuracy {accuracy_score(gold, predicted):.2f}  "
          f"macro-F1 {f1_score(gold, predicted, average='macro'):.2f}  "
          f"Cohen's kappa {cohen_kappa_score(gold, predicted):.2f}")
    print(pd.DataFrame(confusion_matrix(gold, predicted, labels=labels),
                       index=labels, columns=labels))

# Illustrative: 20 messages labeled by a person and by an LLM
human = (
    ["delivery"] * 6 + ["billing"] * 5 + ["product_quality"] * 5 + ["account"] * 4
)
llm   = (["delivery"] * 5 + ["product_quality"] + ["billing"] * 5
         + ["product_quality"] * 3 + ["delivery"] * 2 + ["account"] * 4)
evaluate_labels(human, llm, ["delivery", "billing", "product_quality", "account"])
