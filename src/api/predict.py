import numpy as np
import pandas as pd
import joblib


def predict_price(df, paths):
    """ Predict the price of the property submitted by the user:
        - Gets dataframe with property information and paths to the model and other relevant data
        - Loads model, column transformer, minmax scaler
        - Adjusts the data with transformer and scaler
        - Runs prediction
        - Adjusts prediction rounding to thousands
        Returns price """
    price = None

    transformer = joblib.load(paths["transformer"])
    scaler = joblib.load(paths["scaler"])
    model = joblib.load(paths["model"])
    
    X_predict = df.to_numpy()
    X_predict = transformer.transform(X_predict)
    X_predict = scaler.transform(X_predict)

    prediction = (model.predict(X_predict)).tolist()
    price = round(prediction[0]/1000)*1000

    return price