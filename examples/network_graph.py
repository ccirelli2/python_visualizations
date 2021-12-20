"""
Examples of how to create network graphs in python.

References:
    https://towardsdatascience.com/from-dataframe-to-network-graph-bbb35c8ab675
    https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/
"""
# Libraries
import os
import pandas as pd
import numpy
import networkx as nx
from decouple import config as d_config
from matplotlib.pyplot import figure

# Directories
DIR_SRC = d_config('DIR_SRC')
DIR_DATA = d_config('DIR_DATA')

# Data Files
JIRA_DATA_FILENAME = 'jira_sample.csv'
JIRA_DATA = pd.read_csv(os.path.join(DIR_DATA, JIRA_DATA_FILENAME))
JIRA_DATA_LIM = JIRA_DATA.loc[:, ['Assignee', 'Reporter']]

# Create Instance of Graph
nx_Graph = nx.Graph()

# Populate Graph
n_Graph = nx.from_pandas_edgelist(JIRA_DATA_LIM, 'Assignee', 'Reporter')

# Create Figure
figure(figsize=(10, 8))
nx.draw_shell(n_Graph, with_labels=True)
