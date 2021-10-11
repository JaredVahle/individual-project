import pandas as pd
import numpy as np
from acquire import get_salery_data
from prepare import clean_salery_data

def wrangle_salery_data():
    df = get_salery_data()
    df = clean_salary_data()
    return df