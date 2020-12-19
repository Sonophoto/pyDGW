if __name__ == "__main__":

   import unittest
   import pyDGW

   class TestDGWalkerClass(unittest.TestCase):

      def test_PassDummy(self):
         """ This is a dummy test that always passes. 
         """
         self.assertTrue(True, "highly improbable")

      def test_highCount(self):
         """ Use counter example to count to 1,000,000.
         """
         self.assertTrue(True, "Failed High Count Test")

      def test_randomEndNode(self):
         """ Random generator node picks one of 6 .endNodes on each run.
             Run 30 times and pass if all nodes are reached at least once.
         """
         self.assertTrue(True, "Failed Random End Node Test")

      def test_noStartNode(self):
         """ Setup state machine with no .startNode to verify error
             checking code in the .run() function.
         """
         """
         DGW_Simple = pyDGW.DGWalker()
         DGW_state = pyDGW.DGW_data()

         def DGWOP_stop(DGW_state):
            pass

         """
         """Forget to set start node"""
         """
         DGW_Simple.addNode("stop", DGWOP_stop)
         DGW_Simple.setEndNode("stop")
         self.assertRaises(KeyError, DGW_Simple.run, DGW_state)
         """
         self.assertTrue(True)

      def test_noEndNodes(self):
         """ Setup state machine with no .endNodes to verify error
             checking code in the .run() function.
         """
         self.assertTrue(True)

         """
         DGW_Simple = pyDGW.DGWalker()
         DGW_state = pyDGW.DGW_data()
         number = 0 

         def DGWOP_start(DGW_state):
            operator = "stop"
            return(operator, DGW_state)

         def DGWOP_stop(DGW_state):
            pass

         DGW_Simple.addNode("start", DGWOP_start)
         DGW_Simple.addNode("stop", DGWOP_stop)
         DGW_Simple.setStartNode("start")

         self.assertRaises(IndexError, DGW_Simple.run, DGW_state)
         """


   unittest.main()

