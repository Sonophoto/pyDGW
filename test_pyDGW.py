"""
*************************************************************************
   Testing Harness for pyDGW

   FILENAME:  test_pyDGW.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Runs test on pyDGW for Quality Assurance"
   COPYRIGHT: "Copyright 2016-2020 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************
"""

import unittest
import pyDGW

class TestDGWalkerClass(unittest.TestCase):

  def test_PassDummy(self):
     """ This is a dummy test that always passes.
     """
     print("\nPassing the dummy test")
     self.assertTrue(True, "highly improbable")

  def test_noStartNode(self):
     """ Setup state machine with no .startNode to verify that .run()
         will trigger a SystemExit exception
     """
     print("\nTesting with a missing start node")
     NoStartNodeTest = pyDGW.DGWalker()
     no_start_node_state = pyDGW.DGW_data()

     def OP_stop(no_start_node_state):
        pass

     """Forget to set start node"""
     NoStartNodeTest.addNode("stop", OP_stop)
     NoStartNodeTest.setEndNode("stop")

     """If there is no start node set the library should force exit."""
     self.assertRaises(SystemExit, NoStartNodeTest.run, no_start_node_state)

  def test_noEndNode(self):
     """ Setup state machine with no .endNodes to verify that .run()
         will trigger a SystemExit exception
     """
     print("\nTesting with a missing end node")
     NoEndNodeTest = pyDGW.DGWalker()
     no_end_node_state = pyDGW.DGW_data()

     def OP_start(no_end_node_state):
        pass

     """Forget to set an end node"""
     NoEndNodeTest.addNode("start", OP_start)
     NoEndNodeTest.setStartNode("start")

     """If there is no end node(s) set the library should force exit."""
     self.assertRaises(SystemExit, NoEndNodeTest.run, no_end_node_state)

  def test_highCount(self):
     """ Simple counter counts to 10,00O using a 3 state machine
         with a start node, a worker node and an end node"
     """
     print("\nTesting a complete machine: HiCountTest")
     HiCountTest = pyDGW.DGWalker()

     hi_count_state = pyDGW.DGW_data()
     hi_count_state.count = 0
     hi_count_state.limit = 10000

     def OP_start(hi_count_state):
        hi_count_state.limit = 10000
        return("work", hi_count_state)

     def OP_work(hi_count_state):
         if hi_count_state.count < hi_count_state.limit:
             hi_count_state.count += 1
             return("work", hi_count_state)
         if hi_count_state.count == hi_count_state.limit:
             return("stop", hi_count_state)

     def OP_stop(hi_count_state):
         return(hi_count_state)

     HiCountTest.addNode("start", OP_start)
     HiCountTest.addNode("work", OP_work)
     HiCountTest.addNode("stop", OP_stop)
     HiCountTest.SDEBUG = False      # We only want to see the addNode messaging
     HiCountTest.setStartNode("start")
     HiCountTest.setEndNode("stop")
     HiCountTest.run(hi_count_state)

     """If the library works .count and .limit should now be equal"""
     self.assertEqual(hi_count_state.count, hi_count_state.limit)


unittest.main()

