"""
*********************************************************************
    Python
     -3.5-
                             ____     ____  _        _
               _ __  _   _  |  _ \   / ___|| \      / |
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

  ASCII_ART: Jennifer E. Swofford
                      __    __    __    __
                     /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \  \____
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<

*********************************************************************
"""

class DGW:
   """Maintains a list of Nodes in a graph with the callback functions
      that define the edges and possible transistions from one node to
      the next. implements methods for adding nodes, setting nodes to 
      be ending or starting nodes, and then walking thru the nodes by
      calling the callback function of each node it enters beginning 
      with the start node until it enters an end node."""



    def __init__(self):
        """constructor for the python Directed Graph Walker.
           Each node (or state/vertex) has a callback, and it is
           the callback that defines the edges"""
        self.callbacks = {} #Dictionary of node_name:callback
        self.startNode = None #Set startNode to "NULL"
        self.endNodes  = [] #list of nodes that can exit.


    def addNode(self, node_name, callback):
        """Adds a node and its callback to our nodelist. This 
           is the actual node, the callbacks define the edges"""



    def setStartNode(self, node_name):
        """Sets a node to be a startNode for the graph walker"""



    def setEndNode(self, node_name):
        """Sets a node to be an endNode for the graph walker"""



    def run(self, node_data):
        """Confirms model has a startNode and and endNode and 
           begins an event loop on the startNode."""
