import pandas as pd
import joblib


def load_csv_data(path_to_file, index):
    """ This function loads csv file to DataFrame """
    df = pd.read_csv(path_to_file, index_col=index)
    return df


def save_to_csv(path_to_file, df):
    """ This function saves DataFrame to csv file """
    df.to_csv(path_to_file, index=True)
    # print message
    print("Data saved to csv file...")


def save_ml_files(model, path_file):
    """ This function saves ML related data [models, scaler, transformer] to *.dat files """
    # save file
    joblib.dump(model, path_file)

    # extract folder and file name
    split_char = "\\" if str(path_file).find("\\") != -1 else "/"
    folder = str(path_file).split(split_char)[-2]
    file_name = str(path_file).split(split_char)[-1]
    
    # print message
    print(f"  to ./{folder}/{file_name}")
