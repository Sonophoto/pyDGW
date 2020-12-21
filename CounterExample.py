""" Silly but very clear example of how to use the library to create a state machine"""

import pyDGW

DGW_Counter = pyDGW.DGWalker()

counter_state = pyDGW.DGW_data()
counter_state.count = 0
counter_state.limit = 10

# Set to True to get debugging output from the graph walker 
DGW_Counter.DEBUG = True

def OP_start(counter_state):                               # Create a Start state that initializes
   """Our start state initializes counter_state.count = 0"""  # your state machine with data.
   counter_state.count = 0
   operator = "counter"
   return(operator, counter_state)


def OP_counter(counter_state):                             # Add nodes that process your data and
   """Our counter increments while .count < .limit"""     # determine the next node to move to
   if counter_state.count < counter_state.limit:
      counter_state.count += 1
      print("Counter has reached:", counter_state.count)
      operator = "counter"
   if counter_state.count == counter_state.limit:
      operator = "stop"
   return(operator, counter_state)


def OP_stop(counter_state):                                # Add one or more end nodes that do
   """Exits the state machine and prints our count"""     # final processing on your data and
   print("We have reached", counter_state.count)              # generate output on your display

DGW_Counter.addNode("start", OP_start)                 # Finally use methods from the DGWalker
DGW_Counter.addNode("counter", OP_counter)             # class to setup the machinery for your 
DGW_Counter.addNode("stop", OP_stop)                   # state machine and run it
DGW_Counter.setStartNode("start")
DGW_Counter.setEndNode("stop")
DGW_Counter.run(counter_state)

""" You can do additional processing on your DGW_state object here 
    after your state machine has shut down
"""
