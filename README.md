![Tests](https://github.com/Sonophoto/pyDGW/actions/workflows/tests.yml/badge.svg)

# pyDGW
***A python3 module that implements a machine for defining and walking Directed State Graphs***

What is a directed Graph? It is a mathematical object: [wikipedia on Directed Graphs](https://en.wikipedia.org/wiki/Directed_graph)

pyDGW implements methods for creating directed graphs. These methods include 
adding graph nodes, setting graph nodes to be starting or ending graph nodes, 
and then initiating a walk thru the graph nodes which continues by calling user
specified callback functions in each node beginning with the start node and
running until it enters an end node. pyDGW also specifies a DGW_data object
that is passed along from node to node as the current system state changes.
This allows the user to keep track of the user's application data and generate
final output.

Directed Graphs can be used to understand and simulate Finite State Machines (FSM).

Designing and programming a finite state machine is not documented here. You 
will need data that you use to keep track of your state or "status" and data to
process; you will need a function for each state/node that manipulates that data
according to rules you define and decides which state/node to move to next.

Wikipedia has a [basic article on state machines](https://en.wikipedia.org/wiki/Finite-state_machine)
that is not too technical and includes a turnstyle example.

MIT OpenCourseWare has [a more technical article on state machines](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/unit-1-software-engineering/state-machines/MIT6_01SCS11_chap04.pdf).

Also Note: If you are going to use FSMs you must understand [The Pumping Lemma](https://codeinjection.blogspot.com/2011/02/pumping-lemma-and-why-its-slightly-more.html), Be sure to read the discussion below the article.


## Usage:

1. Instantiate a DGW_data object and a DGWalker object.

2. Define your DGW_data object with state information fields.

3. Write an operator function for each node in your system.
      it should take a DGW_data object and return a list with next_node and DGW_data
      [[ prototype: (next_node, DGW_data) operatorFunctionName(DGW_data) ]]

4. Call .addNode(node_name, callback_name) for each node in the system

5. Call .startNode(node_name) to set your system's start node

6. Call .endNode(node_name) to add endNodes to your system

7. Call .run(DGW_data)

## Tutorials:
See [Simple Example](https://github.com/Sonophoto/pyDGW/blob/master/SimpleExample.py)
for a heavily commented example you can use to start hacking away.

See [Counter Example](https://github.com/Sonophoto/pyDGW/blob/master/CounterExample.py)
and [FlipFlop Example](https://github.com/Sonophoto/pyDGW/blob/master/FlipFlopExample.py)
for slightly more involved usages of pyDGW that use data values to control execution.

See [Turnstyle Example](https://github.com/Sonophoto/pyDGW/blob/master/TurnstyleExample.py)
For a more detailed example that takes user input with 5 states and start-up/shutdown code.

See [CoinOp Example](https://github.com/Sonophoto/pyDGW/blob/master/CoinOpExample.py)
For an even more detailed example with 7 states, closer to a real world machine.

## Troubleshooting:

To help when debugging your code, system messages about what pyDGW is doing can be a big help:

      (YourObjectName).SDEBUG = True      # Default is True so pyDGW will use verbose messaging

To see what the kernel is doing internally (could be hundreds or thousands of message in one run):

      (YourObjectName).KDEBUG = True      # Default is "False"

To setup debugging messages for your own code use this:

      (YourObjectName).DEBUG = True       # Default is "False"
      
then add message lines like the following as needed in the code in your nodes

      if (YourObjectName).DEBUG: print("debugging info:", var_to_watch)

[Read the modules code and comments for more details](https://github.com/Sonophoto/pyDGW/blob/master/pyDGW.py)

If you think you have found a bug, PLEASE let me know by filing an issue here: [Report Bugs or Request Improvements](https://github.com/Sonophoto/pyDGW/issues)
