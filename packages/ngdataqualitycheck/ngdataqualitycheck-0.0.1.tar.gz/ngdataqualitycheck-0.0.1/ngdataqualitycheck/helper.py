import os
from bs4 import UnicodeDammit
import pandas as pd
from datetime import datetime
from ngdataqualitycheck.global_params import *


# For loading data
def load_data(filename=None):
    """
    For loading data from multiple sources and
    creating a dataframe.

    :param filename: Name of the file to be loaded (with extension), defaults to None
    :type filename: str, optional
    :return: Dataframe with records found in the file.
    :rtype: pd.DataFrame
    """
    filetype = filename.split('.')[-1]
    try:
        # load csv
        if filetype == "csv":
            df = pd.read_csv(filename)
        # load json
        elif filetype == 'json':
            df = pd.read_json(filename)
        # load sql
        elif filetype == 'sql':
            df = pd.read_sql(filename)
        # load parquet
        elif filetype == 'parquet':
            df = pd.read_parquet(filename)
        # load excel
        elif filetype == 'excel':
            df = pd.read_excel(filename)
        # load xml
        elif filetype == 'xml':
            df = pd.read_xml(filename)
        # load hdf5
        elif filetype == 'hdf5':
            df = pd.read_hdf(filename)
        # load html
        elif filetype == 'html':
            df = pd.read_html(filename)
        return df
    except NameError as e:
        print(e)

# For obtaining current date and time
def get_datetime():
    """
    For obtaining the current date and time.

    :return: Current data nd time
    :rtype: datetime64
    """
    datenow = datetime.now().strftime(DATE_FORMAT)
    timenow = datetime.now().strftime(TIME_FORMAT)
    return datenow, timenow

# For getting file encoding format
def get_encoding(filename=None):
    """
    For obtaining the encoding of a given file

    :param filename: Name of the file, defaults to None
    :type filename: str, optional
    :return: Encoding value
    :rtype: str
    """
    with open(filename, 'rb') as file:
        content = file.read()
    suggestion = UnicodeDammit(content)
    encoding = suggestion.original_encoding
    return encoding

# For getting dataset information
def get_data_info(df=None):
    """
    For getting the data information from the dataframe

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Dataframe shape and dtypes
    :rtype: tuple, list
    """
    # fetching data shape
    df_shape = df.shape
    # fetching datatypes of columns
    typeslist = []
    i = 1
    for col in df:
        typeslist.append((i, col, df[col].dtypes.name))
        i += 1
    typeslist = tuple(items for items in typeslist)
    return df_shape, typeslist

# For getting  names of empty columns
def get_emptys(df=None):
    """
    For getting info on empty columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of empty columns, list of empty columns
    :rtype: int, list
    """
    emptys_list = []
    for col in df:
        if df[col].empty:
            emptys_list.append(col)
    emptys_count = len(emptys_list)
    return emptys_count, emptys_list

# For getting  names of columns with 0's
def get_zeros(df=None):
    """
    For getting info on zeros columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of zeros columns, list of zeros columns
    :rtype: int, list
    """
    zeros_list = []
    for col in df:
        if (df[col] == 0).sum() > 0:
            zeros_list.append(col)
    zeros_count = len(zeros_list)
    return zeros_count, zeros_list

# For getting  names of columns with negatives
def get_negatives(df=None):
    """
    For getting info on negatives columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of negatives columns, list of negatives columns
    :rtype: int, list
    """
    negatives_list = []
    for col in df:
        try:
            if (df[col] < 0).sum() > 0:
                negatives_list.append(col)
        except:
            pass
    negatives_count = len(negatives_list)
    return negatives_count, negatives_list

# For inspecting Duplicates
def check_duplicates(df=None):
    """
    For getting info on duplicate columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of duplicate columns, index and list of negatives columns
    :rtype: int, list
    """
    # checking for duplicate records
    num_dups = df.duplicated().sum()  # number of duplicates
    # list of duplicate rows
    dup_idx = list(df[df.duplicated(keep='first') == True].index)
    # list of duplicate columns
    dup_cols = []
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            if df.iloc[:, i] is df.iloc[:, j]:
                dup_cols.append((i, j))
    return num_dups, dup_idx, dup_cols

# For inspecting Missing values
def check_missing(df=None):
    """
    For getting info on missing columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of missing columns, list of missing columns
    :rtype: int, list
    """
    # checking for missing values
    num_miss = df.isnull().sum().max()  # number of rows with missing values
    miss_cols = df.columns[df.isnull().any()]
    return num_miss, miss_cols

