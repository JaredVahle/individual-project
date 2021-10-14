import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# modeling methods
from sklearn.metrics import mean_squared_error, explained_variance_score


def make_metric_df(y, y_pred, model_name, metric_df):
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
                'model': model_name, 
                'RMSE_validate': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_validate': explained_variance_score(
                    y,
                    y_pred)
            }])
        return metric_df
    else:
        return metric_df.append(
            {
                'model': model_name, 
                'RMSE_validate': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_validate': explained_variance_score(
                    y,
                    y_pred)
            }, ignore_index=True)


def make_metric_df_train(y, y_pred, model_name, metric_df):
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
                'model': model_name, 
                'RMSE_train': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_train': explained_variance_score(
                    y,
                    y_pred)
            }])
        return metric_df
    else:
        return metric_df.append(
            {
                'model': model_name, 
                'RMSE_train': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_train': explained_variance_score(
                    y,
                    y_pred)
            }, ignore_index=True)

def make_metric_df_test(y, y_pred, model_name, metric_df):
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
                'model': model_name, 
                'RMSE_test': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_test': explained_variance_score(
                    y,
                    y_pred)
            }])
        return metric_df
    else:
        return metric_df.append(
            {
                'model': model_name, 
                'RMSE_test': mean_squared_error(
                    y,
                    y_pred) ** .5,
                'r^2_test': explained_variance_score(
                    y,
                    y_pred)
            }, ignore_index=True)