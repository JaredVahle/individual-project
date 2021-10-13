import pandas as pd
import numpy as np
from acquire import get_salary_data
from prepare import clean_salary_data, train_validate_test, min_max_scaler, explore_clean_salary_data,explore_train_validate_test

def wrangle_salary_data():
    df = get_salary_data()
    df = clean_salary_data(df)
    df.drop(columns = ['basesalary','stockgrantvalue','bonus','dmaid'],inplace = True)
    train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test(df,target = 'total_earnings')
    scaler, X_train_scaled, X_validate_scaled, X_test_scaled = min_max_scaler(X_train, X_validate, X_test)
    return df, train, validate, test, X_train, X_train_scaled , y_train, X_validate, X_validate_scaled , y_validate, X_test, X_test_scaled , y_test, scaler

def wrangle_explore_salary_data():
    df = get_salary_data()
    df = explore_clean_salary_data(df)
    train, validate, test = explore_train_validate_test(df,target = 'total_earnings')
    return df, train, validate, test