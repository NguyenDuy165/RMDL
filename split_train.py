import csv
import random
import argparse
import os

def reservoir_sample(input_csv, output_csv, sample_size, has_header=True):
    """
    Performs reservoir sampling on a CSV to extract `sample_size` random rows.
    Writes them (with header, if present) to `output_csv`.
    """
    reservoir = []
    with open(input_csv, newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader) if has_header else None

        for i, row in enumerate(reader, start=1):
            if i <= sample_size:
                reservoir.append(row)
            else:
                j = random.randrange(i)
                if j < sample_size:
                    reservoir[j] = row

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        if has_header:
            writer.writerow(header)
        writer.writerows(reservoir)
    print(f"Wrote {sample_size} rows to {output_csv}")

def make_output_path(input_csv, out_dir, sample_size, has_header, no_override):
    """
    Generate output filename: <basename>_sample_<size><_noheader?>.csv
    e.g. train.csv -> train_sample_10000.csv
    """
    base, ext = os.path.splitext(os.path.basename(input_csv))
    suffix = f"_sample_{sample_size}"
    if no_override:
        suffix += "_noheader"
    filename = base + suffix + ext
    return os.path.join(out_dir, filename)

def main():
    parser = argparse.ArgumentParser(description="Reservoir-sample CSV files.")
    parser.add_argument("--train-csv",
                        default=r"D:\Project\RMDL\dataset\preprocessed_train.csv",
                        help="Path to the full train CSV")
    parser.add_argument("--test-csv",
                        default=r"D:\Project\RMDL\dataset\preprocessed_test.csv",
                        help="Path to the full test CSV")
    parser.add_argument("--out-dir",
                        default=r"D:\Project\RMDL\dataset",
                        help="Directory to write sample files into")
    parser.add_argument("--train-size",
                        type=int,
                        default=10000,
                        help="Number of rows to sample from train CSV")
    parser.add_argument("--test-size",
                        type=int,
                        default=1000,
                        help="Number of rows to sample from test CSV")
    parser.add_argument("--no-header",
                        action="store_true",
                        help="If set, assumes CSVs have no header and will not write one")

    args = parser.parse_args()

    # compute output paths
    train_out = make_output_path(args.train_csv, args.out_dir, args.train_size, not args.no_header, args.no_header)
    test_out  = make_output_path(args.test_csv,  args.out_dir, args.test_size,  not args.no_header, args.no_header)

    reservoir_sample(
        input_csv   = args.train_csv,
        output_csv  = train_out,
        sample_size = args.train_size,
        has_header  = not args.no_header
    )
    reservoir_sample(
        input_csv   = args.test_csv,
        output_csv  = test_out,
        sample_size = args.test_size,
        has_header  = not args.no_header
    )

if __name__ == "__main__":
    main()
