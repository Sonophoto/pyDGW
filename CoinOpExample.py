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

   NOTE: For more advanced programmers this is a first level abstraction
         and for working code would need a refactor. I know this ;-) This
         is a teaching example so it is written this way so as not to 
         confuse less advanced students. Once they understand this we can 
         move on to passing around references more aggresively with an 
         aggresive refactoring pass. If it is not here when you read this:

                    Feel Free to PR and get credit <wink>
"""

import datetime as dt
import pyDGW

# Setup our data object
CoinOp_state = pyDGW.DGW_data()
CoinOp_state.tender_total = 0
CoinOp_state.soda_sales_total = 0
CoinOp_state.rootbeer_sales_total = 0
CoinOp_state.grape_sales_total = 0
CoinOp_state.orange_sales_total = 0
CoinOp_state.cola_sales_total = 0
CoinOp_state.rootbeer_inventory = 1
CoinOp_state.grape_inventory = 1
CoinOp_state.orange_inventory = 1
CoinOp_state.soda_price = 65 
CoinOp_state.change_due = 0

# Setup our DGWalker object
CoinOp = pyDGW.DGWalker()
CoinOp.DEBUG = False      # User debug watches for user code
CoinOp.KDEBUG = False     # Kernel debug watches from pyDGW
CoinOp.SDEBUG = False     # Verbose operating messages from pyDGW

# Next we define each of the states in our machine

def OP_start(CoinOp_state):
   print("\nSoda Machine power is ON, initializing...")
   print("Type 'shutdown' when idle to shutdown Soda Machine")
   print("Type 'restock' when idle to restock Soda Machine")
   print("Type 'report' when idle to to get sales report")
   return ("accept_coins", CoinOp_state)

def OP_accept_coins(CoinOp_state):
   print("\nWelcome to the pyDGW Soda Machine!")
   print("Sodas are ", CoinOp_state.soda_price, " cents")
   print("Enter 'nickel', 'dime', 'quarter' or 'dollar' to pay")
   print("Enter 'refund' to get your coins back")
   print("Enter 'report' to get report on operations")
   nickel, dime, quarter, dollar = 5, 10, 25, 100
   commandline = input()
   if 'nickel' in commandline:
      CoinOp_state.tender_total += nickel
      if CoinOp_state.tender_total >= CoinOp_state.soda_price:
         return ('dispense', CoinOp_state)
      else:
         return ('accept_coins', CoinOp_state)
   if 'dime' in commandline:
      CoinOp_state.tender_total += dime
      if CoinOp_state.tender_total >= CoinOp_state.soda_price:
         return ('dispense', CoinOp_state)
      else:
         return ('accept_coins', CoinOp_state)
   if 'quarter' in commandline:
      CoinOp_state.tender_total += quarter 
      if CoinOp_state.tender_total >= CoinOp_state.soda_price:
         return ('dispense', CoinOp_state)
      else:
         return ('accept_coins', CoinOp_state)
   if 'dollar' in commandline:
      CoinOp_state.tender_total += dollar 
      if CoinOp_state.tender_total >= CoinOp_state.soda_price:
         return ('dispense', CoinOp_state)
      else:
         return ('accept_coins', CoinOp_state)
   if 'refund' in commandline:
       return ('refund', CoinOp_state)
   if 'restock' in commandline:
       return ('restock', CoinOp_state)
   if 'report' in commandline:
       return ('report', CoinOp_state)
   if 'shutdown' in commandline:
       return ('stop', CoinOp_state)
   # malformed input, loop back
   return('accept_coins', CoinOp_state)

def OP_dispense(CoinOp_state):
   print("\nThank You for your business!")
   print("Enter 'rootbeer' or 'grape' or 'orange' to vend")
   commandline = input()
   if 'rootbeer' in commandline:
      if CoinOp_state.rootbeer_inventory > 0:
         CoinOp_state.tender_total -= CoinOp_state.soda_price
         CoinOp_state.soda_sales_total += CoinOp_state.soda_price
         CoinOp_state.rootbeer_sales_total += 1
         CoinOp_state.rootbeer_inventory -= 1
         print("\nHere is your cold rootbeer. Enjoy!")
         return ('refund', CoinOp_state)
      else:
         print("\nSorry! rootbeer is out of stock")
         return ('dispense', CoinOp_state)
   if 'grape' in commandline:
      if CoinOp_state.grape_inventory > 0:
         CoinOp_state.tender_total -= CoinOp_state.soda_price
         CoinOp_state.soda_sales_total += CoinOp_state.soda_price
         CoinOp_state.grape_sales_total += 1
         CoinOp_state.grape_inventory -= 1
         print("\nHere is your cold grape soda. Enjoy!")
         return ('refund', CoinOp_state)
      else:
         print("\nSorry! grape is out of stock")
         return ('dispense', CoinOp_state)
   if 'orange' in commandline:
      if CoinOp_state.orange_inventory > 0:
         CoinOp_state.tender_total -= CoinOp_state.soda_price
         CoinOp_state.soda_sales_total += CoinOp_state.soda_price
         CoinOp_state.orange_sales_total += 1
         CoinOp_state.orange_inventory -= 1
         print("\nHere is your cold orange soda. Enjoy!")
         return ('refund', CoinOp_state)
      else:
         print("\nSorry! orange is out of stock")
         return ('dispense', CoinOp_state)
   if 'refund' in commandline:
       return ('refund', CoinOp_state)
   # malformed input, loop back
   return('dispense', CoinOp_state)

def OP_refund(CoinOp_state):
   """We are using a 'trick' here. We just got the .tender_total value
      which has been decrimented by the cost of a soda if one was sold,
      or is the amount the customer has deposited so far: so either way
      anything remaining is change. Easy eh?
   """
   print("\nThank You! Your change is ", CoinOp_state.tender_total, " cents")
   # In a real machine we would release the coins here
   # History: In the old days this was a seperate rack of nickels
   CoinOp_state.tender_total = 0
   return('accept_coins', CoinOp_state)

def OP_restock(CoinOp_state):
   print("\nEnter soda name and count to restock")
   print("eg. rootbeer 6")
   soda_name, soda_count = "",0    # tuple assignment
   commandline = input() 
   # wrap this in a try/except
   (soda_name, soda_count) = commandline.split()
   if 'rootbeer' in soda_name:
       CoinOp_state.rootbeer_inventory += int(soda_count)
       return ('accept_coins', CoinOp_state) 
   if 'grape' in soda_name:
       CoinOp_state.grape_inventory += int(soda_count)
       return ('accept_coins', CoinOp_state) 
   if 'orange' in soda_name:
       CoinOp_state.orange_inventory += int(soda_count)
       return ('accept_coins', CoinOp_state) 
   # malformed input, loop back
   print("I'm sorry, that did not make sense, please try again")
   return ('restock', CoinOp_state)

def OP_report(CoinOp_state):
   _printReport(CoinOp_state)
   return ('accept_coins', CoinOp_state)

def OP_stop(CoinOp_state):
   print("\nSoda Machine has shutdown: GoodBye!")
   # Run the report state so we have a final report
   OP_report(CoinOp_state)
   return (CoinOp_state)

# Define our report output as a helper function
def _printReport(CoinOp_state):
   print("\n===========================================================")
   print("Operations report for", dt.date.today().ctime()) 
   print("\nSales Report:")
   print("Total Sodas Sold:", CoinOp_state.rootbeer_sales_total+\
                              CoinOp_state.grape_sales_total+\
                              CoinOp_state.orange_sales_total)
   print("Rootbeer Sales:", CoinOp_state.rootbeer_sales_total)
   print("Grape Soda Sales:", CoinOp_state.grape_sales_total)
   print("Orange Soda Sales:", CoinOp_state.orange_sales_total)
   print("\nSoda Inventory:")
   print("Rootbeer Inventory:", CoinOp_state.rootbeer_inventory)
   print("Grape Soda Inventory:", CoinOp_state.grape_inventory)
   print("Orange Soda Inventory:", CoinOp_state.orange_inventory)
   print("\nFinancial Report:")
   print("Soda Price:", CoinOp_state.soda_price)
   print("Total Cash in Machine:", CoinOp_state.soda_sales_total/100, "Dollars")
   print("===========================================================")
 
# Now we build our CoinOp object from these parts and run it:
CoinOp.DEBUG = True
CoinOp.addNode("start", OP_start)
CoinOp.addNode("accept_coins", OP_accept_coins)
CoinOp.addNode("dispense", OP_dispense)
CoinOp.addNode("refund", OP_refund)
CoinOp.addNode("restock", OP_restock)
CoinOp.addNode("report", OP_report)
CoinOp.addNode("stop", OP_stop)
CoinOp.setStartNode("start")
CoinOp.setEndNode("stop")
CoinOp.run(CoinOp_state)

# Generate a final report after the machine has shutdown
_printReport(CoinOp_state)
