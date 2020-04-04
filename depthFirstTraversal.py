from DFS.tree import  Tree
from DFS.undirectedGraph import Graph
from DFS.undirectedGraph import Graph

class DFS:
    """
    Input: graph, starting root for the depth first traversal of the grapg g
    """
    def __init__(self,graph,root):
        self.__graph = graph
        self.__root = root
        self.__visited = [self.__root]
        self.__dfs = Tree(self.__root)
    
    
    """
    Recursive algorithm for parsing the connected elements of the undirected graph,forming a subgraph, a tree.
    """
    def depthFirst(self,root):
        for child in self.__graph._Graph__outbound[root]:
            if not child in self.__visited:
                self.__visited.append(child)
                self.depthFirst(child)
    
    
    """
    Return the tree of the graph from the dfs' starting from root.
    If the tree has just one component then the vertex is isolated.
    """        
    def getDfs(self):
        self.depthFirst(self.__root)
        return self.__visited