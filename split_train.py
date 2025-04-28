#First 1m rows of training dataset
# import pandas as pd

# INPUT_CSV   = r"D:\Project\RMDL\dataset\train.csv"
# OUTPUT_CSV  = r"D:\Project\RMDL\dataset\train_first_1m.csv"
# NROWS       = 1_000_000

# # Read only the header to know the column count, then skip it when writing:
# df = pd.read_csv(INPUT_CSV, nrows=NROWS, header=0)

# # Write out exactly those rows, no header, no index
# df.to_csv(OUTPUT_CSV, index=False, header=False)

# print(f"Wrote first {NROWS} rows to {OUTPUT_CSV}")


#First 100k rows of testing dataset
import pandas as pd

INPUT_CSV   = r"D:\Project\RMDL\dataset\test.csv"
OUTPUT_CSV  = r"D:\Project\RMDL\dataset\test_first_100k.csv"
NROWS       = 100_000

# Read only the first 100 000 rows (header=0 to consume the header row)
df = pd.read_csv(INPUT_CSV, nrows=NROWS, header=0)

# Write those rows without header or index
df.to_csv(OUTPUT_CSV, index=False, header=False)

print(f"Wrote first {NROWS} rows to {OUTPUT_CSV}")
