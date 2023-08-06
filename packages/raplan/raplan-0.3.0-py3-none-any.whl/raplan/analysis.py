"""Tools for planning and scheduling analysis."""

from typing import Union

from ragraph.edge import Edge
from ragraph.graph import Graph
from ragraph.node import Node

from raplan.classes import Project


def get_maintenance_graph(project: Project, threshold: Union[int, float]) -> Graph:
    """Get a graph of maintenance tasks. Edges are generated with an adjacency value of
    of the threshold minus the time difference between tasks.

    Arguments:
        project: Scheduling project to generate a graph for.
        threshold: Maximum time difference. Tasks that are within this threshold will be
            assigned an adjacency edge.

    Returns:
        Graph of maintenance tasks.
    """
    graph = Graph(
        nodes=[
            Node(
                kind="maintenance",
                annotations=dict(
                    system=s.name,
                    component=c.name,
                    maintenance=m.name,
                    time=m.time,
                    task=m.task.name,
                    cost=m.task.cost,
                    duration=m.task.duration,
                ),
            )
            for s in project.systems
            for c in s.components
            for m in c.maintenance
        ]
    )

    nodes = graph.nodes
    for i, n1 in enumerate(graph.nodes):
        for n2 in nodes[i + 1 :]:

            delta_t = abs(n1.annotations.time - n2.annotations.time)
            if delta_t >= threshold:
                continue
            weight = threshold - delta_t

            graph.add_edge(
                Edge(
                    source=n1,
                    target=n2,
                    kind="adjacency",
                    weights=dict(adjacency=weight),
                )
            )
            graph.add_edge(
                Edge(
                    source=n2,
                    target=n1,
                    kind="adjacency",
                    weights=dict(adjacency=weight),
                )
            )

    return graph
