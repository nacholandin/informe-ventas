import streamlit as st
import numpy as np
import pandas as pd


PAGE_CONFIG = {"page_title"             : "Informe de ventas - Streamlit",  
                 "layout"                : "wide"}

def read_eda():
     df = pd.read_csv("source/tiendas.csv")
     return df