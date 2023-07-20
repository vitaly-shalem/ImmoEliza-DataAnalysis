import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.linear_model import LinearRegression
import xgboost as xgb

from src.manage_csv import load_csv_data


def scale_data(train, test):
    """ This function scales numeric data in train/test features """
    print("Scaling train/test data...")
    minMaxScaler = MinMaxScaler()
    train = minMaxScaler.fit_transform(train)
    test = minMaxScaler.transform(test)
    return train, test


def train_linear_regression(X_train, y_train, X_test, y_test):
    """ This function run Linear Regression model train and test """
    print("Training Linear regression model...")

    lreg = LinearRegression()
    lreg.fit(X_train, y_train)

    lreg_train = round(lreg.score(X_train, y_train) * 100, 2)
    lreg_test  = round(lreg.score(X_test, y_test) * 100, 2)

    print(f"  Linear regression results - TRAIN: {lreg_train}")
    print(f"  Linear regression results - TEST:  {lreg_test}")


def train_xgbooster_regressor(X_train, y_train, X_test, y_test):
    """ This function run XGBoost Regressor train and test """
    print("Training XGBoost Regressor model...")

    xgbreg = xgb.XGBRegressor()
    xgbreg.fit(X_train, y_train)

    xgbreg_train = round(xgbreg.score(X_train, y_train) * 100, 2)
    xgbreg_test  = round(xgbreg.score(X_test, y_test) * 100, 2)

    print(f"  XGBoost Regressor results - TRAIN: {xgbreg_train}")
    print(f"  XGBoost Regressor results - TEST:  {xgbreg_test}")


def train_models(train):
    """ 
    This functions...
        loads data,
        creates features and target variales,
        splits data to train and test, 
        scales features train and test,
        and runs train and test for 2 type of models"
            1. Linear regression
            2. XGBoost Regressor
    """

    # load csv data as dataframe
    df = load_csv_data(train, "ID")

    # create features X and target y variables
    X = df.drop("price", axis=1).to_numpy()
    y = df["price"].to_numpy()

    # split data to train and test 80/20
    print("Split data to train and test:")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    print("  Shape of X_train: ", X_train.shape)
    print("  Shape of X_test:  ", X_test.shape)
    print("  Shape of y_train: ", y_train.shape)
    print("  Shape of y_test:  ", y_test.shape)

    # scale nukeric data
    X_train, X_test = scale_data(X_train, X_test)

    # run linear regression train / test
    train_linear_regression(X_train, y_train, X_test, y_test)

    # run xgbooster regressor train / test
    train_xgbooster_regressor(X_train, y_train, X_test, y_test)
