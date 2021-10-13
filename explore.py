import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import sklearn.feature_selection

def salary_heatmap(df,target = 'total_earnings'):
    '''
    returns a heatmap and correlation for our target of salary
    '''
    plt.figure(figsize = (8,12))
    heatmap = sns.heatmap(df.corr()[[target]].sort_values(by=target, ascending=False), vmin = -.5, vmax = .5, annot = True, cmap = 'rocket')
    heatmap.set_title(f"Features Correlating with {target}")
    
    return heatmap

def plot_categorical_and_continuous_vars(df,categorical,continuous):
    '''
    Prints out multiple plots for both categorical and continuous variables,
    This can take in a list for both categorical and continues along with a dataframe
    and will create a boxplot, swarm plot, and a barplot
    '''
    for cont_col in continuous:
        for cat in categorical:
            categorical_label = cat
            continuous_label = cont_col
            
            fig, axes = plt.subplots(figsize=(12,36), nrows=4,ncols=1)
            fig.suptitle(f'{continuous_label} by {categorical_label}', fontsize=18, y=1.02)
            sns.lineplot(ax=axes[0], x=cat, y=cont_col, data=df)
            axes[0].set_title('Line Plot', fontsize=14)
            axes[0].set_xlabel(categorical_label, fontsize=12)
            axes[0].set_ylabel(continuous_label, fontsize=12)
            
            sns.boxplot(ax=axes[1], x=cat, y=cont_col, data=df,\
                        color='blue')
            axes[1].set_title('Box-and-Whiskers Plot', fontsize=14)
            axes[1].set_xlabel(categorical_label, fontsize=12)
            axes[1].set_ylabel(continuous_label, fontsize=12)
            
            sns.swarmplot(ax=axes[2], x=cat, y=cont_col, data=df,\
                        palette='Blues')
            axes[2].set_title('Swarm Plot', fontsize=14)
            axes[2].set_xlabel(categorical_label, fontsize=12)
            axes[2].set_ylabel(continuous_label, fontsize=12)
            
            sns.barplot(ax=axes[3], x=cat, y=cont_col, data=df,\
                        palette='Purples')
            axes[3].set_title('Bar Plot', fontsize=14)
            axes[3].set_xlabel(categorical_label, fontsize=12)
            axes[3].set_ylabel(continuous_label, fontsize=12)
            
            plt.tight_layout()
            
            plt.show()

def corr_two_vars(df,x,y):
    r, p = stats.pearsonr(df[x],df[y])
    print(f"p-value:{round(p,5)}")
    print(f"R: {round(r,4)}")
    scatter_plot = df.plot.scatter(x,y)
    scatter_plot.figure.set_dpi(300)
    plt.title(f"{x}'s relationship with {y}")
    if p < .05:
        print("This correlation is statistically significant")

    return r,p

def plot_hist(df,col_list):
    '''
    Plots a histogram and uses .describe for the columns in col list.
    '''
    for col in col_list:
        print(col)
        print(df[col].describe())
        print("--------------------------")
        plt.rcParams['font.size'] = '16'
        hist = df[col].hist(figsize = (12,8), grid = True)
        hist.plot()
        plt.title(f'Distribution of {col}')
        plt.show()

def multivar_scatter(df,x,y,hue):
    plt.rcParams['font.size'] = '16'
    