#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:25:35 2017

@author: T. Swayne
"""



#==============================================================================
# Consider our representation of permutations of students in a line 
# from Exercise 1. (The teacher only swaps the positions of two students that 
# are next to each other in line.) Let's consider a line of three students, 
# Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class 
# created in the lecture, we can create a graph with the design chosen 
# in Exercise 1: vertices represent permutations of the students in line; 
# edges connect two permutations if one can be made into the other by 
# swapping two adjacent students.
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
        
        
#==============================================================================
# We construct our graph by first adding the following nodes:
#==============================================================================

# make a list
#nodes = []
#nodes.append(Node("ABC")) # nodes[0]
#nodes.append(Node("ACB")) # nodes[1]
#nodes.append(Node("BAC")) # nodes[2]
#nodes.append(Node("BCA")) # nodes[3]
#nodes.append(Node("CAB")) # nodes[4]
#nodes.append(Node("CBA")) # nodes[5]

# make the items in the list into nodes
#g = Graph()
#for n in nodes:
#    g.addNode(n)

# sample for creating specific edges, from L03-2
# g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))

# adding specific edges -- there are 12 for an arrangement of 3 
# (2 possible swaps per arrangement) -- but half of these are redundant 
# so really only 6

#g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB"))) # swapping B and C
#g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC"))) # swapping A and B
#g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))
#g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))
#g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))
#g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA"))) 


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


# testing nodes and edges
# for n in nodes:
#    print(n.getName())
#    print(g.childrenOf(n)) did not work

def buildKidGraph(graphType):
    g = graphType()
    
    for name in ('ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'): #Create 6 nodes
        g.addNode(Node(name))

    g.addEdge(Edge(g.getNode("ABC"), g.getNode("ACB"))) # swapping B and C
    g.addEdge(Edge(g.getNode("ABC"), g.getNode("BAC"))) # swapping A and B
    g.addEdge(Edge(g.getNode("ACB"), g.getNode("CAB")))
    g.addEdge(Edge(g.getNode("BAC"), g.getNode("BCA")))
    g.addEdge(Edge(g.getNode("BCA"), g.getNode("CBA")))
    g.addEdge(Edge(g.getNode("CAB"), g.getNode("CBA"))) 
    return g
    
print(buildKidGraph(Graph))