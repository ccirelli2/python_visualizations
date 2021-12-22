"""
Create a network graph of linked in connections

References:
https://medium.com/bitgrit-data-science-publication/visualize-your-linkedin-network-with-python-59a213786c4

"""
# Libraries
import os
import pandas as pd
from decouple import config as d_config
import matplotlib.pyplot as plt

# Library Settings
pd.set_option("max_columns", None)

# Directories
DIR_SRC = d_config("DIR_SRC")
DIR_DATA = d_config("DIR_DATA")

# Data Files
DATA_FILENAME = "Connections.csv"
DATA_CONN = pd.read_csv(os.path.join(DIR_DATA, DATA_FILENAME), skiprows=2)

def group_by_cnt(
    df_data: pd.DataFrame, col_name: str, top: int = 0, pplot: bool = False
) -> pd.DataFrame:
    """
    Function to group data by column and get count.  Also, can plot.
    param df_data:
    :param df_data:
    :param col_name:
    :param top:
    :param pplot:
    :return:
    """
    df_grouped = (
        df_data.groupby(col_name)[col_name].count().sort_values(ascending=False)
    )

    if top:
        df_grouped = df_grouped.head(top)

    if pplot:
        df_grouped.plot(kind="bar", title="Top Connections By Cnt")
        plt.tight_layout()
        plt.show()

    return df_grouped


rel_company = group_by_cnt(df_data=DATA_CONN, col_name="Company", top=10, pplot=False)

rel_position = group_by_cnt(df_data=DATA_CONN, col_name="Position", top=10, pplot=True)
