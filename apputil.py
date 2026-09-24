import seaborn as sns
import pandas as pd
import numpy as np


# update/add code below ...
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# replace '?', 'h', 'g' genders with NaN
df_bellevue.loc[:, ['gender']] = df_bellevue['gender'] \
            .replace(['?', 'h', 'g'], np.nan)

def fibonacci(n):
    '''
    Given n, this function will return the nth number of the Fibonacci Series.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def to_binary(number):
    '''
    Given an integer, this function will return its binary representation.
    '''
    if number == 0:
        return '0'
    elif number == 1:
        return '1'
    else:
        return str(to_binary(number // 2)) + str(number%2)


def task_1():
    '''
    Returns a list of all column names, sorted in order from least missing
    values to most missing values.
    '''
    bellevue_cols = []

    for col in df_bellevue:
        bellevue_cols.append((col, df_bellevue[col].isna().sum()))

    bellevue_cols.sort(key=lambda column_pair: column_pair[1])
    bellevue_cols_sorted = [col[0] for col in bellevue_cols]

    return bellevue_cols_sorted


def task_2():
    '''
    Returns a data frame with two columns ('year' and 'total_admissions'),
    describing the amount of admissions for each year in the dataset.
    '''
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in']).dt.year
    df_year_admins = df_bellevue['year'].value_counts() \
                                        .reset_index(name='total_admissions') \
                                        .sort_values('year') \
                                        .reset_index(drop=True)
    return df_year_admins


def task_3():
    '''
    Returns a series with 'gender' as the index, and the average age for
    each gender as the value.
    '''
    df_gender_mean_age = df_bellevue.groupby('gender') \
                                    [['age']].mean()
    return df_gender_mean_age['age']


def task_4():
    '''
    Returns a list of the 5 most common professions in order of prevalence.
    '''
    professions = df_bellevue['profession'].value_counts() \
                                            .sort_values(ascending=False) \
                                            .index[:5] \
                                            .to_list()

    return professions
