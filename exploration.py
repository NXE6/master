# TEMPLATE PYTHON FUNCTIONS FOR BASIC DATA EXPLORATION

# Import Standard Libraries

import numpy as np
import pandas as pd


# Called with filepath, reading data from example CSV file with NO headers, and return it as dataframe

def ReadFile(filepath):
  df = pd.read_csv(filepath, header="None")
  return df


# Called with dataframe, showing simple preview

def PreviewFile(df):
  df.head(10)
  df.tail(10)
  df.columns
  return


# Called with dataframe and filepath, writing data to CSV file

def WriteFile(df, filepath):
  df.to_csv(filepath)
  return


# Calling all functions

filepath = "gs://my_first_bucket_nxe6/Titanic"
ReadFile(filepath)
PreviewFile(df)
WriteFile(df, filepath)
