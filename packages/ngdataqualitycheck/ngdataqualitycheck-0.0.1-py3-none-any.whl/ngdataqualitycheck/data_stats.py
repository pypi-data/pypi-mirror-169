import numpy as np
import pandas as pd

from ngdataqualitycheck.global_params import *


# Text columns stats
def get_text_stats(df=None):
    """
    For getting statistics of text features

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: List of text features and dictionary of text feature statistics
    :rtype: list, dictionary
    """
    # Extracting features with type 'object'
    obj_cols = [col for col in df.columns if df[col].dtype.name == 'object']
    for col in obj_cols:
        df1 = df.copy()
        # Extracting numerical features
        try:
            df[col] = df[col].astype('float')
        except:
            # Extracting datetime features
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                continue

    # Extracting features with type 'object'
    obj_cols = [col for col in df.columns if df[col].dtype.name == 'object']
    for col in obj_cols:
        # Extracting categorical features
        df1 = df.copy()
        if (df1[col].nunique() < 20):
            df[col] = df[col].astype('category')

    # Extracting columns with type 'object'
    obj_cols = [col for col in df.columns if df[col].dtype.name == 'object']

    # Obtaining and storing the parameters of text features
    txt_coldict = {}
    for col in obj_cols:
        coldict = {}
        coldict['Name'] = col
        coldict['Datatype'] = df[col].dtypes.name
        coldict['Count'] = df[col].count()
        coldict['Total Zeros'] = (df[col] == 0).sum()
        coldict['Total Missing Values'] = df[col].isnull().sum()
        coldict['% Missing Values'] = np.round(100*df[col].isnull().mean(), 2)
        coldict['Total Unique Values'] = df[col].nunique()
        # Finding text length
        len_list = []
        for i in range(df.shape[0]):
            len_list.append(len(str(df.loc[i, col])))
        len_list = list(set(len_list))
        if 3 in len_list:
            len_list.remove(3)
        len_list = max(len_list)
        coldict['Text max length'] = len_list
        txt_coldict[col] = coldict
    return df, obj_cols, txt_coldict


def get_num_stats(df=None):
    """
    For getting statistics of numerical features

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: List of numerical features and dictionary of numerical feature statistics
    :rtype: list, dictionary
    """
    # Extracting numerical features
    num_cols = [col for col in df if df[col].dtype.name in NUMERIC_TYPES]
    continuous_cols = []
    discrete_cols = []

    # Obtaining and storing the parameters of numerical features
    num_coldict = {}
    for col in num_cols:
        find_mode = False
        coldict = {}
        coldict['Name'] = col
        coldict['Datatype'] = df[col].dtypes.name
        # getting the type of numerical features
        if (df[col].nunique() < 20) and (df[col].isnull().mean() < 0.5):
            coldict['Type'] = 'Discrete'
            # separating boolean features
            if df[col].nunique() == 2:
                df1 = df.copy()
                df1[col] = df1[col].astype('bool')
                coldict['Datatype'] = df1[col].dtypes.name
            discrete_cols.append(col)
            find_mode = True
        elif (df[col].nunique() > 20) and (df[col].isnull().mean() < 0.5):
            coldict['Type'] = 'Continuous'
            continuous_cols.append(col)
        else:
            coldict['Type'] = 'Unable to identify.'

        coldict['Count'] = df[col].count()
        coldict['Zeros'] = (df[col] == 0).sum()
        coldict['Negatives'] = (df[col] < 0).sum()
        coldict['Missing Values'] = df[col].isnull().sum()
        coldict['% Missing Values'] = np.round(100*df[col].isnull().mean(), 2)
        coldict['Unique Values'] = df[col].nunique()
        coldict['Minimum'] = np.round(df[col].min(), 2)
        coldict['Maximum'] = np.round(df[col].max(), 2)
        coldict['Mean'] = np.round(df[col].mean(), 2)
        coldict['Median'] = np.round(df[col].median(), 2)

        if find_mode:
            # getting class composition of discrete variable
            cat_comp = dict(
                np.round((100*df[col].value_counts()/df[col].shape[0]), 2))
            coldict['% Class Distribution'] = cat_comp
            first = list(cat_comp.keys())[0]
            second = list(cat_comp.keys())[1]
            diff = cat_comp[first]-cat_comp[second]
            if (cat_comp[first]) > 60:
                coldict['Imbalance'] = 'True'
            elif (diff) > 25:
                coldict['Imbalance'] = 'True'
            else:
                coldict['Imbalance'] = 'False'
            # getting mode for discrete variables
            coldict['Mode'] = df[col].mode().values[0]
        elif (not find_mode) and (df[col].nunique() > 2):
            # getting stats for continuous variables
            coldict['Standard Deviation'] = np.round(df[col].std(), 2)
            coldict['Mean Absolute Deviation'] = np.round(df[col].mad(), 2)
            coldict['Skewness'] = np.round(df[col].skew(), 2)
            coldict['Kurtosis'] = np.round(df[col].kurtosis(), 2)
            coldict['Quantiles'] = {
                '25th': np.round(df[col].quantile(0.25), 2),
                '50th': np.round(df[col].quantile(0.5), 2),
                '75th': np.round(df[col].quantile(0.75), 2),
                '95th': np.round(df[col].quantile(0.95), 2),
                '99th': np.round(df[col].quantile(0.99), 2)}
            # finding outliers
            if abs(df[col].skew()) > 0.7:
                # Applying IQR for identifying outliers for skewed features
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1
                upper = q3+(1.5*iqr)
                lower = q1-(1.5*iqr)
                outlier_count = np.sum(df[col] > upper)+np.sum(df[col] < lower)
            else:
                # Applying 3 std deviations for normally distributed features
                col_mean = np.mean(df[col])
                col_stdev = np.std(df[col])
                upper = col_mean+(3*col_stdev)
                lower = col_mean-(3*col_stdev)
                outlier_count = np.sum(df[col] > upper)+np.sum(df[col] < lower)

            coldict['% Outliers'] = np.round(
                (100*outlier_count/df.shape[0]), 2)
            coldict['Outlier Cutoffs'] = [
                np.round(lower, 2), np.round(upper, 2)]
        num_coldict[col] = coldict
    return df, num_cols, discrete_cols, continuous_cols, num_coldict


