#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:04:37 2018
Author:     Allan Olsen aka cjoke
Purpose:    Create a mindmap application with graphviz and save as dot file.
license:    MIT License (see LICENSE online)
"""
import graphviz as gv
import os

class Mindmap:
    def __init__(self, name):
        self.name = name
        self.graph = gv.Digraph(format='dot')
        self.graph.attr('node', shape='box')

    def add_node(self, node):
        self.graph.node(node)

    def remove_node(self, node):
        self.graph.node(node, _attributes={'style': 'invis'})

    def add_edge(self, edge, label=None):
        if label:
            self.graph.edge(edge[0], edge[1], label=label)
        else:
            self.graph.edge(edge[0], edge[1])

    def save(self):
        self.graph.render(self.name, view=True)
        os.remove(self.name)

class UserDialog:
    def __init__(self, mindmap):
        self.mindmap = mindmap

    def view_nodes(self):
        return self.mindmap.graph.body

    def add_node(self, node):
        self.mindmap.add_node(node)

    def remove_node(self, node):
        self.mindmap.remove_node(node)

    def add_edge(self, edge, label=None):
        self.mindmap.add_edge(edge, label)

if __name__ == '__main__':
    m = Mindmap('test')
    u = UserDialog(m)
    u.add_node('a')
    u.add_node('b')
    u.add_node('c')
    u.add_edge(('b', 'a'), label='pointer')
    u.add_edge(('b', 'c'), label='pointer')
    u.add_edge(('a', 'b'), label='pointer')
    u.add_edge(('a', 'c'), label='pointer')
    print(u.view_nodes())
    m.save()
