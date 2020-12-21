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

import pyDGW

DGW_FlipFlop = pyDGW.DGWalker()

FF_state = pyDGW.DGW_data()
FF_state.state = 0
FF_state.counter = 0
FF_state.limit = 10

# Set to True to get debugging output from the graph walker 
DGW_FlipFlop.KDEBUG = False 
# Set to True to use: "if DGW_FlipFlop.DEBUG: print()" for debugging
DGW_FlipFlop.DEBUG = True 
# Set to True to get operating status messages from pyDGW
DGW_FlipFlop.SDEBUG = False

def OP_start(FF_state):
   """Our start state initializes our flip flop"""
   print("Beginning FlipFlopping...")
   if DGW_FlipFlop.DEBUG: print("Count is: ", FF_state.counter)
   FF_state.state = 0
   operator = "flip"
   return(operator, FF_state)

def OP_flip(FF_state):
   """We are Flip, if toggled we flop"""
   if FF_state.counter == FF_state.limit: FF_state.state = 2
   if FF_state.state == 0:
      FF_state.state =  1
      FF_state.counter += 1
      operator = "flop"
      if DGW_FlipFlop.DEBUG:
         print("Flip is Flopping")
         print("Count is: ", FF_state.counter)
   if FF_state.state == 2:
      operator = "stop"
   return(operator, FF_state)

def OP_flop(FF_state):
   """We are Flop, if toggled we flip"""
   if FF_state.counter == FF_state.limit: FF_state.state = 2
   if FF_state.state == 1:
      FF_state.state =  0
      FF_state.counter += 1
      operator = "flip"
      if DGW_FlipFlop.DEBUG:
         print("Flop is Flipping")
         print("Count is: ", FF_state.counter)
   if FF_state.state == 2:
      operator = "stop"
   return(operator, FF_state)

def OP_stop(FF_state):
   """Exits the state machine, allows us to output data""" 
   print("We have executed ", FF_state.counter, " Flip Flops")

DGW_FlipFlop.addNode("start", OP_start)
DGW_FlipFlop.addNode("flip", OP_flip)
DGW_FlipFlop.addNode("flop", OP_flop)
DGW_FlipFlop.addNode("stop", OP_stop)
DGW_FlipFlop.setStartNode("start")
DGW_FlipFlop.setEndNode("stop")
DGW_FlipFlop.run(FF_state)


