import pandas as pd
import os
from functools import reduce


FILES_PATH = os.path.join(os.getcwd(), "data-warehouse")

'''
Example:
rating = read_table("Rating.xlsx")
'''

def read_table(file_name):
    try:
        return pd.read_excel(os.path.join(FILES_PATH, file_name))
    except:
        # empty DF
        return pd.DataFrame()


