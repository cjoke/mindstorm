#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:04:37 2018
Author:     Allan Olsen aka cjoke
Purpose:    Create a mindmap application with graphviz and save as dot file.
license:    MIT License (see LICENSE online)
"""


import graphviz as gv
from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Command:
    """
    This class represents a command that the user can execute.
    """

    name: str
    description: str
    action: Callable[[], None]


@dataclass
class UserDialog:
    """
    This class is responsible for processing user input.
    """

    graph: gv.Digraph
    commands: List[Command]

    def __init__(self, graph):
        self.graph = graph
        self.commands = self.initialize_commands()

    def initialize_commands(self) -> List[Command]:
        return [
            Command("1", "Add node", self.add_node),
            Command("2", "Remove node", self.remove_node),
            Command("3", "Add edge", self.add_edge),
            Command("4", "View nodes", self.view_nodes),
            Command("5", "Save graph", self.save_graph),
            Command("6", "Exit", self.exit),
        ]

    def add_node(self):
        node = input("Enter the name of the node you want to add: ")
        self.graph.node(node)

    def remove_node(self):
        # Graphviz does not support removing nodes directly.
        # You might need to create a new graph without the node to remove it.
        pass

    def add_edge(self):
        edge = input(
            "Enter the names of the two nodes you want to connect, separated by a comma: "
        ).split(",")
        self.graph.edge(edge[0].strip(), edge[1].strip())

    def view_nodes(self):
        print(self.graph.source)

    def save_graph(self):
        self.graph.render("graph", view=True)

    def exit(self):
        self.save_graph()
        exit()

    def start(self):
        while True:
            for command in self.commands:
                print(f"{command.name}. {command.description}")
            choice = input("Choose an option: ")

            for command in self.commands:
                if choice == command.name:
                    command.action()
                    break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    m = gv.Digraph(format="dot")
    d = UserDialog(m)
    d.start()
