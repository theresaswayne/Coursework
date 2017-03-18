#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:51:41 2017

@author: T. Swayne
"""
#==============================================================================
# code from ex2
# 
#==============================================================================

# here are the graph classes from lec03-2

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
               
#==============================================================================
# ex 7
#==============================================================================
# Write a WeightedEdge class that extends Edge. 
# Its constructor requires a weight parameter, 
# as well as the parameters from Edge. 
# You should additionally include a getWeight method. 
# The string value of a WeightedEdge from node A to B 
# with a weight of 3 should be "A->B (3)".

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() \
               + ' (' + str(self.getWeight()) + ')'
    
class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
        

 
# testing


# testing nodes and edges
# for n in nodes:
#    print(n.getName())
#    print(g.childrenOf(n)) did not work

def buildKidGraph(graphType):
    g = graphType()
    
    for name in ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'): #Create 6 nodes
        g.addNode(Node(name))

    w = WeightedEdge(g.getNode("ABC"), g.getNode("ACB"), 6)
    print(w.getWeight())
    print(str(w))
    
    return g
    
buildKidGraph(Graph)



# TODO: ideas for adding edges automatically --
# make the string into a chain (or use slicing)
# go through the string and swap each position with the one after
# swap1 = s[0:i-1]+s[i:i+1]+s[i-1:i]+s[i+1:]
# or go through the nodes, getName, and something like 
#(stackoverflow)
# def swap(c, i, j):
# ...  c = list(c)
# ...  c[i], c[j] = c[j], c[i]
# ...  return ''.join(c)
#s = '2134'
#swap(s, 0, 1)
#'1234'
