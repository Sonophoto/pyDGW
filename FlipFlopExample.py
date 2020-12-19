"""
*************************************************************************
 _____ _ _          ____    _____ _               _____ ____  __  __ 
|  ___| (_)_ __    / /\ \  |  ___| | ___  _ __   |  ___/ ___||  \/  |
| |_  | | | '_ \  / /  \ \ | |_  | |/ _ \| '_ \  | |_  \___ \| |\/| |
|  _| | | | |_) | \ \  / / |  _| | | (_) | |_) | |  _|  ___) | |  | |
|_|   |_|_| .__/   \_\/_/  |_|   |_|\___/| .__/  |_|   |____/|_|  |_|
          |_|                            |_|                         

   FILENAME:  FlipFlopExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements a simple bistable flip flop with a limit"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************   
"""

""" Silly but very clear example of how to use the library to create a state machine"""

import pyDGW

DGW_FlipFlop = pyDGW.DGWalker()

DGW_state = pyDGW.DGW_data()
DGW_state.state = 0
DGW_state.counter = 0
DGW_state.limit = 20

# Set to True to get debugging output from the graph walker 
DGW_FlipFlop.KDEBUG = False 
# Set to True to use: "if DGW_FlipFlop.DEBUG: print()" for debugging
DGW_FlipFlop.DEBUG = True 
# Set to True to get operating status messages from pyDGW
DGW_FlipFlop.SDEBUG = False

def DGWOP_start(DGW_state):
   """Our start state initializes our flip flop"""
   print("Beginning FlipFlopping...")
   if DGW_FlipFlop.DEBUG: print("Count is: ", DGW_state.counter)
   DGW_state.state = 0
   operator = "flip"
   return(operator, DGW_state)


def DGWOP_flip(DGW_state):
   """We are Flip, if toggled we flop"""
   if DGW_state.counter == DGW_state.limit: DGW_state.state = 2
   if DGW_state.state == 0:
      DGW_state.state =  1
      DGW_state.counter += 1
      operator = "flop"
      if DGW_FlipFlop.DEBUG:
         print("Flip is Flopping")
         print("Count is: ", DGW_state.counter)
   if DGW_state.state == 2:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_flop(DGW_state):
   """We are Flop, if toggled we flip"""
   if DGW_state.counter == DGW_state.limit: DGW_state.state = 2
   if DGW_state.state == 1:
      DGW_state.state =  0
      DGW_state.counter += 1
      operator = "flip"
      if DGW_FlipFlop.DEBUG:
         print("Flop is Flipping")
         print("Count is: ", DGW_state.counter)
   if DGW_state.state == 2:
      operator = "stop"
   return(operator, DGW_state)


def DGWOP_stop(DGW_state):
   """Exits the state machine, allows us to output data""" 
   print("We have executed ", DGW_state.counter, " Flip Flops")

DGW_FlipFlop.addNode("start", DGWOP_start)
DGW_FlipFlop.addNode("flip", DGWOP_flip)
DGW_FlipFlop.addNode("flop", DGWOP_flop)
DGW_FlipFlop.addNode("stop", DGWOP_stop)
DGW_FlipFlop.setStartNode("start")
DGW_FlipFlop.setEndNode("stop")
DGW_FlipFlop.run(DGW_state)


