"""Simplest example of a directed graph walker
   Copyright 2016, 2017 Brig Young, Sonophotostudios.com
   License: BSD-2c, (Citation Required) See LICENSE file
"""

import pyDGW

DGW_Simple = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
last_state = 0                            # This is our "state" or "status"

def DGWOP_start(DGW_state):
   """Our start state
   """
   print("We have entered start")         # Optional messaging
   DGW_state.last_state = 1               # Do something to change status
   if DGW_state.last_state :              # Use logic to determine next state 
      operator = "stop"

   print("Next Operator is:", operator)   # Optional messaging
   return(operator, DGW_state)            # Pass modified state back to DGWalker

def DGWOP_stop(DGW_state):
   """Our stop state
   """
   DGW_state.last_state = 42 
   print("We have stopped")
   return(DGW_state)                      # Returning our completed "output"


DGW_Simple.DEBUG = True                   # Setup any desired runtime options
DGW_Simple.addNode("start", DGWOP_start)  # Add a callback for each state node
DGW_Simple.addNode("stop", DGWOP_stop)
DGW_Simple.setStartNode("start")          # Define ONE starting node
DGW_Simple.setEndNode("stop")             # Define ONE or MORE ending nodes
DGW_Simple.run(DGW_state)                 # Run the initialized graph walker


# Now you can do additional processing on DGW_state, generate other output
# with matplotlib, and or format the information and print it on screen:
 
print("The Answer Is: ", DGW_state.last_state)
