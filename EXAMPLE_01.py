"""Simplest example of a directed graph walker"""

import pyDGW

DGW_Simple = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
number = 0 

def DGWOP_start(DGW_state):
   """Our start state initializes DGW_state.count = 1"""
   print("We have reached The Beginning")
   DGW_state.number = 1
   operator = "stop"
   print("State Number is now:", DGW_state.number)
   print("Next Operator is:", operator)
   return(operator, DGW_state)

def DGWOP_stop(DGW_state):
   """Exits the state machine and prints a message""" 
   print("We have reached The End")

DGW_Simple.DEBUG = True
DGW_Simple.addNode("start", DGWOP_start)
DGW_Simple.addNode("stop", DGWOP_stop)
DGW_Simple.setStartNode("start")
DGW_Simple.setEndNode("stop")
DGW_Simple.run(DGW_state)


