import pandas as pd
import numpy as np
from acquire import get_salery_data

def clean_salary_data(df):
    df.drop(columns = ['timestamp',
    'Race',
    'Education',
    'otherdetails',
    'gender',
    'rowNumber',
    'Race_Asian',
    'Race_White',
    'Race_Two_Or_More',
    'Race_Black',
    'Race_Hispanic'],inplace = True)
    df.dropna(inplace = True)
    df = df[df.Highschool + df.Some_College + df.Bachelors_Degree + df.Masters_Degree + df.Doctorate_Degree > 0]
    df.rename(columns = {'Masters_Degree':'masters_degree',
                        'Bachelors_Degree':'bachelors_degree',
                        'Doctorate_Degree':'doctorate_degree',
                        'Highschool':'highschool',
                         'Some_College':'some_college'},inplace = True)
    df['highly_experenced'] = df.yearsofexperience >= 4
    return df