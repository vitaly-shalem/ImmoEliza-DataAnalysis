import pandas as pd

def load_csv_data(path_to_file, index):
    """ This function loads csv file to DataFrame """
    df = pd.read_csv(path_to_file, index_col=index)
    return df


def save_to_csv(path_to_file, df):
    """ This function saves DataFrame to csv file """
    df.to_csv(path_to_file, index=True)
    print("Data saved to csv file...")