def get_cat_stats(df):
    """
    For getting statistics of categorical features

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: List of categorical features and dictionary of categorical feature statistics
    :rtype: list, dictionary
    """
    # Extracting categorical features
    cat_cols = [
        col for col in df if df[col].dtype.name in CATEGORY_TYPES]
    # Obtaining and storing the parameters of categorical features
    cat_coldict = {}
    for col in cat_cols:
        coldict = {}
        coldict['Name'] = col
        coldict['Datatype'] = df[col].dtypes.name
        coldict['Count'] = df[col].count()
        coldict['Zeros'] = (df[col] == 0).sum()
        coldict['Missing Values'] = df[col].isnull().sum()
        coldict['% Missing Values'] = np.round(100*df[col].isnull().mean(), 2)
        coldict['Unique Values'] = df[col].nunique()
        coldict['Mode'] = df[col].mode().values[0]

        cat_comp = dict(
            np.round((100*df[col].value_counts()/df[col].shape[0]), 2))

        coldict['% Class Distribution'] = cat_comp

        first = list(cat_comp.keys())[0]
        second = list(cat_comp.keys())[1]
        diff = cat_comp[first]-cat_comp[second]

        if (cat_comp[first]) > 60:
            coldict['Imbalance'] = 'True'
        elif (diff) > 25:
            coldict['Imbalance'] = 'True'
        else:
            coldict['Imbalance'] = 'False'
        cat_coldict[col] = coldict
    return df, cat_cols, cat_coldict


def get_time_stats(df):
    """
    For getting statistics of datetime features

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: List of datetime features and dictionary of datetime feature statistics
    :rtype: list, dictionary
    """
    time_cols = [
        col for col in df if df[col].dtype.name in DATETIME_TYPES]
    time_coldict = {}
    for col in time_cols:
        coldict = {}
        coldict['Name'] = col
        coldict['Datatype'] = df[col].dtypes.name
        coldict['Count'] = df[col].count()
        coldict['Zeros'] = (df[col] == 0).sum()
        coldict['Missing Values'] = df[col].isnull().sum()
        coldict['% Missing Values'] = np.round(100*df[col].isnull().mean(), 2)
        coldict['Unique Values'] = df[col].nunique()
        coldict['First timestamp'] = df[col].min()
        coldict['Latest timestamp'] = df[col].max()

        # calculating time step
        timestep_list = []
        for i in range(1, df.shape[0]):
            if df[col][i] != 'NaT' and df[col][i-1] != 'NaT':
                timestep = df[col][i] - df[col][i-1]
                timestep_list.append(timestep)

        # finding whether the data is uniform
        uniformity = False
        timestep_list = list(set(timestep_list))
        if len(timestep_list) == 1:
            uniformity = True
        coldict['Uniform data'] = uniformity
        if uniformity:
            coldict['Timestep'] = timestep_list[0]
        else:
            coldict['Timesteps'] = len(timestep_list)
        time_coldict[col] = coldict
    return df, time_cols, time_coldict
