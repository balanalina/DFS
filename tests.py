from DFS.undirectedGraph import Graph
from DFS.tree import Tree
from DFS.depthFirstTraversal import DFS
import unittest

class test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def tests(self):
        g = Graph(5)
        g.addEdge(0,1)
        g.addEdge(1,2) 
        g.addEdge(2,4) 
        g.addEdge(3,2) 
        g.addEdge(3,4) 
        g.addEdge(4,3) 
        g.addEdge(4,1)
        gr = g.copyGraph()
        assert g.isEdge(0,4) == False
        g.addEdge(0,4)
        assert g.isEdge(0, 4) == True 
        g.addEdge(0, 2)
        g.removeEdge(0, 2)
        assert g.isEdge(0,5) == False
        assert g.addEdge(0,1) == False
        assert g.isEdge(0,2) == False
        assert g.isEdge(1,2) == True
        assert gr.isEdge(0,4) == False
        t = Tree(0)
        t.addChildren(0, 1)
        t.addChildren(1,2)
        t.addChildren(2, 4)
        t.addChildren(2,3)
        assert t.getChild(2) == [4,3] 
        dfs = DFS(g,3)