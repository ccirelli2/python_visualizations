"""
Examples of how to create network graphs in python.

References:
    https://towardsdatascience.com/from-dataframe-to-network-graph-bbb35c8ab675
    https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/
"""
# Libraries
import os
import pandas as pd
import networkx as nx
from decouple import config as d_config
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

# Directories
DIR_SRC = d_config("DIR_SRC")
DIR_DATA = d_config("DIR_DATA")

# Data Files
JIRA_DATA_FILENAME = "jira_sample.csv"
JIRA_DATA = pd.read_csv(os.path.join(DIR_DATA, JIRA_DATA_FILENAME))
JIRA_DATA_LIM = JIRA_DATA.loc[:, ["Assignee", "Reporter"]]

# Declare Variables
GEN_PLOT = True

# Create Instance of Graph
nx_Graph = nx.Graph()

# Populate Graph
n_Graph = nx.from_pandas_edgelist(JIRA_DATA_LIM, "Assignee", "Reporter")

# Generate Plot
if GEN_PLOT:
    figure(figsize=(5, 4))
    nx.draw_shell(n_Graph, with_labels=True)
    # plt.show()
    plt.savefig('ex_network_graph.png')

# Create Data-Frame Num Connections
def get_num_connections(graph: nx.Graph) -> pd.DataFrame:
    """
    Function to create a dataframe with the node name and connection count.

    :type graph: nx.Graph instance.
    :param graph: network graph.
    :return: dataframe with one column as the node name and the other the number of connections.
    """
    num_connections = {x: len(graph[x]) for x in list(graph)}
    df_connections = pd.DataFrame.from_dict(num_connections, "index").reset_index()
    df_connections.rename(columns={'index': 'Feature', 0: "Num_Connections"}, inplace=True)
    df_connections.sort_values(
        by="Num_Connections", ascending=False, inplace=True
    )
    return df_connections
