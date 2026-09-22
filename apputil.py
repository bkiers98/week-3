import seaborn as sns
import pandas as pd


# update/add code below ...
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


def to_binary(i):
    '''
    Given an integer, this function will return its binary representation.
    '''
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return int(str(to_binary(i // 2)) + str(i%2))


def task_1():
    bellevue_cols = []

    #replace '?' gender with NaN
    df_bellevue.loc[:, ['gender']] = df_bellevue['gender'].replace('?', np.nan)

    for col in df_bellevue:
        bellevue_cols.append((col, df_bellevue[col].isna().sum()))
    bellevue_cols.sort(key=lambda x: x[1])
    bellevue_cols_sorted = [col[0] for col in bellevue_cols]
    print(bellevue_cols_sorted)
    