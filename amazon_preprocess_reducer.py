#!/usr/bin/env python
import sys
import numpy as np

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# # Define parameters that match your training.
# max_words = 20000
# max_len = 500

# # In a real scenario, you should load your tokenizer that was fitted during training (e.g., via pickle).
# # For demonstration, we initialize a new Tokenizer. (This is a placeholder.)
# tokenizer = Tokenizer(num_words=max_words)
# # WARNING: The vocabulary must match the one used in training.

# # Load the trained RMDL model.
# # The model file is distributed to this reducer via the -cacheFile option (with alias "rmdl_trained_model.keras").
# model = load_model("rmdl_trained_model.keras")

# def preprocess_review(review_text):
#     """
#     Tokenize and pad the review text. In a real system, use the same preprocessing as in training.
#     """
#     # Convert review to sequence (Note: you must use the same tokenizer as during training)
#     seq = tokenizer.texts_to_sequences([review_text])
#     padded = pad_sequences(seq, maxlen=max_len)
#     return padded

# for line in sys.stdin:
#     # Each line from the mapper is: review_id <tab> review_text
#     parts = line.strip().split('\t', 1)
#     if len(parts) < 2:
#         continue
#     review_id, review_text = parts[0], parts[1]
#     try:
#         processed = preprocess_review(review_text)
#         preds = model.predict(processed)
#         # For binary classification, assume model.predict returns a probability vector.
#         predicted_label = int(np.argmax(preds, axis=1)[0])
#         confidence = float(np.max(preds, axis=1)[0])
#         # Output: review_id, original review_text, predicted label, confidence
#         print(f"{review_id}\t{review_text}\t{predicted_label}\t{confidence:.4f}")
#     except Exception as e:
#         print(f"ERROR processing review_id {review_id}: {e}", file=sys.stderr)
