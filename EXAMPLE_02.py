""" Silly but very clear example of how to use the library to create a state machine"""

import pyDGW

DGW_Counter = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
DGW_state.count = 0
DGW_state.limit = 1000

# Set to True to get debugging output from the graph walker 
DGW_Counter.DEBUG = False 

def DGWOP_start(DGW_state):
   """Our start state initializes DGW_state.count = 0"""
   DGW_state.count = 0
   operator = "counter"
   return(operator, DGW_state)


def DGWOP_counter(DGW_state):
   """Our counter increments while .count < .limit"""
   if DGW_state.count < DGW_state.limit:
      DGW_state.count = DGW_state.count + 1
      print("Counter has reached:", DGW_state.count)
      operator = "counter"
   if DGW_state.count == DGW_state.limit:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_stop(DGW_state):
   """Exits the state machine and prints our count""" 
   print("We have reached", DGW_state.count)

DGW_Counter.addNode("start", DGWOP_start)
DGW_Counter.addNode("counter", DGWOP_counter)
DGW_Counter.addNode("stop", DGWOP_stop)
DGW_Counter.setStartNode("start")
DGW_Counter.setEndNode("stop")
DGW_Counter.run(DGW_state)


