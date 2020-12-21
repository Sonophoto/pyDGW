"""
*************************************************************************
         ____      _        ___            _____ ____  __  __ 
        / ___|___ (_)_ __  / _ \ _ __     |  ___/ ___||  \/  |
       | |   / _ \| | '_ \| | | | '_ \    | |_  \___ \| |\/| |
       | |__| (_) | | | | | |_| | |_) |   |  _|  ___) | |  | |
        \____\___/|_|_| |_|\___/| .__/    |_|   |____/|_|  |_|
                                |_|                           

   FILENAME:  CoinOpExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements a state machine simulating a Vending Machine"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************

   In this simulation of a Soda Vending Machine we are going all out to 
   implemement a machine that tracks soda inventory, sales, and
   individual coin counts. While this is still a "trivial" model, it
   helps us to learn how to use state machines in combination with
   regular imperative code. This model is not that far from a finished
   machine and has more features than any OG vending machine.

   TODO: Overview of Model

   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   This example goes further by showing how a python module can hide
   the complexities of abstract code (THe FSM implementation) from the
   code needed to implement the vending machine model.

   NOTE: all of the logic of handling the state machine is essentially
   invisible, we don't have to think about the mechanics at all.
   All of the logic we do see is the implementation of our solution in
   our operator nodes, with each node responsible for:

       1. modifying the problem's state variable DGW_state
       2. choosing the next ooperator
       3. calling that operator and passing along DGW_state

   So sketch out the nodes in your machine, write-up logic for each node, 
   and connect them together with pyDGW.DGWalker

   I hope this code encourages you to play with and learn more about 
   Finite State Machines AKA Directed Graph Walkers.

"""

import datetime as dt
import pyDGW

DGW_CoinOp = pyDGW.DGWalker()

DGW_CoinOp.DEBUG = False      # User debug watches for user code
DGW_CoinOp.KDEBUG = False     # Kernel debug watches from pyDGW
DGW_CoinOp.SDEBUG = False     # Verbose operating messages from pyDGW

CoinOp_state = pyDGW.DGW_data()
CoinOp_state.tender_total = 0
CoinOp_state.soda_sales_total = 0
CoinOp_state.rootbeer_sales_total = 0
CoinOp_state.grape_sales_total = 0
CoinOp_state.orange_sales_total = 0
CoinOp_state.cola_sales_total = 0
CoinOp_state.nickels_total = 0
CoinOp_state.dimes_total = 0
CoinOp_state.quarters_total = 0
CoinOp_state.rootbeer_inventory = 0
CoinOp_state.grape_inventory = 0
CoinOp_state.orange_inventory = 0
CoinOp_state.orange_inventory = 0
CoinOp_state.soda_price = 0
CoinOp_state.change_due = 0


def OP_start(CoinOp_state):
   print("\nSoda Machine power is ON, initializing...")
   print("Type 'shutdown' at any input to shutdown Soda Machine")
   print("Type 'restock' at any input to restock Soda Machine")
   print("Type 'report' at any input to to get sales report")
   return("accept_coins", CoinOp_state)

def OP_accept_coins(CoinOp_state):
   print("\nWelcome to the pyDGW Soda Machine!")
   print("Enter 'nickel' or 'dime' or 'quarter' to pay")
   print("Enter 'refund' to get your coins back")
   print("Enter 'restock' or 'report' or 'shutdown' to admin")
   commandline = input()
   return("dispense", CoinOp_state)         

def OP_dispense(CoinOp_state):
   print("\nThank You for your business!")
   print("Enter 'rootbeer' or 'grape' or 'orange' to vend")
   return("stop", CoinOp_state) 

def OP_refund(CoinOp_state):
   pass

def OP_restock(CoinOp_state):
   pass

def OP_report(CoinOp_state):
   pass

def OP_stop(CoinOp_state):
   print("\nSoda Machine has shutdown: GoodBye!")

# Now we build our DGW_CoinOp object from these parts and run it:

DGW_CoinOp.DEBUG = True
DGW_CoinOp.addNode("start", OP_start)
DGW_CoinOp.addNode("accept_coins", OP_accept_coins)
DGW_CoinOp.addNode("dispense", OP_dispense)
DGW_CoinOp.addNode("refund", OP_refund)
DGW_CoinOp.addNode("restock", OP_restock)
DGW_CoinOp.addNode("report", OP_report)
DGW_CoinOp.addNode("stop", OP_stop)
DGW_CoinOp.setStartNode("start")
DGW_CoinOp.setEndNode("stop")
DGW_CoinOp.run(CoinOp_state)
