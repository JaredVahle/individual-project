import pandas as pd
import numpy as np

def get_salary_data():
    df = pd.read_csv('Levels_Fyi_Salary_Data.csv')
    return df