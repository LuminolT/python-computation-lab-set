'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-05-06 06:21:52
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-05-06 06:42:02
FilePath: /lab-3/sublab-1/visualize.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''
import networkx as nx
import matplotlib.pyplot as plt


def ackermann(m: int, n: int) -> int:
    """
        Ackerman function.
    """
    if m < 0 or n < 0:
        raise ValueError("Not Positive Interger")
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# 创建有向图
G = nx.DiGraph()


def add_node(m, n):
    G.add_node((m, n))
    if m == 0:
        return
    elif n == 0:
        add_node(m - 1, 1)
        G.add_edge((m, n), (m - 1, 1))
    else:
        add_node(m, n - 1)
        add_node(m - 1, ackermann(m, n - 1))
        G.add_edge((m, n), (m, n - 1))
        G.add_edge((m, n), (m - 1, ackermann(m, n - 1)))


add_node(3, 4)
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True)
plt.show()
