import json
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st


class sleep_data:
    def __init__(self, result_link):
        self.result_link = result_link
        self.data = None
        

    def load_data(self):
        self.data = pd.read_csv(self.result_link)
        return self.data
    
    def filter_data(self):
        if self.data is None:
            self.load_data
        
        

        self.data["heart_rate_filtered"] = self.data["heart_rate"].rolling(
            window=5,
            center=True
        ).mean()

        self.data["hrv_filtered"] = self.data["hrv"].rolling(
            window=5,
            center=True
        ).median()

        self.data["spo2_filtered"] = self.data["spo2"].rolling(
            window=5,
            center=True
        ).median()

        return self.data
