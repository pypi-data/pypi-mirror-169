import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import missingno as msno
from ngdataqualitycheck.global_params import *
from ngdataqualitycheck.helper import *
from ngdataqualitycheck.make_directory import MakeDirectory


# Creating directory to store plots
md = MakeDirectory(
    dir_structure=generate_directory['dir_structure'],
    basefolder=generate_directory['basefolder'])

plot_folder = md.create_directory(foldername='plots')

# For plotting wordcloud
def plot_wordcloud(
        df,
        col,
        name_of_file,
        timenow,
        width=WORDCLOUD_PARAMS['width'],
        height=WORDCLOUD_PARAMS['height'],
        color=WORDCLOUD_PARAMS['color'],
        facecolor=WORDCLOUD_PARAMS['facecolor'],
        figsize=WORDCLOUD_PARAMS['figsize'],
        fontsize=WORDCLOUD_PARAMS['fontsize']):
    """
    For generating wordcloud

    :param df: DataFrame
    :type df: pd.DataFrame
    :param col: Feature column
    :type col: str
    :param name_of_file: File name
    :type name_of_file: str
    :param timenow: Current time
    :type timenow: datetime
    :param width: Plot width
    :type width: int, optional
    :param height: Plot height
    :type height: int, optional
    :param color: Plot color
    :type color: str, optional
    :param facecolor: Plot facecolor
    :type facecolor: str, optional
    :param figsize: Plot figure size
    :type figsize: tuple, optional
    :param fontsize: Plot fontsize
    :type fontsize: int, optional
    :return: Plot name
    :rtype: str
    """
    # Preparing data for generating wordcloud
    checklist = ['Name:', 'Length:', 'dtype:']
    wordslist = str(df[col]).split()

    for word in wordslist:
        if word in checklist:
            wordslist.remove(word)

    wordslist.remove('object')
    wordslist.remove(f"{col},")
    
    text_to_plot = " ".join(wordslist)
    
    # Generating wordcloud
    wordcloud = WordCloud(width=width, 
                          height=height, 
                          background_color=color, 
                          min_font_size=fontsize).generate_from_text(text_to_plot)

    # Plot the WordCloud image
    plt.figure(figsize=figsize, facecolor=facecolor)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout()

    # Saving plot
    plotname = f'{plot_folder}\\{name_of_file}_{col}_{timenow}.png'
    plt.savefig(plotname)


# For plotting wordclouds of text features
def plot_text(df, name_of_file, text_cols_list, timenow):
    """
    For plotting text data using wordcloud

    :param df: Dataframe
    :type df: pd.DataFrame
    :param name_of_file: File name
    :type name_of_file: str
    :param text_cols_list: List of text features
    :type text_cols_list: list
    :param timenow: Current time
    :type timenow: datetime
    :return: Wordcloud
    :rtype: image
    """
    # Creating a copy of dataframe
    df_copy = df.copy()
    for col in df_copy.columns:
        df_copy[col] = df_copy[col].astype('str')
    # Defining stopwords
    stop_words = set(stopwords.words('english'))

    # Function for detokenizing text
    def detokenize(tokenised_text):
        """
        For detokenizing text

        :param tokenised_text: List of tokenized text
        :type tokenised_text: list
        :return: Detokenized text
        :rtype: str
        """
        detokenised_text = " ".join(tokenised_text)
        return detokenised_text
    
    # Generating wordcloud
    for col in text_cols_list:
        # Tokenizing
        df_copy[col] = df_copy[col].apply(word_tokenize)
        # Stopword removal
        df_copy[col] = df_copy[col].apply(
            lambda x: [word for word in x if word not in stop_words])
        # Detokenizing
        df_copy[col] = df_copy[col].apply(lambda x: detokenize(x))
        plot_wordcloud(df=df_copy, col=col, name_of_file=name_of_file, timenow=timenow)  # Plotting wordcloud


# For plotting numerical features
def plot_numerical(df, name_of_file, col, timenow):
    """
    For plotting numerical features

    :param df: Dataframe
    :type df: pd.DataFrame
    :param name_of_file: File name
    :type name_of_file: str
    :param col: Feature Columns
    :type col: str
    :param timenow: Current time
    :type timenow: datetime
    """
    # probability density plot
    plt.figure()
    sns.boxplot(
        data=df,
        x=col,
        width=NUM_PLOT_PARAMS['width'],
        color=NUM_PLOT_PARAMS['color'])
    sns.despine(left=True)

    # Calculating 1st quantile
    q1 = df[col].quantile(0.25)
    q1_text = f"Q1\n{q1}"

    # Calculating 2nd quantile
    q2 = df[col].quantile(0.5)
    q2_text = f"Q2\n{q2}"

    # Calculating 3rd quantile
    q3 = df[col].quantile(0.75)
    q3_text = f"Q3\n{q3}"

    # Calculating min
    mind = np.round(df[col].min(), 2)
    mind_text = f"Min\n{mind}"

    # Calculating max
    maxd = np.round(df[col].max(), 2)
    maxd_text = f"Max\n{maxd}"

    plt.text(q1, -0.15, q1_text, ha='center')
    plt.text(q2, 0.25, q2_text, ha='center')
    plt.text(q3, -0.15, q3_text, ha='center')
    plt.text(mind, 0.35, mind_text, ha='center')
    plt.text(maxd, 0.35, maxd_text, ha='center')

    plt.xlabel(col, fontsize=NUM_PLOT_PARAMS['axis_fontsize'])
    plt.title(f'Distribution of "{col}"',
              fontsize=NUM_PLOT_PARAMS['title_fontsize'])

    # Saving plot
    plotname = f'{plot_folder}\\{name_of_file}_{col}_{timenow}.png'
    plt.savefig(plotname)




