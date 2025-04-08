import sys
from collections import defaultdict

# Store predictions
predictions = defaultdict(list)

# Read input from Mapper
for line in sys.stdin:
    review, prediction = line.strip().split("\t")
    predictions[review].append(int(prediction))

# Majority voting for each review
for review, preds in predictions.items():
    final_pred = round(sum(preds) / len(preds))  # Majority vote
    sentiment = "Positive" if final_pred == 1 else "Negative"
    print(f"{review}\t{sentiment}")
