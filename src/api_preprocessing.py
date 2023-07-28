import numpy as np
import pandas as pd

from src.prep_data import *
from src.convert_data import *

def fix_columns(df):
    """ Fix column order to match the model expectations """
    column_order = ["type", "region", "province", "district", "localityType",
                    "bedroomCount", "netHabitableSurface", "condition", "epcScore", 
                    "bathroomCount", "showerRoomCount", "toiletCount", 
                    "hasLift", "fireplaceExists", "hasSwimmingPool", "hasAirConditioning", 
                    "hasGarden", "hasTerrace", "gardenSurface", "terraceSurface", "land"]
    df = df[column_order]
    return df


def process_property_data(property_data):
    """ This function processes user enetered data to ml format to run price prediction:
        Gets python dictionary and returns Pandas dataframe """
    df = pd.DataFrame(property_data, index=[0])
    df["localityType"] = df["postalCode"].apply(create_localityType)
    # fill nul values
    df = fill_null_values(df)
    # convert property type to 0/1 value
    df = fix_type(df)
    # map property condition to nymeric values on a scale
    df = map_condition(df)
    # map epc score to nymeric values on a scale
    df = map_epc(df)
    # fix column order
    df = fix_columns(df)

    return df

