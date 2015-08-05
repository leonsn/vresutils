import networkx as nx
import numpy as np

from vresutils.graph import OrderedGraph

from . import make_toModDir
toModDir = make_toModDir(__file__)

def penalize(x, n):
    """
    Thumb-rule for the aggregation of cross-border power lines.

    Parameters
    ---------
    x : float
        total line capacity
    n : int
        number of power lines

    Returns
    -------
    c : float
        resulting capacity
    """

    if n == 1:
        return x
    elif n == 2:
        return 5./6. * x
    elif n == 3:
        return 4./6. * x
    else:
        return .5 * x

##
# Functions which provide access to special network data
#

def entsoe_tue():
    return OrderedGraph(nx.read_gpickle(toModDir("data/entsoe_2009_final.gpickle")))

def entsoe_tue_linecaps(with_manual_link=True):
    G = entsoe_tue()

    # Add linecapacities by assuming:
    # - number of circuits is always 2
    # - 380kV if any of the connected nodes are 380kV and 220kV else
    # - 380kV lines have a capacity of 1500MW per circuit
    # - 220kV lines have a capacity of 500MW per circuit.

    voltages = nx.get_node_attributes(G, 'voltage')
    for n1, n2, attr in G.edges_iter(data=True):
        voltage = max(voltages.get(n1, 380), voltages.get(n2, 380))
        capacity = 2. * (1.5 if voltage == 380 else 0.5)
        attr.update(voltage=voltage, capacity=capacity)

    # Add missing link
    if with_manual_link:
        length = node_distance(G, '782', '788')
        X = specific_susceptance * length
        G.add_edge('788', '782',
                   capacity=3.0, X=X, Y=1/X,
                   length=length, limit=0.0, voltage=380)

    return G

# Given by bialek's network
# TODO : replace this by a well founded value from oeding or similar
# as soon as we can switch to a scigrid based network
specific_susceptance = 0.00068768296005101493  # mean of X / L

def node_distance(G, n1, n2):
    """
    A distance measure between two nodes in graph `G` which correlates
    well with what is already present in the length edge attribute in
    the bialek grid.

    Arguments
    ---------
    G : nx.Graph
    n1 : node label 1
    n2 : node label 2

    Returns
    -------
    d : float
        distance
    """
    return 110. * np.sqrt(np.sum((G.node[n1]['pos'] - G.node[n2]['pos'])**2))

def eu():
    return nx.read_gpickle(toModDir("data/EU.gpickle"))