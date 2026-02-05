"""
  ____                  _                _____ ____  __  __ 
 / ___|___  _   _ _ __ | |_ ___ _ __    |  ___/ ___||  \/  |
| |   / _ \| | | | '_ \| __/ _ \ '__|   | |_  \___ \| |\/| |
| |__| (_) | |_| | | | | ||  __/ |      |  _|  ___) | |  | |
 \____\___/ \__,_|_| |_|\__\___|_|      |_|   |____/|_|  |_|

   FILENAME:  CounterExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements a dead simple 3 state FSM"
   COPYRIGHT: "Copyright 2016-2026 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************   
"""
import pyDGW

# Setup your state variables
counter_state = pyDGW.DGW_data()
counter_state.count = 0
counter_state.limit = 10

# Instatiate a Directed Graph Walker object
DGW_Counter = pyDGW.DGWalker()

# Set to True to get debugging output from the graph walker 
DGW_Counter.DEBUG = True

# Define your operators
def OP_start(counter_state):
   """Our start state initializes counter_state.count = 0"""
   counter_state.count = 0
   operator = "counter"
   return(operator, counter_state)

def OP_counter(counter_state):
   """Our counter increments while .count < .limit"""
   if counter_state.count < counter_state.limit:
      counter_state.count += 1
      print("Counter has reached:", counter_state.count)
      operator = "counter"
   if counter_state.count == counter_state.limit:
      operator = "stop"
   return(operator, counter_state)

def OP_stop(counter_state):
   """Exits the state machine and prints our count"""
   print("We have reached", counter_state.count)

# Configure your Directed Graph Walker with your operators
# and run it to completion
DGW_Counter.addNode("start", OP_start)
DGW_Counter.addNode("counter", OP_counter)
DGW_Counter.addNode("stop", OP_stop)
DGW_Counter.setStartNode("start")
DGW_Counter.setEndNode("stop")
DGW_Counter.run(counter_state)

""" You can do additional processing on your DGW_state object here 
    after your state machine has shut down
"""
