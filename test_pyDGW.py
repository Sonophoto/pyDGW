"""
*************************************************************************
   Testing Harness for pyDGW

   FILENAME:  test_pyDGW.py
   AUTHOR:    "Brig Young, https://github.com/Sonophoto/"
   PURPOSE:   "Runs test on pyDGW for Quality Assurance"
   COPYRIGHT: "Copyright 2016-2026 Brig Young, Sonophotostudios.com"
   LICENSE:   " BSD 2-Clause, (Citation Required) See LICENSE file"

*************************************************************************
"""

import unittest
import pyDGW


class TestDGWDataClass(unittest.TestCase):
    """Test the DGW_data base class."""

    def test_initialization(self):
        """Test that DGW_data can be instantiated."""
        state = pyDGW.DGW_data()
        self.assertIsInstance(state, pyDGW.DGW_data)

    def test_attribute_extension(self):
        """Test that DGW_data can be extended with custom attributes."""
        state = pyDGW.DGW_data()
        state.counter = 0
        state.name = "test"
        self.assertEqual(state.counter, 0)
        self.assertEqual(state.name, "test")

    def test_attribute_mutation(self):
        """Test that DGW_data attributes can be mutated."""
        state = pyDGW.DGW_data()
        state.value = 10
        state.value += 5
        self.assertEqual(state.value, 15)


class TestDGWalkerInitialization(unittest.TestCase):
    """Test DGWalker initialization and configuration."""

    def setUp(self):
        """Set up a fresh DGWalker instance for each test."""
        self.walker = pyDGW.DGWalker()
        self.walker.SDEBUG = False

    def test_initialization(self):
        """Test that DGWalker initializes with correct default values."""
        self.assertEqual(self.walker.operator_counter, 0)
        self.assertEqual(self.walker.node_counter, 1)
        self.assertIsNone(self.walker.startNode)
        self.assertEqual(self.walker.endNodes, [])
        self.assertEqual(self.walker.callbacks, {})

    def test_debug_flags_defaults(self):
        """Test that debug flags are initialized correctly."""
        walker = pyDGW.DGWalker()
        self.assertFalse(walker.DEBUG)
        self.assertFalse(walker.KDEBUG)
        self.assertTrue(walker.SDEBUG)

    def test_addNode(self):
        """Test that addNode correctly adds a node to the callbacks dictionary."""
        def test_callback(state):
            return ("next", state)
        
        self.walker.addNode("test_node", test_callback)
        self.assertIn("test_node", self.walker.callbacks)
        self.assertEqual(self.walker.callbacks["test_node"], test_callback)

    def test_addNode_multiple(self):
        """Test that multiple nodes can be added."""
        def callback1(state):
            return ("node2", state)
        
        def callback2(state):
            return ("end", state)
        
        self.walker.addNode("node1", callback1)
        self.walker.addNode("node2", callback2)
        
        self.assertEqual(len(self.walker.callbacks), 2)
        self.assertIn("node1", self.walker.callbacks)
        self.assertIn("node2", self.walker.callbacks)

    def test_setStartNode(self):
        """Test that setStartNode correctly sets the start node."""
        self.walker.setStartNode("start")
        self.assertEqual(self.walker.startNode, "start")

    def test_setStartNode_overwrites(self):
        """Test that setStartNode can overwrite previous start node."""
        self.walker.setStartNode("start1")
        self.walker.setStartNode("start2")
        self.assertEqual(self.walker.startNode, "start2")

    def test_setEndNode(self):
        """Test that setEndNode correctly adds an end node to the list."""
        self.walker.setEndNode("end")
        self.assertIn("end", self.walker.endNodes)
        self.assertEqual(len(self.walker.endNodes), 1)

    def test_setEndNode_multiple(self):
        """Test that multiple end nodes can be added."""
        self.walker.setEndNode("end1")
        self.walker.setEndNode("end2")
        self.walker.setEndNode("end3")
        
        self.assertEqual(len(self.walker.endNodes), 3)
        self.assertIn("end1", self.walker.endNodes)
        self.assertIn("end2", self.walker.endNodes)
        self.assertIn("end3", self.walker.endNodes)


class TestDGWalkerErrors(unittest.TestCase):
    """Test error handling and validation in DGWalker."""

    def setUp(self):
        """Set up a fresh DGWalker instance for each test."""
        self.walker = pyDGW.DGWalker()
        self.walker.SDEBUG = False
        self.state = pyDGW.DGW_data()

    def test_noStartNode(self):
        """Test that run() raises SystemExit when no start node is set."""
        def op_stop(state):
            return state
        
        self.walker.addNode("stop", op_stop)
        self.walker.setEndNode("stop")
        
        with self.assertRaises(SystemExit):
            self.walker.run(self.state)

    def test_noEndNode(self):
        """Test that run() raises SystemExit when no end nodes are set."""
        def op_start(state):
            return ("next", state)
        
        self.walker.addNode("start", op_start)
        self.walker.setStartNode("start")
        
        with self.assertRaises(SystemExit):
            self.walker.run(self.state)


