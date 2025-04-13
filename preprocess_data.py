import pandas as pd
import string

# Load the raw dataset (adjust the file path as needed)
data = pd.read_csv('dataset/sample.csv')

# # Fill missing values and combine title and text into a single review field
# data['title'] = data['title'].fillna('')
# data['text'] = data['text'].fillna('')
# data['review'] = data['title'] + " " + data['text']

# Clean the review text: lower-case and remove punctuation
def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

data['review'] = data['review'].apply(clean_text)

# Convert polarity: assuming polarity=1 (negative) becomes 0, polarity=2 (positive) becomes 1.
data['label'] = data['polarity'].apply(lambda x: 0 if x == 1 else 1)

# Save the preprocessed data to a new CSV (only the review and label columns)
data[['review', 'label']].to_csv('preprocessed_reviews.csv', index=False)
print("Preprocessing complete. Saved preprocessed_reviews.csv")
