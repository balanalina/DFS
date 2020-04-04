from DFS.undirectedGraph import Graph
from DFS.depthFirstTraversal import DFS
import random

"""
Creates and returns a random graph having n vertices and m edges.
"""
def createRandomGraph(n, m):
    graph = Graph(n)
    for i in range(m):
        v1 = random.randint(0,n-1)
        v2 = random.randint(0,n-1)
        while not graph.addEdge(v1,v2):
            v1 = random.randint(0,n-1)
            v2 = random.randint(0,n-1)
    return graph

def printGraph(g):
    s1 = "Graph: \n"
    for vertice in range(len(g.getOUT())):
        s1 += str(vertice) + " --> " 
        for v in g.getOUT()[vertice]:
            s1+= str(v) + " "
        s1+="\n"
    print(s1)
    
def printConnected(list):
    for i in range(len(list)):
        print(str(list[i]) + " ")
    print(" ")
        
def getConnected(g,n):
    list = []
    dict = {}
    for i in range(n):
        dict[i] = False
    for i in range(n):
        dfs = DFS(g,i)
        l = dfs.getDfs()
        list.append(l)
        if not dict[l[0]]:
            printConnected(l)
            for j in range(len(l)):
                dict[l[j]] = True
            
        
def main():
    n= int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))
    g = createRandomGraph(n, m)
    printGraph(g)
    getConnected(g, n)
        
    
    
main()
