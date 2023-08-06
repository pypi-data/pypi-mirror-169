import os

"""
This module holds the global parameter values.
"""

# Current date format
DATE_FORMAT = "%Y-%m-%d"

# Current time format
TIME_FORMAT = "%Hh-%Mm-%Ss"

# List of Pandas numeric datatypes
NUMERIC_TYPES = ['int8', 'int16', 'int32',
                 'int64', 'float16', 'float32', 'float64']

# List of Pandas categorical datatypes
CATEGORY_TYPES = ['bool', 'category']

# List of Pandas datetime datatypes
DATETIME_TYPES = ['datetime64[ns]', 'timedelta[ns]']

# Pearson Correlation Coefficient threshold
CORR_THRESHOLD = 0.5

# Text length for identifying primary keys
MAX_TEXT_LENGTH = 50

# Percentage missing values threshold
PERCENT_MISSING_VAL = 50

# Skewness threshold
SKEWNESS = [-0.75, 0.75]

# Outlier threshold
PERCENT_OUTLIER_LIMIT = 25

# Format of saved plots
PLOT_FORMAT = ['png']

# Values for Wordcloud
WORDCLOUD_PARAMS = {
    'width': 1200,
    'height': 600,
    'color': 'white',
    'facecolor': None,
    'figsize': (8, 8),
    'fontsize': 10
}

# Values for numerical plots
NUM_PLOT_PARAMS = {
    'width': 0.25,
    'color': '#ACD6F1',
    'axis_fontsize': 14,
    'title_fontsize': 16
}

# List of months
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']

# List of days
DAYS = ['sunday', 'monday', 'tuesday',
        'wednesday', 'thursday', 'friday', 'saturday']

# Pie plot parameters
PIE_PLOT_PARAMS = {
    'autopct': '%2.2f%%',
    'radius': 1,
    'textprops': {
        'fontsize': 12
    },
    'title_fontsize': 16
}

# Bar plot parameters
BAR_PLOT_PARAMS = {
    'figsize': (15, 6),
    'palette': 'bwr',
    'ec': 'black',
    'axis_fontsize': 14,
    'title_fontsize': 16
}

# Correlation plot parameters
CORR_PLOT_PARAMS = {
    'color': 'blue',
    'alpha': 0.35,
    's': 10,
    'ticks_fontsize': 11,
    'axis_fontsize': 12,
    'title_fontsize': 18
}

# Missing value plot parameters
MISSING_PLOT_PARAMS = {
    'figsize': (15, 10),
    'color': '#FE9595',
    'ticks_fontsize': 13,
    'axis_fontsize': 15,
    'title_fontsize': 18,
    'annot_fontsize': 13,
    'hmap_fontsize': 21,
    'hmap_title_fontsize': 27
}

# This dictionary consists of the parameters for defining the Log folder structure.
generate_directory = {
    "dir_structure": None,
    "basefolder": "artifacts"
}

# This variable is used for getting the current working directory path.
curr_directory = os.getcwd()
