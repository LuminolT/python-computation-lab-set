'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-05-06 06:36:28
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-05-06 06:41:20
FilePath: /lab-3/sublab-1/visualize_html.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''
import plotly.graph_objects as go
import networkx as nx


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

node_x = []
node_y = []
for key in pos:
    x, y = pos[key]
    node_x.append(x)
    node_y.append(y)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=[f'A({m},{n})' for m, n in G.nodes()],
    textposition="top center",
    marker=dict(
        color='lightblue',
        size=15
    )
))

fig.add_trace(go.Scatter(
    x=edge_x, y=edge_y,
    mode='lines',
    line=dict(width=1, color='gray'),
    hoverinfo='none'
))


fig.update_layout(
    title_text="Ackermann Function Call Graph",
    title_x=0.5,
    showlegend=False,
    width=800,
    height=600,
    hovermode='closest',
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
)

fig.write_html("ackermann_graph.html")
