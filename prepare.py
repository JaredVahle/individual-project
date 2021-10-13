import pandas as pd
import numpy as np
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def clean_salary_data(df):
    '''
    This function creates a dummy variable for title and concats it with the current dataframe,
    Drops columns that are not useful, or would make the dataset too large to use dummies on,
    Drops nulls, removes any rows that do not have education documented, renames some columns,
    for readability, and finally adds a column for highly experienced.
    '''
    dummy_df = pd.get_dummies(df[['title']])
    dummy_df.columns = [col.lower().replace(" ","_") for col in dummy_df]
    df = pd.concat([df, dummy_df], axis=1)
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
    'Race_Hispanic',
    'company',
    'level',
    'location',
    'tag',
    'title'],inplace = True)
    df.dropna(inplace = True)
    df = df[df.Highschool + df.Some_College + df.Bachelors_Degree + df.Masters_Degree + df.Doctorate_Degree > 0]
    df.rename(columns = {'Masters_Degree':'masters_degree',
                        'Bachelors_Degree':'bachelors_degree',
                        'Doctorate_Degree':'doctorate_degree',
                        'Highschool':'highschool',
                        'Some_College':'some_college',
                        'totalyearlycompensation':'total_earnings'},inplace = True)
    df['highly_experienced'] = df.yearsofexperience >= 4
    df['highly_experienced'] = df.highly_experienced.astype(int)
    return df

def explore_clean_salary_data(df):
    '''
    This function is for my exploration so that i can ask interesting questions about the data.
    '''
    dummy_df = pd.get_dummies(df[['gender']])
    dummy_df.columns = [col.lower().replace(" ","_") for col in dummy_df]
    df = pd.concat([df, dummy_df], axis=1)
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
                        'Some_College':'some_college',
                        'totalyearlycompensation':'total_earnings'},inplace = True)
    df.drop(columns = ['gender_title:_senior_software_engineer','gender_female'],inplace = True)
    df['highly_experienced'] = df.yearsofexperience >= 4
    df['highly_experienced'] = df.highly_experienced.astype(int)
    return df

def train_validate_test(df, target):
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=174)
    # split train/validate into train (60%) and validate (20%)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=174)
    # splits our target off of our train, validate, test
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test

def explore_train_validate_test(df, target):
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=174)
    # split train/validate into train (60%) and validate (20%)
    train, validate = train_test_split(train_validate, test_size=.25, random_state=174)
    return train, validate, test


def min_max_scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    Returns scaler, X_train_scaled, X_validate_scaled, X_test_scaled dfs 
    """
    scaler = MinMaxScaler().fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index, columns = X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled

def remove_outliers(df):
    '''
    This function will remove outliers of our target var in order to do better modeling
    '''
    new_df = df[(np.abs(stats.zscore(df['total_earnings'])) < 3)]
    return new_df