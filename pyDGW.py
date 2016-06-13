"""
*********************************************************************
                   python Directed Graph Walker

   Python                    ____     ____  _        _
    -3.5-      _ __  _   _  |  _ \   / ___|| \      / |
              | '_ \| | | | | | | | | |  _  \ \ /\ / / 
              | |_) | |_| | | |_| | | |_| |  \ V  V /  
              | .__/ \__, | |____/   \____|   \_/\_/   
              |_|    |___/                        
                "Follow the Arrows until the end..."

   FILENAME: pyDGW.py 
     AUTHOR: "Brig Young, https://github.com/Sonophoto/"
    PURPOSE: "Implements a basic state machine architecture"               
  COPYRIGHT: "2016 Brig Young, http://SonophotoStudios.com/" 
    LICENSE: "BSD 2-Clause, See LICENSE file in project root"         

*********************************************************************
This class implements an object that walks through a user defined
state machine or directed graph, however you perfer to see it.

Maintains a list of named nodes(vertices) in a directed graph.

Each node has a user defined callback function that implements the
possible transistions (edges) from itself to other nodes.

The callbacks pass an object that contains user defined state
information and/or the data being processed to the next node.

Implements methods for adding nodes, and setting nodes to be ending 
and starting nodes.

Implements a mathod for walking thru the nodes by calling the
callback function of each node it enters beginning with the start
node until it enters an end node.
"""

import sys


class DGW_data:
   """This is an empty class that is to be instantiated and then 
   populated with whatever variables your state machine needs to
   maintain. It will be passed from node to node automatically"""
   pass


class DGWalker:
   """This class implements the actual graph walker and the support 
   functions to initialize it. The constructor creates a blank object
   and the methods addNode(), setStartNode() and setEndNodes() are used
   to configure the state machine with named nodes and callbacks"""

   def __init__(self):
      """constructor for the python Directed Graph Walker. We have a 
      blank dictionary for our node_name->callback association. We have
      a blank startNode and a blank list of endNodes."""
      self.callbacks = {}
      self.startNode = None 
      self.endNodes  = [] 
      self.DEBUG     = False

   def addNode(self, node_name, callback):
      """Adds a node and its callback to our dictionary."""
      # This creates a hash (dict) of nodes and their callback references
      if self.DEBUG:
         print("Adding node:", node_name)
      self.callbacks[node_name] = callback 


   def setStartNode(self, node_name):
      """Sets a node to be the startNode for the graph walker"""
      if self.DEBUG:
         print("setting", node_name, "to .startNode")
      # This sets a scalar value to our .startNode
      self.startNode = node_name


   def setEndNode(self, node_name):
      """Sets a node to be an endNode for the graph walker"""
      if self.DEBUG:
         print("Adding", node_name, "to .endNodes list")
      # This creates a list of .endNodes for our loop control 
      self.endNodes.append(node_name)


   def run(self, DGW_node):
      """Confirms model has a startNode and at least one endNode. 
      Begins an event loop on the startNode."""

      # Make sure we have a .startNode
      try:
         operator = self.callbacks[self.startNode]
      except:
         sys.exit("No starting node has been set, use .setStartNode()")
      if self.DEBUG:
         print("Start Node is:", self.startNode)
      # Make sure we have At Least one .endNode.
      if not self.endNodes: 
         sys.exit("No ending nodes have been set, use .setEndNode()")
      if self.DEBUG:
         print("End Nodes are:", self.endNodes)
      
      # Loop until we hit an end state and then run its code (output)
      while True:
         (next_node, DGW_node) = operator(DGW_node)
         if self.DEBUG:
            print("next_node is:", next_node)
         if next_node in self.endNodes:
            if self.DEBUG:
               print("next_node is an endNode:", next_node)
            operator = self.callbacks[next_node]
            operator(DGW_node) 
            break;
         else:                        
            operator = self.callbacks[next_node]
         if self.DEBUG:
            print("Bottom of loop, queued operator is:", operator)




