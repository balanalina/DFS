from copy import deepcopy 
class Graph:
    def __init__(self,number):
        self.__n = number
        self.__inbound = [[]for i in range(number)]
        self.__outbound = [[] for i in range(number)]
        for i in range(number):
            self.__inbound[i] = []
            self.__outbound[i] = []
            
    """
    This function returns true if there is an edge between the vertices "start" and "end" and False othewise.
    Input: start, end - integers
    Output: True, False
    """
    def isEdge(self,start,end):
        if end in  self.__outbound[start] and start in self.__inbound[end]:
            return True
        return False
    
    """
    The functions adds a new edge to the graph, returns False if the edge already exists, if the edge is added True will be returned.The default value for a cost is 1.
    Input: start(starting vertex of the edge),end(ending vertex of the edge) and otherwise
    Output: True or False
    """
    def addEdge(self,start,end):
        if self.isEdge(start,end) or start == end:
            return False
        self.__outbound[start].append(end)
        self.__outbound[end].append(start)
        self.__inbound[start].append(end)
        self.__inbound[end].append(start)
        return True
    
    """
    The function removes an edge and its cost and returns True,if the edge does not exist False is returned.
    Inout: start,end - unsigned integers
    Output: True or False
    """
    def removeEdge(self,start,end):
        if self.isEdge(start, end):
            self.__outbound[start].remove(end)
            self.__inbound[end].remove(start)
            return True
        return False
    
    """
    This function returns the number of vertices of the graph.
    Input: - 
    Output: n - integer
    """
    def getVertices(self):
        return self.__n    

    
    """
    The function creates and returns another graph, representing a copy of the initial graph.
    Input: -
    Outpu: g - Graph
    """
    def copyGraph(self):
        graph = Graph(self.__n)
        graph.setOutbound(deepcopy(self.getOutbound()))
        graph.setInbound(deepcopy(self.getInbound()))
        return graph 
    """
    Setters and getters.
    """
    def getInbound(self):
        return self.__inbound
    
    def getOutbound(self):
        return self.__outbound
    
    def setInbound(self,list):
        self.__inbound = list
        
    def setOutbound(self,list):
        self.__outbound = list
        
    
    def getIN(self):
        return self.__inbound
    
    def getOUT(self):
        return self.__outbound
    
    
    """
    This 3 functions return iterators for parsing the graph,parsing inbounds and outbounds.
    """
    def parseOut(self,vertex):
        return vertexIteratorOut(self,vertex)
    
    def parseIn(self,vertex):
        return vertexIteratorIn(self,vertex)
    
    def parse(self):
        return verticesIterator(self)
    """
    Iterator for parsing out a vertex.
    Input: graph - Graph, vertex - integer
    """
class vertexIteratorOut:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
    """
    Checks if there still are elements to parse.
    """  
    def valid(self):
        if self.__current < len(self.__g.getOutbound()[self.__vertex]):
            return True
        return False
    
    """
    Moves to the next element if there is a next element.
    """
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
    """
    Makes the first element the current element.
    """
    def first(self):
        self.__current = 0 
        
    """
    Returns the current element that was iterated.
    """
    def getCurrent(self):
        if self.valid():
            return self.__g.getOutbound()[self.__vertex][self.__current]
        else:
            raise ValueError
     
    """
    Iterator for parsing in a vertex.
    Input: graph - Graph, vertex - integer
    """   
class vertexIteratorIn:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
    
    """
    Checks if there still are elements  to be iterated.
    """   
    def valid(self):
        if self.__current < len(self.__g.getInbound()[self.__vertex]):
            return True
        return False
    
    """
    Moves the iterator to the next element if there still are elements.
    """
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
    
    """
    The first element becomes the current one.
    """
    def first(self):
        self.__current = 0 
        
    """
    Return the current element.
    """
    def getCurrent(self):
        if self.valid():
            return self.__g.getInbound()[self.__vertex][self.__current]
        else:
            raise ValueError
     
    """
    Iterator for parsing the graph.
    Input: graph - Graph
    """   
class verticesIterator:
    def __init__(self,graph):
        self.__g = graph
        self.__current = 0
    
    """
    Checks if there still are vertices to be iterated.
    """
    def valid(self):
        if self.__current < self.__g._Graph__n:
            return True
        return False
    
    def first(self):
        self.__current = 0
        
    def next(self):
        if self.valid():
            self.__current += 1
            
            
        return False
    
    def getCurrent(self):
        if self.valid():
            return self.__current
        raise ValueError
    
