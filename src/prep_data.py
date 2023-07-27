import numpy as np
import pandas as pd
import re

from src.handle_files import *

def subset_to_train_data(df, list):
    """ This function creates a subset of a DataFrame based on the list of required columns """
    return df[list]


def create_localityType(postalCode):
    """ This function converts a postal code to localityType, values are int 1 to 4 """
    localityType = 0
    # X000 & X00X > 1
    if re.match(r"^[1-9][0]{3}$", postalCode) or re.match(r"^[1-9][0]{2}[1-9]$", postalCode):
        localityType = 1
    # X0X0 & X0XX> 2
    elif re.match(r"^([1-9][0]){2}$", postalCode) or re.match(r"^[1-9][0][1-9]{2}$", postalCode):
        localityType = 2
    # XX00 & XX0X > 3
    elif re.match(r"^[1-9]{2}[0]{2}$", postalCode) or re.match(r"^[1-9]{2}[0][1-9]$", postalCode):
        localityType = 3
    # XXX0 & XXXX > 4
    elif re.match(r"^[1-9]{3}[0]$", postalCode) or re.match(r"^[1-9]{4}$", postalCode):
        localityType = 4
    return localityType


def fill_null_values(df):
    """ This function fills NA values for specific columns """
    # fill with UNKNOWN
    fill_with_unknown = ["condition", "epcScore"]
    for fwu in fill_with_unknown:
        df[fwu].fillna(value="UNKNOWN", inplace=True)
    # fill with 0
    fill_with_zero = ["bathroomCount", "toiletCount", "gardenSurface", "terraceSurface", "land"]
    for fwz in fill_with_zero:
        df[fwz].fillna(value=0, inplace=True)
    # convert boolean to 1/0 and fill with 0
    boolean_to_fix = ["hasLift", "hasGarden", "hasTerrace", "fireplaceExists", "hasSwimmingPool", "hasAirConditioning"]
    for btf in boolean_to_fix:
        df[btf].fillna(value=False, inplace=True)
        df[btf] = df[btf].apply(lambda x: 1 if x == True else 0)
    return df


def remove_outliers(df):
    """ This function maps some outlying vakues for specific columns """
    df.drop(df[df["bedroomCount"] > 12].index, inplace=True)
    df.loc[df["showerRoomCount"] < 1, "showerRoomCount"] = 0
    df.loc[df["showerRoomCount"] > 14, "showerRoomCount"] = 14
    df.loc[df["gardenSurface"] < 4, "gardenSurface"] = 0
    df.loc[df["gardenSurface"] > 1000, "gardenSurface"] = 1000
    df.loc[df["terraceSurface"] > 100, "terraceSurface"] = 100
    df.loc[df["land"] < 10, "land"] = 0
    df.loc[df["land"] > 50000, "land"] = 50000
    return df


def remove_lines_missing_data(df):
    """ This function drops rown where the critical values are NA """
    df.dropna(subset=['netHabitableSurface'], inplace=True)
    df.dropna(subset=['bedroomCount'], inplace=True)
    df.dropna(subset=['price'], inplace=True)
    return df


def remove_duplicates(df):
    """ This function removes duplicates from a given DataFrame """
    df.drop_duplicates(inplace=True)
    return df


def prepare_data(raw, prep):
    """ This function runs the data preparation pipeline """
    
    # load csv file to dataframe
    df = load_csv_data(raw, "ID")

    # drop duplicates
    df = remove_duplicates(df)

    # remove line with missing critical data
    df = remove_lines_missing_data(df)

    # remove/map outliers
    df = remove_outliers(df)

    # fill nul values
    df = fill_null_values(df)

    # subset to train data / "postalCode", 
    data_to_use = ["type", "region", "province", "district", "localityType", 
                   "bedroomCount", "netHabitableSurface", "condition", "epcScore", 
                   "bathroomCount", "showerRoomCount", "toiletCount", 
                   "hasLift", "fireplaceExists", "hasSwimmingPool", "hasAirConditioning", 
                   "hasGarden", "hasTerrace", "gardenSurface", "terraceSurface", "land", 
                   "price"]
    df = subset_to_train_data(df, data_to_use)

    print("The data has been prepared...")

    save_to_csv(prep, df)
