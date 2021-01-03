[![Build Status](https://travis-ci.org/Sonophoto/pyDGW.svg?branch=master)](https://travis-ci.org/Sonophoto/pyDGW)

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
use to keep track of your state or "status" and data to process; you need a
function for each node that manipulates that data according to rules you
define and decides which state to move to next.

***Usage:***

1. Instantiate a DGW_data object and a DGWalker object.

2. Define your DGW_data object with state information fields.

3. Write an operator function for each node in your system.
      it should take a DGW_data object and return a list with next_node and DGW_data
      [[ prototype: (next_node, DGW_data) operatorFunctionName(DGW_data) ]]

4. Call .addNode(node_name, callback_name) for each node in the system

5. Call .startNode(node_name) to set your system's start node

6. Call .endNode(node_name) to add endNodes to your system

7. Call .run(DGW_data)

***Tutorials:***
See [Simple Example](https://github.com/Sonophoto/pyDGW/blob/master/SimpleExample.py)
for a heavily commented example you can use to start hacking away.

See [Counter Example](https://github.com/Sonophoto/pyDGW/blob/master/CounterExample.py)
and [FlipFlop Example](https://github.com/Sonophoto/pyDGW/blob/master/FlipFlopExample.py)
for slightly more involved usages of pyDGW that use data values to control execution.

See [Turnstyle Example](https://github.com/Sonophoto/pyDGW/blob/master/TurnstyleExample.py)
For a more detailed example that takes user input with 5 states and start-up/shutdown code.

See [CoinOp Example](https://github.com/Sonophoto/pyDGW/blob/master/CoinOpExample.py)
For an even more detailed example with 7 states, closer to a real world machine.

***Troubleshooting:***

To help when debugging your code, system messages about what pyDGW is doing can be a big help:

      (YourObjectName).SDEBUG = True      # Default is True so pyDGW will use verbose messaging

To see what the kernel is doing internally (could be hundreds or thousands of message in one run):

      (YourObjectName).KDEBUG = True      # Default is "False"

To setup debugging messages for your own code use this:

      (YourObjectName).DEBUG = True       # Default is "False"
      
then add message lines like the following as needed in the code in your nodes

      if (YourObjectName).DEBUG: print("debugging info:", var_to_watch)

[Read the modules code and comments for more details](https://github.com/Sonophoto/pyDGW/blob/master/pyDGW.py)

If you think you have found a bug PLEASE, let me know (File an Issue), I want this project to be perfect. Patches (PRs) are very welcome and will be added to your credit if correct.
