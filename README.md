# pyDGW
***A class that implements a basic state machine for walking Directed State Graphs***

Maintains a dict of nodes in a graph with callback functions that define
the edges and possible transistions from one node to the next. Maintains a
DGW_data object that is passed from node to node as the current system state.
pyDGW implements methods for adding nodes, setting nodes to be ending or
starting nodes, and then walking thru the nodes by calling the callback
function of each node it enters beginning with the start node until it enters
an end node.

Programming a state machine is not documented here. You need data that you 
use to keep track of your state and to process; you need a function for each
node that manipulates that data according to rules _YOU_ define and decides 
which state to move to next.

Usage:

1. Instantiate a DGW_data object and a DGW object.

2. Define your DGW_data object with state information fields.

3. Write an operator function for each node in your system.
      it should take a DGW_data object and return a list with next_node and DGW_data
      [[ prototype: (next_node, DGW_data) functionName(DGW_data) ]]

4. Call .addNode(node_name, callback_name) for each node in the system

5. Call .startNode(node_name) to set your system's start node

6. Call .endNode(node_name) to add endNodes to your system

7. Call .run(DWG_data)
