# import tensorflow as tf
# print(tf.__version__)
# # 1) List GPUs
# print("GPUs:", tf.config.list_physical_devices('GPU'))
# # 2) Get build info dict
# build_info = tf.sysconfig.get_build_info()
# print("CUDA version:", build_info.get('cuda_version', 'unknown'))
# print("cuDNN version:", build_info.get('cudnn_version', 'unknown'))

import pandas as pd
from tensorflow.keras.utils import to_categorical
from RMDL.RMDL_Text import Text_Classification
import time

# 1) Load the preprocessed CSVs
#    We assume each CSV has no header, columns [label, review_text]
train = pd.read_csv("D:/Project/RMDL/dataset/preprocessed_train_sample_100000.csv",
                    encoding='latin1',
                    sep="\t", header=None,
                    names=["label","review"],
                    skipinitialspace=True)
test  = pd.read_csv("D:/Project/RMDL/dataset/preprocessed_test_sample_10000.csv",
                    encoding='latin1',
                    sep="\t", header=None,
                    names=["label","review"],
                    skipinitialspace=True)

# 2) Extract X/y and (optionally) one-hot encode y
X_train, y_train = train["review"].tolist(), train["label"].astype(int).tolist()
X_test,  y_test  = test["review"].tolist(),  test["label"].astype(int).tolist()


# Start timer
start_time = time.perf_counter()

# 3) Call RMDL’s Text_Classification
rmdl_model = Text_Classification(
    x_train=X_train,
    y_train=y_train,
    x_test=X_test,
    y_test=y_test,
    batch_size=64,
    sparse_categorical=0,
    random_deep=[3, 3, 3],
    epochs=[10, 10, 10],
    plot=False,
    MAX_NB_WORDS = 20000
)

# End timer
end_time = time.perf_counter()

# Compute and print elapsed time
elapsed = end_time - start_time
print(f"[TIMING] Text_Classification call took {elapsed:.2f} seconds")