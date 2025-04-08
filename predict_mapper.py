import sys
import joblib
import numpy as np
from RMDL import text_feature_extraction as txt

# Load the test model
model = joblib.load("rmdl_final_test.joblib")

# Process only 5 records
for i, line in enumerate(sys.stdin):
    if i >= 5:  # Stop after 5 reviews
        break

    review = line.strip()
    cleaned_review = txt.text_cleaner(review)

    # Convert text to input format
    X_new = np.array([cleaned_review])

    # Predict sentiment
    prediction = np.argmax(model.predict(X_new), axis=-1)[0]

    # Output for Reducer
    print(f"{review}\t{prediction}")
