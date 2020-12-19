""" Silly but very clear example of how to use the library to create a state machine"""

import pyDGW

DGW_Counter = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
DGW_state.count = 0
DGW_state.limit = 20

# Set to True to get debugging output from the graph walker 
DGW_Counter.DEBUG = True

def DGWOP_start(DGW_state):                               # Create a Start state that initializes
   """Our start state initializes DGW_state.count = 0"""  # your state machine with data.
   DGW_state.count = 0
   operator = "counter"
   return(operator, DGW_state)


def DGWOP_counter(DGW_state):                             # Add nodes that process your data and
   """Our counter increments while .count < .limit"""     # determine the next node to move to
   if DGW_state.count < DGW_state.limit:
      DGW_state.count += 1
      print("Counter has reached:", DGW_state.count)
      operator = "counter"
   if DGW_state.count == DGW_state.limit:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_stop(DGW_state):                                # Add one or more end nodes that do
   """Exits the state machine and prints our count"""     # final processing on your data and
   print("We have reached", DGW_state.count)              # generate output on your display

DGW_Counter.addNode("start", DGWOP_start)                 # Finally use methods from the DGWalker
DGW_Counter.addNode("counter", DGWOP_counter)             # class to setup the machinery for your 
DGW_Counter.addNode("stop", DGWOP_stop)                   # state machine and run it
DGW_Counter.setStartNode("start")
DGW_Counter.setEndNode("stop")
DGW_Counter.run(DGW_state)

""" You can do additional processing on your DGW_state object here 
    after your state machine has shut down
"""
