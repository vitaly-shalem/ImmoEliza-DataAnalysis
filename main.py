from pathlib import Path

import pandas as pd

from src.handle_files import save_ml_files
from src.prep_data import prepare_data
from src.convert_data import convert_data
from src.train_model import train_models


def main():
    """ This is the main function to run the main pipeline
            1. Data preparation
            2. Data conversion for ML training
            3. Model training
    """

    # files to load / save data
    raw_data = Path.cwd() / "data" / "02_cleanData_properties_data.csv"
    prep_data = Path.cwd() / "data" / "04_ml_prep_data_drop_duplicate.csv"
    train_data = Path.cwd() / "data" / "05_ml_data.csv"

    # prepare data
    prepare_data(raw_data, prep_data)

    # convert data
    convert_data(prep_data, train_data)

    # train models
    transformer, scaler, lreg_model, xgbreg_model = train_models(train_data)

    # paths to save ml files
    transformer_path = Path.cwd() / "models" / "transformer.dat"
    scaler_path = Path.cwd() / "models" / "scaler.dat"
    lreg_model_path = Path.cwd() / "models" / "lreg_model.dat"
    xgbreg_model_path = Path.cwd() / "models" / "xgbreg_model.dat"

    # save ml files
    print("Saving ML data...")
    save_ml_files(transformer, transformer_path)
    save_ml_files(scaler, scaler_path)
    save_ml_files(lreg_model, lreg_model_path)
    save_ml_files(xgbreg_model, xgbreg_model_path)

if __name__ == '__main__':
    main()
