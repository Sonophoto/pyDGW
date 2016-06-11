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

Maintains a list of Nodes in a graph with the callback functions
that define the edges and possible transistions from one node to
the next. implements methods for adding nodes, setting nodes to 
be ending or starting nodes, and then walking thru the nodes by
calling the callback function of each node it enters beginning 
with the start node until it enters an end node.
"""

import sys


# This class is supposed to be the data passed thru the nodes ref Python 3 tutorial section 9.7.
#
# so do 
# foo = DGW_data()
# foo.bar = 'cat'
# foo.foo = 'dog'
# foo.method = someReference
#A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods read() and readline() that get the data from a string buffer instead, and pass it as an argument.
#
#Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is the function object corresponding to the method.


class DGW_data:
   pass


class DGW:
   def __init__(self):
      """constructor for the python Directed Graph Walker.  Each node
      (or state/vertex) has a callback, and it is the callback that 
      defines the edges"""
      self.callbacks = {}    #Dictionary of node_name:callback PERL:HASH
      self.startNode = None  #Set startNode to "NULL"        PERL:SCALAR 
      self.endNodes  = []    #list of nodes that can exit.     PERL:LIST
      # every flippin thing in the language is a reference! see id() 


   def addNode(self, node_name, callback):
      """Adds a node and its callback to our nodelist. This is the 
      actual node, the callbacks define the edges"""

      self.callbacks[node_name] = callback # Popu. Asso. Array.


   def setStartNode(self, node_name):
      """Sets a node to be a startNode for the graph walker"""
        
      self.startNode = node_name # Setting a scalar value


   def setEndNode(self, node_name):
      """Sets a node to be an endNode for the graph walker"""

      self.endNode.append(node_name) #ALL variables are objects! With methods?!! nice.


   def run(self, DGW_node):
      """Confirms model has a startNode and and endNode and 
           begins an event loop on the startNode."""
           # Exception Handling: https://wiki.python.org/moin/HandlingExceptions
      try:
         operator = self.callbacks[self.startNode]
      except:
         sys.exit("No starting node has been set, aborting")
      
      if not self.endNodes: 
         sys.exit("No ending node has been set, aborting")

      while TRUE:
         (next_node, DGW_data) = operator(DGW_data)
         if next_node in self.endNodes: # We have reached an endNode
            break;
         else:                          # Otherwise, set the next operator
            operator = self.callbacks[next_node]