# For inspecting Constant features
def check_constants(df=None):
    """
    For getting info on constants columns

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :return: Number of constants columns, list of constants columns
    :rtype: int, list
    """
    const_cols = [col for col in df.columns if df[col].nunique() == 1]
    num_const = len(const_cols)
    return num_const, const_cols

# For obtaining correlation of Numerical features
def get_correlation(df=None, thresh=0.5):
    """
    For getting feature correlation

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :param thresh: Correlation threshold, defaults to 0.5
    :type thresh: float, optional
    :return: List of tuples with features and their corresponding correlation
    :rtype: List of tuples
    """
    # getting numerical columns
    num_cols = [col for col in df.columns if df[col].dtype.name in NUMERIC_TYPES]
    # calculating Pearson's correlation
    corlist = []
    for i in range(len(num_cols)):
        for j in range(1, len(num_cols)):
            cor = df[[num_cols[i], num_cols[j]]].corr().values[0, 1]
            corlist.append((num_cols[i], num_cols[j], cor.round(2)))
    # getting the list of correlated variables
    final_list = []
    for item in corlist:
        for i in item:
            try:
                float(i)
                if abs(float(i)) > thresh and float(i) != 1:
                    final_list.append(item)
            except:
                False
    corlist = list(set(list((tuple(set(i)) for i in final_list))))
    return corlist

# Foe generating data quality warnings
def generate_warnings(df=None, txt_coldict=None, cat_coldict=None, num_coldict=None, time_coldict=None):
    """
    For generating warnings related to features within the given dataframe

    :param df: Dataframe, defaults to None
    :type df: pd.DataFrame, optional
    :param txt_coldict: Dictionary of text columns stats, defaults to None
    :type txt_coldict: dictionary, optional
    :param cat_coldict: Dictionary of categorical columns stats, defaults to None
    :type cat_coldict: dictionary, optional
    :param num_coldict: Dictionary of numerical columns stats, defaults to None
    :type num_coldict: dictionary, optional
    :param time_coldict: Dictionary of datetime columns stats, defaults to None
    :type time_coldict: dictionary, optional
    :return: Dictionary of warnings and related features
    :rtype: dictionary
    """
    # creating dictionary for storing warnings
    warn_dict = {}
    warn_dict['missing_values'] = []
    warn_dict['prim_for_key'] = []
    warn_dict['imbalance'] = []
    warn_dict['neg_mean'] = []
    warn_dict['left_skew'] = []
    warn_dict['right_skew'] = []
    warn_dict['outlier'] = []

    for col in df:
        # checking text data
        if col in txt_coldict.keys():
            src_dict = txt_coldict[col]
            # percentage missing values
            if src_dict['% Missing Values'] > PERCENT_MISSING_VAL:
                warn_dict['missing_values'].append(col)
            # whether primary key or not
            if (src_dict['Text max length'] < MAX_TEXT_LENGTH) and (df[col].nunique() > 0.9*df.shape[0]):
                warn_dict['prim_for_key'].append(col)

        # checking category data
        elif col in cat_coldict.keys():
            src_dict = cat_coldict[col]
            # percentage missing values
            if src_dict['% Missing Values'] > PERCENT_MISSING_VAL:
                warn_dict['missing_values'].append(col)
            # checking for imbalance
            if src_dict['Imbalance'] == 'True':
                warn_dict['imbalance'].append(col)

        # checking numerical data
        elif col in num_coldict.keys():
            src_dict = num_coldict[col]
            try:
                # percentage missing values
                if src_dict['% Missing Values'] > PERCENT_MISSING_VAL:
                    warn_dict['missing_values'].append(col)
                # checking negative mean
                if src_dict['Mean'] < 0:
                    warn_dict['neg_mean'].append(col)
                # checking skewness
                if src_dict['Skewness'] < SKEWNESS[0]:
                    warn_dict['left_skew'].append(col)
                elif src_dict['Skewness'] > SKEWNESS[1]:
                    warn_dict['right_skew'].append(col)
                # checking outliers
                if src_dict['% Outliers'] > PERCENT_OUTLIER_LIMIT:
                    warn_dict['outlier'].append(col)
            except:
                continue
        # checking datetime data
        elif col in time_coldict.keys():
            src_dict = time_coldict[col]
            # percentage missing values
            if src_dict['% Missing Values'] > PERCENT_MISSING_VAL:
                warn_dict['missing_values'].append(col)
    return warn_dict

