class Tree:
    def __init__(self,root):
        self.__children = {root:[]}
        self.__parent = {root:None}
        self.__root = root
        
    """"
    Adds a new children,childVertex from parentVertex.
    Preconditions: parentVertex must exist
    """
    def addChildren(self,parentVertex,childVertex):
        self.__children[parentVertex].append(childVertex)
        self.__parent[childVertex] = parentVertex
        self.__children[childVertex] = []
    
    """
    Checks if a vertex is in the tree.
    Returns True if it is and False otherwise.
    """  
    def isVertex(self,vertex):
        return vertex in self.__children.keys()
        
    """
    Returns the children of the vertex.
    None is returned if there is no child.
    """
    def getChild(self,vertex):
        if self.__children[vertex] != []:
            return self.__children[vertex]
        return None
    
    """
    Returns the parent of the vertex.
    None is returned if the vertex is not in the tree.
    """
    def getParent(self,vertex):
        if not self.isVertex(vertex):
            return None
        return self.__parent[vertex]
        
    """
    The printTreeR function prints a subtree, the next one print the tree rooted in the vertex root.
    """
    def printTree(self,root,spaces):
        print(' ' * spaces,root)
        for children in self.__children[root]:
            self.printTree(children, spaces+1)
            



        
    