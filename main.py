from pathlib import Path

import pandas as pd

from src.manage_csv import *
from src.prep_data import prepare_data
from src.convert_data import convert_data
from src.train_model import train_models


def main():
    """ This is the main function to run the main pipeline
            1. Data preparation
            2. Data conversion for ML training
            3. Model training
    """
    # files to save data
    raw_data = Path.cwd() / "data" / "02_cleanData_properties_data.csv"
    prep_data = Path.cwd() / "data" / "04_ml_prep_data_drop_duplicate.csv"
    train_data = Path.cwd() / "data" / "05_ml_data.csv"
    # prepare data
    prepare_data(raw_data, prep_data)
    # convert data
    convert_data(prep_data, train_data)
    # train models
    train_models(train_data)

if __name__ == '__main__':
    main()
