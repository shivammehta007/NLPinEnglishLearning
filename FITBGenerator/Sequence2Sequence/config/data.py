"""
Configuration for Datasets
"""
import os


RAW_DATASET_FILENAME = "GrammarDataset.csv"
DATASET_FOLDER = "data"
RAW_DATASET_FOLDER = "raw"
PROCESSED_DATASET_FOLDER = "processed"
PROCESSED_DATASET_TRAIN_FILENAME = "train"
PROCESSED_DATASET_VALID_FILENAME = "valid"
PROCESSED_DATASET_TEST_FILENAME = "test"
FAIRSEQ_PREPROCESSED_DATASET = os.path.join(DATASET_FOLDER, "fairseq_binaries")
RAW_DATASET = os.path.join(DATASET_FOLDER, RAW_DATASET_FOLDER, RAW_DATASET_FILENAME)
PROCESSED_DATASET = {
    "train": os.path.join(
        DATASET_FOLDER, PROCESSED_DATASET_FOLDER, PROCESSED_DATASET_TRAIN_FILENAME
    ),
    "valid": os.path.join(
        DATASET_FOLDER, PROCESSED_DATASET_FOLDER, PROCESSED_DATASET_VALID_FILENAME
    ),
    "test": os.path.join(
        DATASET_FOLDER, PROCESSED_DATASET_FOLDER, PROCESSED_DATASET_TEST_FILENAME
    ),
}

TEMP_DIR = ".temp"
