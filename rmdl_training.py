# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical
# import chardet
# import pickle

# from RMDL.RMDL_Text import Text_Classification

# # ---------------------------
# # Step 1: Load Preprocessed Data
# # ---------------------------
# # Preprocessed file should have two columns: review and label.
# # Since your dataset doesn't have a header originally, make sure the CSV was saved with a header.
# data = pd.read_csv(
#     'D:/Project/RMDL/preprocessed_reviews.csv',
#     encoding='latin1',
#     header=None,
#     names=['label', 'review'],
#     skipinitialspace=True
# )

# data['label'] = data['label'].astype(int)

# # ---------------------------
# # Step 2: Split Data
# # ---------------------------
# X_train, X_test, y_train, y_test = train_test_split(data['review'], data['label'], test_size=0.2, random_state=42)

# # ---------------------------
# # Step 3: Tokenize and Pad Text
# # ---------------------------
# max_words = 20000   # size of the vocabulary
# max_len = 100       # maximum length of each review (in tokens)

# tokenizer = Tokenizer(num_words=max_words)
# tokenizer.fit_on_texts(X_train)

# X_train_seq = tokenizer.texts_to_sequences(X_train)
# X_test_seq = tokenizer.texts_to_sequences(X_test)

# X_train_pad = pad_sequences(X_train_seq, maxlen=max_len)
# X_test_pad = pad_sequences(X_test_seq, maxlen=max_len)

# # ---------------------------
# # Step 4: Prepare Labels
# # ---------------------------
# num_classes = 2  # binary classification: negative or positive
# y_train_cat = to_categorical(y_train, num_classes=num_classes)
# y_test_cat = to_categorical(y_test, num_classes=num_classes)

# # ---------------------------
# # Step 5: Train the RMDL Model Using Predefined Functions
# # ---------------------------
# # Here we instantiate the RMDL model. The constructor parameters may vary.
# # For example, input_shape could be (max_len,) and we need to specify the number of classes.

# rmdl_model = Text_Classification(
#     x_train=X_train.tolist(),
#     y_train=y_train.tolist(),
#     x_test=X_test.tolist(),
#     y_test=y_test.tolist(),
#     batch_size=5,
#     sparse_categorical=0,
#     random_deep=[3, 3, 3],
#     epochs=[5, 5, 5],
#     plot=True
# )
# # ---------------------------
# # Step 6: Save the fitted tokenizer so you can re‑use the same word→index map
# # ---------------------------
# with open("tokenizer.pkl", "wb") as f:
#     pickle.dump(tokenizer, f)
# print("Saved model and tokenizer!")


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.utils import to_categorical
# from RMDL.RMDL_Text import Text_Classification
# import pickle

# # -- 1) Load preprocessed data (TSV with no header)
# df = pd.read_csv("D:/Project/RMDL/preprocessed_reviews.csv",
#                  encoding='latin1',
#                  sep="\t", header=None,
#                  names=["polarity","review"],
#                  skipinitialspace=True)

# # convert polarity to int
# df["polarity"] = df["polarity"].astype(int)

# # -- 2) Split
# X_train, X_test, y_train, y_test = train_test_split(df["review"].tolist(), df["polarity"].tolist(),test_size=0.2, random_state=42)

# # -- 3) Fit tokenizer
# max_words = 20000
# tokenizer = Tokenizer(num_words=max_words)
# tokenizer.fit_on_texts(X_train)

# # -- 4) Train RMDL
# rmdl_model = Text_Classification(
#     x_train=X_train,
#     y_train=y_train,
#     x_test=X_test,
#     y_test=y_test,
#     batch_size=5,
#     sparse_categorical=0,
#     random_deep=[3, 3, 3],
#     epochs=[5, 5, 5],
#     plot=True
# )

# # -- 5) Save artifacts
# with open("tokenizer.pkl","wb") as f:
#     pickle.dump(tokenizer, f)
# print("✅ Saved rmdl_trained_model.keras and tokenizer.pkl")


import pandas as pd
from tensorflow.keras.utils import to_categorical
from RMDL.RMDL_Text import Text_Classification

# 1) Load the preprocessed CSVs
#    We assume each CSV has no header, columns [label, review_text]
train = pd.read_csv("D:/Project/RMDL/dataset/preprocessed_train.csv",
                    encoding='latin1',
                    sep="\t", header=None,
                    names=["label","review"],
                    skipinitialspace=True)
test  = pd.read_csv("D:/Project/RMDL/dataset/preprocessed_test.csv",
                    encoding='latin1',
                    sep="\t", header=None,
                    names=["label","review"],
                    skipinitialspace=True)

# 2) Extract X/y and (optionally) one-hot encode y
X_train, y_train = train["review"].tolist(), train["label"].astype(int).tolist()
X_test,  y_test  = test["review"].tolist(),  test["label"].astype(int).tolist()

# 3) Call RMDL’s Text_Classification
rmdl_model = Text_Classification(
    x_train=X_train,
    y_train=y_train,
    x_test=X_test,
    y_test=y_test,
    batch_size=5,
    sparse_categorical=0,
    random_deep=[3, 3, 3],
    epochs=[5, 5, 5],
    plot=True
)