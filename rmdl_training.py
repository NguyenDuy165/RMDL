import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import chardet

from RMDL.RMDL_Text import Text_Classification

# ---------------------------
# Step 1: Load Preprocessed Data
# ---------------------------
# Preprocessed file should have two columns: review and label.
# Since your dataset doesn't have a header originally, make sure the CSV was saved with a header.
data = pd.read_csv(
    'D:/Project/RMDL/preprocessed_reviews.csv',
    encoding='latin1',
    header=None,
    names=['label', 'review'],
    skipinitialspace=True
)

data['label'] = data['label'].astype(int)

# ---------------------------
# Step 2: Split Data
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(data['review'], data['label'], test_size=0.2, random_state=42)

# ---------------------------
# Step 3: Tokenize and Pad Text
# ---------------------------
max_words = 20000   # size of the vocabulary
max_len = 100       # maximum length of each review (in tokens)

# tokenizer = Tokenizer(num_words=max_words)
# tokenizer.fit_on_texts(X_train)
# X_train_seq = tokenizer.texts_to_sequences(X_train)
# X_test_seq = tokenizer.texts_to_sequences(X_test)

# X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
# X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

# ---------------------------
# Step 4: Prepare Labels
# ---------------------------
num_classes = 2  # binary classification: negative or positive
y_train_cat = to_categorical(y_train, num_classes=num_classes)
y_test_cat = to_categorical(y_test, num_classes=num_classes)

# ---------------------------
# Step 5: Train the RMDL Model Using Predefined Functions
# ---------------------------
# Here we instantiate the RMDL model. The constructor parameters may vary.
# For example, input_shape could be (max_len,) and we need to specify the number of classes.

rmdl_model = Text_Classification(
    x_train=X_train.tolist(),
    y_train=y_train.tolist(),
    x_test=X_test.tolist(),
    y_test=y_test.tolist(),
    batch_size=5,
    sparse_categorical=0,
    random_deep=[3, 3, 3],
    epochs=[5, 5, 5],
    plot=True
)
