"""
*************************************************************************
  _____                     _         _        _____ ____  __  __ 
 |_   _|   _ _ __ _ __  ___| |_ _   _| | ___  |  ___/ ___||  \/  |
   | || | | | '__| '_ \/ __| __| | | | |/ _ \ | |_  \___ \| |\/| |
   | || |_| | |  | | | \__ \ |_| |_| | |  __/ |  _|  ___) | |  | |
   |_| \__,_|_|  |_| |_|___/\__|\__, |_|\___| |_|   |____/|_|  |_|
                               |___/                             
       "Around and Around it goes, but if you don't pay: ALARM!"

   FILENAME:  TurnstyleExample.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Implements a state machine simulating a Turnstyle"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************

   Fairly complete example of a Turnstyle that:

       * Has a startup and initialization state
       * Accepts one token to allow you through
       * Accepts additional tokens as donations
       * Triggers an alarm if you pass without paying
       * Keeps track of how many tokens have been paid
       * Generates a report when shutdown
       * Is fairly robust against nonsensical inputs

   This is a much more complete example than the simple counter and 
   flip/flop and takes user input to decide how to change state.

   A turn style accepts tokens, can lock and unlock itself, and triggers an
   alarm if you jump over it (by typing 'pass' without typing 'token' first)
   Finally when we shutdown we generate a small report on the machine.

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

DGW_Turnstyle = pyDGW.DGWalker()

DGW_Turnstyle.DEBUG = False      # User debug watches for user code
DGW_Turnstyle.KDEBUG = False     # Kernel debug watches from pyDGW
DGW_Turnstyle.SDEBUG = False     # Verbose operating messages from pyDGW

DGW_state = pyDGW.DGW_data()
DGW_state.alarm_status = 0
DGW_state.token_total = 0
DGW_state.pass_total = 0
DGW_state.alarm_total = 0


def OP_start(DGW_state):
   print("\nTurnstyle power is ON, initializing...")
   print("Type 'shutdown' at any input to shutdown Turnstyle")
   DGW_state.alarm_status = 0 
   return("accept_token", DGW_state)

def OP_accept_token(DGW_state):
   print("\nWelcome to the pyDGW Turnstyle!")
   print("Enter 'pass' to go through the turnstyle")
   print("Enter 'token' to insert a token")
   commandline = input()
   if "pass" in commandline:
      DGW_state.alarm_status = 1
      DGW_state.pass_total += 1              # UNPAID PASS
      return("alarm", DGW_state)
   if "token" in commandline:
      DGW_state.token_total += 1
      return("unlock", DGW_state)
   if "shutdown" in commandline:
      return("stop", DGW_state)
   #else ignore bad input
   print("We are sorry, please try again...")
   return("accept_token", DGW_state)         

def OP_unlock(DGW_state):
   print("\nThank You for your business!")
   print("please enter 'pass' to go through the turnstyle")
   print("enter 'token' to donate additional tokens")
   commandline = input()
   if 'token' in commandline:
      print("Thanks for the tip!")
      DGW_state.token_total += 1            # DONATION
      return("unlock", DGW_state)
   if 'pass' in commandline:
      print("Have a safe Trip!")
      DGW_state.pass_total += 1              # PAID PASS
      return("accept_token", DGW_state)
   if "shutdown" in commandline:
      return("stop", DGW_state)
   #else ignore bad input
   print("We are sorry, please try again...")
   return("unlock", DGW_state)

def OP_alarm(DGW_state):
   DGW_state.alarm_total += 1
   _soundAlarm()
   commandline = input()
   if "password" in commandline:
      return('start', DGW_state)
   if "shutdown" in commandline:
      DGW_state.alarm_status = 0
      return('stop', DGW_state)
   #else ignore bad input and stop
   return('stop', DGW_state)

def OP_stop(DGW_state):
   if DGW_state.alarm_status:
      _soundBadPassword() 
   print("\nOperations Report for: ", dt.date.today().ctime())
   print("-------------------------------------------------")
   print(" Total Sales: ", DGW_state.token_total)     
   print("Total Passes: ", DGW_state.pass_total)
   print("Total Alarms: ", DGW_state.alarm_total)
   if DGW_state.pass_total != 0:
      print(" Tokens/Pass: ", DGW_state.token_total / DGW_state.pass_total)
   else:
      print(" Tokens/Pass: Not applicable")
   print("-------------------------------------------------")
   print("\nTurnstyle power is OFF, Goodbye\n")
   return(DGW_state)

# Lets wrap our alarm notifications to unclutter our code:

def _soundAlarm():
   print("\n************************************************")
   print("  ALARM! A Trespasser Has Jumped The Turnstyle!")
   print("************************************************")
   print("please type 'password' to clear the alarm")

def _soundBadPassword():
   print("\n***********************************************")
   print("  BAD PASSWORD! Attempted Unauthorized Access!")
   print("***********************************************")

# Now we build our DGW_Turnstyle object from these parts and run it:

DGW_Turnstyle.DEBUG = True
DGW_Turnstyle.addNode("start", OP_start)
DGW_Turnstyle.addNode("accept_token", OP_accept_token)
DGW_Turnstyle.addNode("unlock", OP_unlock)
DGW_Turnstyle.addNode("alarm", OP_alarm)
DGW_Turnstyle.addNode("stop", OP_stop)
DGW_Turnstyle.setStartNode("start")
DGW_Turnstyle.setEndNode("stop")
DGW_Turnstyle.run(DGW_state)

