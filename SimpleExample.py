"""
*************************************************************************   
       ____  _                 _          _____ ____  __  __ 
      / ___|(_)_ __ ___  _ __ | | ___    |  ___/ ___||  \/  |
      \___ \| | '_ ` _ \| '_ \| |/ _ \   | |_  \___ \| |\/| |
       ___) | | | | | | | |_) | |  __/   |  _|  ___) | |  | |
      |____/|_|_| |_| |_| .__/|_|\___|   |_|   |____/|_|  |_|
                        |_|                                

   FILENAME:  SimpleExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements the simplest possible FSM, Extra Comments"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************   
"""

import pyDGW                             # Import the pyDGW module

# First we create the state variable that we pass around. 
# This is a trivial example but important

Simple_state = pyDGW.DGW_data()          # Instatiate a DGW_data object
Simple_state.the_answer = 0              # Extend Simple_state with data members 

# Next we create the Graph Walker object that will hold our state methods

DGW_Simple = pyDGW.DGWalker()            # Instantiate a DGWalker object

# Next we define the operator functions for each state in our state machine
# We use logic in each operator to determine which edge we will follow when
# we change state. # An operator could contain another state machine.

def OP_start(Simple_state):              # A Start Node is required
   """Our start state"""                 # Optional Docstring
   print("Entering the start node")      # Optional messaging
   Simple_state.the_answer = 1           # Do something to change data 
   if Simple_state.the_answer :          # Use logic to determine next state 
      operator = "stop"                  # operator is the next state
   print("Next Operator is:", operator)  # Optional messaging
   return(operator, Simple_state)        # Pass operator and modified state 
                                         # back to DGWalker which will load
                                         # and execute the next node.
def OP_stop(Simple_state):
   """Our stop state"""
   Simple_state.the_answer = 42        # Do any final processing at shutdown
   print("We have stopped")
   return(Simple_state)                # Returning our completed "output"

# Finally we use the methods of pyDGW to build our state machine and run it

DGW_Simple.DEBUG = True                # Setup any desired runtime options
DGW_Simple.addNode("start", OP_start)  # Add a callback for each state node
DGW_Simple.addNode("stop", OP_stop)
DGW_Simple.setStartNode("start")       # Define ONE starting node
DGW_Simple.setEndNode("stop")          # Define ONE or MORE ending nodes
DGW_Simple.run(Simple_state)           # Run the initialized graph walker


# Now you can do additional post processing on Simple_state, generate other
# output with matplotlib, and or format the information and print it on screen:
 
print("The Answer to Life, The Universe and Everything Is: ", Simple_state.the_answer)
