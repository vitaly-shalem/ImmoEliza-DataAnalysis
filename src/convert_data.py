import numpy as np
import pandas as pd

from src.handle_files import *


def fix_type(df):
    """ This function maps property type to numeric values:
        1 for HOUSE, 0 for APARTMENT """
    df["type"] = df["type"].apply(lambda x: 1 if x == "HOUSE" else 0)
    return df


def map_condition(df):
    """ This function maps property condition to numerical values:
        1 to 6 scale, 0 for unknown """
    df.loc[df["condition"] == "NEW", "condition"] = 1
    df.loc[df["condition"] == "AS_NEW", "condition"] = 1
    df.loc[df["condition"] == "JUST_RENOVATED", "condition"] = 2
    df.loc[df["condition"] == "GOOD", "condition"] = 3
    df.loc[df["condition"] == "TO_BE_DONE_UP", "condition"] = 4
    df.loc[df["condition"] == "TO_RENOVATE", "condition"] = 5
    df.loc[df["condition"] == "TO_RESTORE", "condition"] = 6
    df.loc[df["condition"] == "UNKNOWN", "condition"] = 0
    return df


def map_epc(df):
    """ This function maps EPC scores to numerical values:
        A to G scale to 1 to 7 scale, 0 for unknown """
    df.loc[df["epcScore"] == "A", "epcScore"] = 1
    df.loc[df["epcScore"] == "B", "epcScore"] = 2
    df.loc[df["epcScore"] == "C", "epcScore"] = 3
    df.loc[df["epcScore"] == "D", "epcScore"] = 4
    df.loc[df["epcScore"] == "E", "epcScore"] = 5
    df.loc[df["epcScore"] == "F", "epcScore"] = 6
    df.loc[df["epcScore"] == "G", "epcScore"] = 7
    df.loc[df["epcScore"] == "UNKNOWN", "epcScore"] = 0
    return df


def convert_data(prep, train):
    """ This function runs the pipeline of data mapping for ML training """
    # load csv data
    df = load_csv_data(prep, "ID")

    # fix some data
    #   - convert property type to 0/1 value
    df = fix_type(df)
    #   - map property condition to nymeric values on a scale
    df = map_condition(df)
    #   - map epc score to nymeric values on a scale
    df = map_epc(df)
    
    print("The train data has been prepared...")
    
    # save to csv file
    save_to_csv(train, df)
