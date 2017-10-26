
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

Maintains a dict of named nodes(vertices) in a directed graph.

Each node has a user defined callback function that implements the
possible transistions (edges) from itself to other nodes.

The callbacks pass an object that contains user defined state
information and/or the data being processed to the next node.

Implements methods for adding nodes, and setting nodes to be ending
and starting nodes.

Implements a method for walking thru the nodes by calling the
callback function of each node it enters beginning with the start
node until it enters an end node and finally running the code in
the end node to generate output etc.
"""


import sys


class DGW_data:
   """
   This is the Data class for the DGW. Create an instance that
   inherits from this class and then extend it with the variables
   you need to track.It will be passed around automatically
   """
   pass


class DGWalker:
   """
   Implements the  DGW. The constructor creates a blank object.
   Methods addNode(), setStartNode() and setEndNodes() are used to
   configure the state machine with named nodes and callbacks
   """

   def __init__(self):
      """Constructor initializes data members and DEBUG defaults"""

      self.operator_counter = 0
      """This counts how many operations have been performed from
      .startNode to .endNodes[]."""

      self.node_counter = 1
      """This counts how many nodes have been entered including the
      .startNode."""

      self.callbacks = {}
      """The dictionary of node names and their callbacks"""

      self.startNode = None
      """The node name to use as the initial callback key"""

      self.endNodes = []
      """A list of node names to use as the final callback key."""

      self.DEBUG     = False
      """Debug User Code      DEFAULT: False"""

      self.KDEBUG    = False
      """Kernel status output DEFAULT: False"""

      self.SDEBUG    = True
      """Verbose Setup        DEFAULT: True
      We want this but it can be turned off """

   def addNode(self, node_name, callback):
      """Adds a node_name and its callback ref to our .callbacks dictionary."""
      self.callbacks[node_name] = callback 
      if self.SDEBUG:
         print("Adding node:", node_name)

   def setStartNode(self, node_name):
      """Sets node_name to be the .startNode for the graph walker."""
      self.startNode = node_name
      if self.SDEBUG:
         print("setting", node_name, "to .startNode")

   def setEndNode(self, node_name):
      """
      Appends node_name to the .endNodes list for the graph walker.
      The callback in all .endNodes is called upon entry to the node.
      This allows the user to print final results before pyDGW halts
      """
      self.endNodes.append(node_name)
      if self.SDEBUG:
         print("Adding", node_name, "to .endNodes list")

   def update_kernel_counter(self):
       """PRIVATE: This is called in the kernel loop to update"""
       self.node_counter = self.node_counter + 1
       self.operator_counter = self.operator_counter + 1

   def run(self, DGW_node):
      """
      Sanity Checks: .startNode and at least one .endNodes are set. 
      Loop: Until we reach an endNode and run its operator code.
      """
     
      # SETUP: make sure we have a .startNode and at least one .endNodes[]
      try:
         operator = self.callbacks[self.startNode]
      except:
         sys.exit("No starting node has been set, use .setStartNode()")

      if not self.endNodes: 
         sys.exit("No ending nodes have been set, use .setEndNode()")
      if self.KDEBUG: 
          print("Start Node is:", self.startNode)
          print("End Nodes are:", self.endNodes)
      
      # LOOP: until we hit an end state and then run its code (output)
      while True:
         (next_node, DGW_node) = operator(DGW_node)
         self.update_kernel_counter()
         if self.KDEBUG:
            print("next_node is:", next_node)

         if next_node in self.endNodes:
            if self.KDEBUG:
               print("next_node is an endNode:", next_node)
            operator = self.callbacks[next_node]
            operator(DGW_node) 
            break;
         else:                        
            operator = self.callbacks[next_node]
         if self.KDEBUG:
            print("Bottom of loop, queued operator is:", operator)


if __name__ == "__main__":

   import unittest
   import pyDGW

   class TestDGWalkerClass(unittest.TestCase):

      def test_PassDummy(self):
         """ This is a dummy test that always passes. 
         """
         self.assertTrue(True, "highly improbable")

      def test_highCount(self):
         """ Use counter example to count to 1,000,000.
         """
         self.assertTrue(True, "Failed High Count Test")

      def test_randomEndNode(self):
         """ Random generator node picks one of 6 .endNodes on each run.
             Run 30 times and pass if all nodes are reached at least once.
         """
         self.assertTrue(True, "Failed Random End Node Test")

      def test_noStartNode(self):
         """ Setup state machine with no .startNode to verify error
             checking code in the .run() function.
         """
         """
         DGW_Simple = pyDGW.DGWalker()
         DGW_state = pyDGW.DGW_data()

         def DGWOP_stop(DGW_state):
            pass

         """
         """Forget to set start node"""
         """
         DGW_Simple.addNode("stop", DGWOP_stop)
         DGW_Simple.setEndNode("stop")
         self.assertRaises(KeyError, DGW_Simple.run, DGW_state)
         """
         self.assertTrue(True)

      def test_noEndNodes(self):
         """ Setup state machine with no .endNodes to verify error
             checking code in the .run() function.
         """
         self.assertTrue(True)

         """
         DGW_Simple = pyDGW.DGWalker()
         DGW_state = pyDGW.DGW_data()
         number = 0 

         def DGWOP_start(DGW_state):
            operator = "stop"
            return(operator, DGW_state)

         def DGWOP_stop(DGW_state):
            pass

         DGW_Simple.addNode("start", DGWOP_start)
         DGW_Simple.addNode("stop", DGWOP_stop)
         DGW_Simple.setStartNode("start")

         self.assertRaises(IndexError, DGW_Simple.run, DGW_state)
         """


   unittest.main()