def plot_discrete(df, name_of_file, col, timenow):
    """
    For plotting discrete features

    :param df: Dataframe
    :type df: pd.DataFrame
    :param name_of_file: File name
    :type name_of_file: str
    :param col: Feature
    :type col: str
    :param timenow: Current time
    :type timenow: datetime
    """
    df_copy = df.copy()

    try:
        df_copy[col] = df_copy[col].astype('int')
    except:
        df_copy[col] = df_copy[col].astype('category')

    month_order = [i.title() for i in MONTHS]

    day_order = [i.title() for i in DAYS]

    plot_month = False
    plot_day = False

    if df_copy[col].nunique() == 2:
        # Pieplot
        plt.figure()
        plt.pie(df_copy[col].value_counts(),
                labels=list(df_copy[col].unique()),
                autopct=PIE_PLOT_PARAMS['autopct'],
                radius=PIE_PLOT_PARAMS['radius'],
                textprops=PIE_PLOT_PARAMS['textprops'])
        plt.title(f'Composition of "{col}"',
        fontsize=PIE_PLOT_PARAMS['title_fontsize'])
        plt.tight_layout()
    else:
        # Horizontal barplot
        for i in df[col].apply(lambda x: str(x).lower()).unique():
            if i in MONTHS:
                plot_month=True
            elif i in DAYS:
                plot_day=True
        # Plotting months
        if plot_month:
            plt.figure(figsize=BAR_PLOT_PARAMS['figsize'])
            plt.subplot(1, 2, 1)
            sns.countplot(
                data=df_copy,
                y=col,
                palette=BAR_PLOT_PARAMS['palette'],
                ec=BAR_PLOT_PARAMS['ec'],
                order=month_order)
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.subplot(1, 2, 2)
            sns.countplot(data=df_copy,
                          y=col,
                          palette=BAR_PLOT_PARAMS['palette'],
                          ec=BAR_PLOT_PARAMS['ec'],
                          order=list(df_copy[col].value_counts().index))
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.suptitle(
                f'Composition of "{col}"',
                fontsize=BAR_PLOT_PARAMS['title_fontsize'])
        # Plotting days
        elif plot_day:
            plt.figure(figsize=BAR_PLOT_PARAMS['figsize'])
            plt.subplot(1, 2, 1)
            sns.countplot(
                data=df_copy,
                y=col,
                palette=BAR_PLOT_PARAMS['palette'],
                ec=BAR_PLOT_PARAMS['ec'],
                order=day_order)
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.subplot(1, 2, 2)
            sns.countplot(data=df_copy,
                          y=col,
                          palette='bwr',
                          ec='black',
                          order=list(df_copy[col].value_counts().index))
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.suptitle(
                f'Composition of "{col}"', 
                fontsize=BAR_PLOT_PARAMS['title_fontsize'])
        # Plotting regular barplots
        else:
            plt.figure(figsize=BAR_PLOT_PARAMS['figsize'])
            plt.subplot(1, 2, 1)
            try:
                plot_order = sorted(list(df_copy[col].unique()))
            except:
                plot_order = None
            sns.countplot(
                data=df_copy, 
                y=col, 
                palette='bwr',
                ec='black', 
                order=plot_order)
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.subplot(1, 2, 2)
            try:
                plot_order = list(df_copy[col].value_counts().index)
            except:
                plot_order = None
            sns.countplot(data=df_copy,
                          y=col,
                          palette='bwr',
                          ec='black',
                          order=plot_order)
            sns.despine()
            plt.xlabel(f'Count of "{col}"',
                       fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.ylabel(col, fontsize=BAR_PLOT_PARAMS['axis_fontsize'])
            plt.suptitle(
                f'Composition of "{col}"', 
                fontsize=BAR_PLOT_PARAMS['title_fontsize'])
        plt.tight_layout()
    
    # Saving plot
    plotname = f'{plot_folder}\\{name_of_file}_{col}_{timenow}.png'
    plt.savefig(plotname)

# Plot correlations Scatter plot


def plot_correlation(df, name_of_file, corlist, timenow):
    """
    For plotting correlation between features

    :param df: Dataframe
    :type df: pd.DataFrame
    :param name_of_file: File name
    :type name_of_file: str
    :param corlist: List of correlated features
    :type corlist: list
    :param timenow: Current time
    :type timenow: datetime
    :return: Plot name
    :rtype: str
    """
    if len(corlist) <= 4:
        height=4
    else:
        height=len(corlist)*0.9
    plt.figure(figsize=(15, height))
    plotnumber=1
    for item in corlist:
        if plotnumber < 1+len(corlist):
            if type(item[0]) is not str:
                ax=plt.subplot(int(np.ceil(len(corlist)/4)), 4, plotnumber)
                plt.scatter(x=df[item[1]], y=df[item[2]],
                            color=CORR_PLOT_PARAMS['color'],
                            alpha=CORR_PLOT_PARAMS['alpha'],
                            s=CORR_PLOT_PARAMS['s'])
                plt.xticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.yticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.xlabel(
                    item[1], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.ylabel(
                    item[2], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.title(f"Corr={item[0]}")
            elif type(item[1]) is not str:
                ax=plt.subplot(int(np.ceil(len(corlist)/4)), 4, plotnumber)
                plt.scatter(x=df[item[0]], y=df[item[2]],
                            color=CORR_PLOT_PARAMS['color'],
                            alpha=CORR_PLOT_PARAMS['alpha'],
                            s=CORR_PLOT_PARAMS['s'])
                plt.xticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.yticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.xlabel(
                    item[0], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.ylabel(
                    item[2], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.title(f"Corr={item[1]}")
            elif type(item[2]) is not str:
                ax=plt.subplot(int(np.ceil(len(corlist)/4)), 4, plotnumber)
                plt.scatter(x=df[item[1]], y=df[item[0]],
                            color=CORR_PLOT_PARAMS['color'],
                            alpha=CORR_PLOT_PARAMS['alpha'],
                            s=CORR_PLOT_PARAMS['s'])
                plt.xticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.yticks(fontsize=CORR_PLOT_PARAMS['ticks_fontsize'])
                plt.xlabel(
                    item[1], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.ylabel(
                    item[0], 
                    fontsize=CORR_PLOT_PARAMS['axis_fontsize'])
                plt.title(f"Corr={item[2]}")
            plotnumber += 1
    plt.suptitle('Correlated Numerical Variables',
                 fontsize=CORR_PLOT_PARAMS['title_fontsize'])
    plt.tight_layout()
    
    # Saving plot
    plotname=f"{plot_folder}\\{name_of_file}_numerical_correlation_{timenow}.png"
    plt.savefig(plotname)
    return plotname

# Plotting missing values

def plot_missing(df, name_of_file, timenow):
    """
    For plotting missing feature data

    :param df: Dataframe
    :type df: pd.DataFrame
    :param name_of_file: File name
    :type name_of_file: str
    :param timenow: Current time
    :type timenow: datetime
    :return: Plot names
    :rtype: str
    """
    # Generating dictionary of missing values
    missing_dict = {}
    
    for col in df:
        missing_dict[col] = np.round(100*(df[col].isnull().mean()), 2)
    
    missing_dict = {
        k: v for k, v in sorted(missing_dict.items(), 
        key=lambda item: item[1], 
        reverse=True)}
    missing_dict = {k: v for k, v in missing_dict.items() if v!=0}

    # Plotting missing values bar chart
    plt.figure(figsize=MISSING_PLOT_PARAMS['figsize'])
    
    sns.barplot(x=list(missing_dict.values()), 
                y=list(
                    missing_dict.keys()), 
                    color=MISSING_PLOT_PARAMS['color'])
    sns.despine()
    plt.xticks(fontsize=MISSING_PLOT_PARAMS['ticks_fontsize'])
    plt.xlabel(
        "% Missing value", 
        fontsize=MISSING_PLOT_PARAMS['axis_fontsize'])
    plt.yticks(fontsize=MISSING_PLOT_PARAMS['ticks_fontsize'])
    plt.ylabel(
        "Columns", 
        fontsize=MISSING_PLOT_PARAMS['axis_fontsize'])
    plt.title(
        '% Missing Values in the data.', 
        fontsize=MISSING_PLOT_PARAMS['title_fontsize'])
    
    # setting values over barplot
    for index, value in enumerate(list(missing_dict.values())):
        plt.text(
            value+0.01*(max(list(missing_dict.values()))), 
            index, 
            str(value)+"%", 
            fontdict={'fontsize':MISSING_PLOT_PARAMS['annot_fontsize']})
    datenow, timenow=get_datetime()
    miss_bar_name = f'{plot_folder}\\{name_of_file}_missing_hbar_{timenow}.png'
    plt.savefig(miss_bar_name)

    # Generating heatmap
    missing_hmap = msno.heatmap(
        df, 
        fontsize=MISSING_PLOT_PARAMS['hmap_fontsize'], 
        cbar=False)
    plt.title(
        'Missing Values Correlation map', 
        fontsize=MISSING_PLOT_PARAMS['hmap_title_fontsize'], 
        y=1.05)
    
    # Saving plot
    miss_hmap_name = f"{plot_folder}\\{name_of_file}_missing_hmap_{timenow}.png"
    missing_hmap_copy = missing_hmap.get_figure()
    missing_hmap_copy.savefig(miss_hmap_name, bbox_inches = 'tight')
    return miss_bar_name, miss_hmap_name
