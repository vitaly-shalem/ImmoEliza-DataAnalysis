import numpy as np
import pandas as pd

from src.manage_csv import *


def fix_type(df):
    """ This function maps property type to numeric values:
        1 for HOUSE, 0 for APARTMENT """
    df["typeNum"] = df["type"].apply(lambda x: 1 if x == "HOUSE" else 0)
    return df


def map_condition(df):
    """ This function maps property condition to numerical values:
        1 to 6 scale, 0 for unknown """
    df["conditionNum"] = None
    df.loc[df["condition"] == "AS_NEW", "conditionNum"] = 1
    df.loc[df["condition"] == "JUST_RENOVATED", "conditionNum"] = 2
    df.loc[df["condition"] == "GOOD", "conditionNum"] = 3
    df.loc[df["condition"] == "TO_BE_DONE_UP", "conditionNum"] = 4
    df.loc[df["condition"] == "TO_RENOVATE", "conditionNum"] = 5
    df.loc[df["condition"] == "TO_RESTORE", "conditionNum"] = 6
    df.loc[df["condition"] == "UNKNOWN", "conditionNum"] = 0
    return df


def map_epc(df):
    """ This function maps EPC scores to numerical values:
        A to G scale to 1 to 7 scale, 0 for unknown """
    df["epcScoreNum"] = None
    df.loc[df["epcScore"] == "A", "epcScoreNum"] = 1
    df.loc[df["epcScore"] == "B", "epcScoreNum"] = 2
    df.loc[df["epcScore"] == "C", "epcScoreNum"] = 3
    df.loc[df["epcScore"] == "D", "epcScoreNum"] = 4
    df.loc[df["epcScore"] == "E", "epcScoreNum"] = 5
    df.loc[df["epcScore"] == "F", "epcScoreNum"] = 6
    df.loc[df["epcScore"] == "G", "epcScoreNum"] = 7
    df.loc[df["epcScore"] == "UNKNOWN", "epcScoreNum"] = 0
    return df


def subset_data(df):
    """ This function creates a new dataframe, 
        a subset of the main, with the data to be used in training """
    subset = ["typeNum", 
              "netHabitableSurface", "bedroomCount",
              "bathroomCount", "showerRoomCount", "toiletCount", 
              "conditionNum", "epcScoreNum",
              "hasLift", "fireplaceExists", "hasSwimmingPool", "hasAirConditioning", 
              "hasGarden", "hasTerrace",
              "gardenSurface", "terraceSurface", "land",
              "price"]
    df = df[subset]
    return df


def get_col_dummies(df, column):
    """ This function creates dummies dataframe for required column """
    dummies = pd.get_dummies(df[column], prefix=column, prefix_sep="_", dtype=float)
    return dummies


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

    # create a new dataframe with the data to be used in training
    df_mapped = subset_data(df)

    # create dummies for categorical values and merge
    #   - region
    df_mapped = df_mapped.merge(get_col_dummies(df, "region"), on="ID")
    #   - province
    df_mapped = df_mapped.merge(get_col_dummies(df, "province"), on="ID")
    #   - district
    df_mapped = df_mapped.merge(get_col_dummies(df, "district"), on="ID")
    #   - localityType (derived from postalCode)
    df_mapped = df_mapped.merge(get_col_dummies(df, "localityType"), on="ID")

    print("The train data has been prepared...")
    
    # save to csv file
    save_to_csv(train, df_mapped)
