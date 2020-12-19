"""
*************************************************************************   
 ____  _                 _        _____ ____  __  __ 
/ ___|(_)_ __ ___  _ __ | | ___  |  ___/ ___||  \/  |
\___ \| | '_ ` _ \| '_ \| |/ _ \ | |_  \___ \| |\/| |
 ___) | | | | | | | |_) | |  __/ |  _|  ___) | |  | |
|____/|_|_| |_| |_| .__/|_|\___| |_|   |____/|_|  |_|
                  |_|                                

   FILENAME:  SimpleExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements the simplest possible state machine"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************   
"""

import pyDGW                              # Import the pyDGW module

DGW_Simple = pyDGW.DGWalker()             # Instantiate a DGWalker object

DGW_state = pyDGW.DGW_data()              # Instatiate a DGW_data object
DGW_state.the_answer = 0                  # Extend DGW_state with data members 

def DGWOP_start(DGW_state):               # A Start Node is required
   """Our start state"""                  # Optional Docstring
   print("Entering the start node")       # Optional messaging
   DGW_state.the_answer = 1               # Do something to change data 
   if DGW_state.the_answer :              # Use logic to determine next state 
      operator = "stop"                   # operator is the next state
   print("Next Operator is:", operator)   # Optional messaging
   return(operator, DGW_state)            # Pass operator and modified state 
                                          # back to DGWalker which will load
                                          # and execute the next node.

def DGWOP_stop(DGW_state):
   """Our stop state"""
   DGW_state.the_answer = 42              # Do any final processing at shutdown
   print("We have stopped")               
   return(DGW_state)                      # Returning our completed "output"


DGW_Simple.DEBUG = True                   # Setup any desired runtime options
DGW_Simple.addNode("start", DGWOP_start)  # Add a callback for each state node
DGW_Simple.addNode("stop", DGWOP_stop)
DGW_Simple.setStartNode("start")          # Define ONE starting node
DGW_Simple.setEndNode("stop")             # Define ONE or MORE ending nodes
DGW_Simple.run(DGW_state)                 # Run the initialized graph walker


# Now you can do additional post processing on DGW_state, generate other output
# with matplotlib, and or format the information and print it on screen:
 
print("The Answer to Life, The Universe and Everything Is: ", DGW_state.the_answer)
