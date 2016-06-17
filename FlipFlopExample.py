""" Silly but very clear example of how to use the library to create a state machine"""

import pyDGW

DGW_FlipFlop = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
DGW_state.state = 0
DGW_state.limit = 1000

# Set to True to get debugging output from the graph walker 
DGW_FlipFlop.KDEBUG = True
# Set to True to use: "if DGW_FlipFlop.DEBUG: print()" for debugging
DGW_FlipFlop.DEBUG = True 

def DGWOP_start(DGW_state):
   """Our start state initializes our flip flop"""
   print("Beginning FlipFlopping...")
   DGW_state.state = 0
   operator = "flip"
   return(operator, DGW_state)


def DGWOP_flip(DGW_state):
   """We are Flip, if toggled we flop"""
   if DGW_state.state == 0:
      DGW_state.state =  1
      operator = "flop"
      if DGW_FlipFlop.DEBUG:
         print("Flip is Flopping")
   if DGW_state.state == 2:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_flop(DGW_state):
   """We are Flop, if toggled we flip"""
   if DGW_state.state == 1:
      DGW_state.state =  0
      operator = "flip"
      if DGW_FlipFlop.DEBUG:
         print("Flop is Flipping")
   if DGW_state.state == 2:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_stop(DGW_state):
   """Exits the state machine""" 
   print("We have reached", DGW_state.state)

DGW_FlipFlop.addNode("start", DGWOP_start)
DGW_FlipFlop.addNode("flip", DGWOP_flip)
DGW_FlipFlop.addNode("flop", DGWOP_flop)
DGW_FlipFlop.addNode("stop", DGWOP_stop)
DGW_FlipFlop.setStartNode("start")
DGW_FlipFlop.setEndNode("stop")
DGW_FlipFlop.run(DGW_state)