class TestDGWalkerExecution(unittest.TestCase):
    """Test state machine execution and behavior."""

    def setUp(self):
        """Set up a fresh DGWalker instance for each test."""
        self.walker = pyDGW.DGWalker()
        self.walker.SDEBUG = False

    def test_simple_single_transition(self):
        """Test a simple state machine with one transition."""
        state = pyDGW.DGW_data()
        state.value = 0
        
        def op_start(state):
            state.value = 42
            return ("end", state)
        
        def op_end(state):
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("end", op_end)
        self.walker.setStartNode("start")
        self.walker.setEndNode("end")
        self.walker.run(state)
        
        self.assertEqual(state.value, 42)

    def test_counter_increment(self):
        """Test that counter increments correctly during execution."""
        state = pyDGW.DGW_data()
        
        def op_start(state):
            return ("end", state)
        
        def op_end(state):
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("end", op_end)
        self.walker.setStartNode("start")
        self.walker.setEndNode("end")
        
        initial_op_count = self.walker.operator_counter
        initial_node_count = self.walker.node_counter
        
        self.walker.run(state)
        
        self.assertEqual(self.walker.operator_counter, initial_op_count + 1)
        self.assertEqual(self.walker.node_counter, initial_node_count + 1)

    def test_looping_behavior(self):
        """Test state machine with looping behavior and proper termination."""
        state = pyDGW.DGW_data()
        state.count = 0
        state.limit = 100
        
        def op_start(state):
            return ("work", state)
        
        def op_work(state):
            if state.count < state.limit:
                state.count += 1
                return ("work", state)
            else:
                return ("stop", state)
        
        def op_stop(state):
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("work", op_work)
        self.walker.addNode("stop", op_stop)
        self.walker.setStartNode("start")
        self.walker.setEndNode("stop")
        self.walker.run(state)
        
        self.assertEqual(state.count, state.limit)

    def test_highCount(self):
        """Test counter that counts to 10,000 using a 3-state machine."""
        state = pyDGW.DGW_data()
        state.count = 0
        state.limit = 10000
        
        def op_start(state):
            state.limit = 10000
            return ("work", state)
        
        def op_work(state):
            if state.count < state.limit:
                state.count += 1
                return ("work", state)
            if state.count == state.limit:
                return ("stop", state)
        
        def op_stop(state):
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("work", op_work)
        self.walker.addNode("stop", op_stop)
        self.walker.setStartNode("start")
        self.walker.setEndNode("stop")
        
        initial_count = state.count
        self.walker.run(state)
        
        self.assertEqual(state.count, state.limit)
        self.assertGreater(state.count, initial_count)
        self.assertEqual(self.walker.operator_counter, 10002)

    def test_state_mutation_across_transitions(self):
        """Test that state is properly mutated through multiple transitions."""
        state = pyDGW.DGW_data()
        state.step = 0
        state.accumulator = 0
        
        def op_start(state):
            state.step = 1
            state.accumulator += 10
            return ("middle", state)
        
        def op_middle(state):
            state.step = 2
            state.accumulator += 20
            return ("end", state)
        
        def op_end(state):
            state.step = 3
            state.accumulator += 30
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("middle", op_middle)
        self.walker.addNode("end", op_end)
        self.walker.setStartNode("start")
        self.walker.setEndNode("end")
        self.walker.run(state)
        
        self.assertEqual(state.step, 3)
        self.assertEqual(state.accumulator, 60)

    def test_multiple_end_nodes_first(self):
        """Test execution with multiple end nodes, reaching the first one."""
        state = pyDGW.DGW_data()
        state.result = None
        
        def op_start(state):
            return ("end1", state)
        
        def op_end1(state):
            state.result = "end1_reached"
            return state
        
        def op_end2(state):
            state.result = "end2_reached"
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("end1", op_end1)
        self.walker.addNode("end2", op_end2)
        self.walker.setStartNode("start")
        self.walker.setEndNode("end1")
        self.walker.setEndNode("end2")
        self.walker.run(state)
        
        self.assertEqual(state.result, "end1_reached")

    def test_multiple_end_nodes_second(self):
        """Test execution with multiple end nodes, reaching the second one."""
        state = pyDGW.DGW_data()
        state.result = None
        
        def op_start(state):
            return ("end2", state)
        
        def op_end1(state):
            state.result = "end1_reached"
            return state
        
        def op_end2(state):
            state.result = "end2_reached"
            return state
        
        self.walker.addNode("start", op_start)
        self.walker.addNode("end1", op_end1)
        self.walker.addNode("end2", op_end2)
        self.walker.setStartNode("start")
        self.walker.setEndNode("end1")
        self.walker.setEndNode("end2")
        self.walker.run(state)
        
        self.assertEqual(state.result, "end2_reached")


if __name__ == '__main__':
    unittest.main()

