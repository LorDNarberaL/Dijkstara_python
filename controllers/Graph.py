class Graph :
    class Node :
        def __init__(self, edge) :
            self.edge = edge
            self.next = None

    class Edge :
        def __init__(self, start, end, weight) :
            self.start = start
            self.end = end
            self.weight = weight
            self.next = None

        def getterStart(self) :
            return self.start

        def getterEnd(self) :
            return self.end

        def getterWeight(self) :
            return self.weight
    
    def __init__(self, vertex) :
        self.vertex = vertex
        self.graph = [None] * self.vertex
        self.listEdge = []

    def addEdge(self, start, end, weight) :
        edge = self.Edge(start, end, weight)
        list = self.Node(edge)
        list.next = self.graph[start]
        self.graph[start] = list      

        self.listEdge.append(edge)

        #self.listEdge.insert(len(self.edgelist)-1, edge)
        
        edge = self.Edge(end, start, weight)
        list = self.Node(edge)
        list.next = self.graph[end]
        self.graph[end] = list

    def printGraph(self) :
        print("Graph :")
        for i in range(self.vertex) :
            print(" V[%d]"%i,end = '')
            list = self.graph[i]
            if(list == None) :
                print(" --> None")
                continue
            while (list != None) :
                print(" --> V[%d]" %list.edge.getterEnd(),end = '')
                print(" | %d" %list.edge.getterWeight(),end = '')
                list = list.next
            print()
        
    def printEdge(self) :
        print("Edges :")
        for i in range(len(self.listEdge)) :
            print(" [%d]"%(i+1),end = '')
            print(" Start %d" %self.listEdge[i].getterStart(),end = '')
            print(" --> End %d" %self.listEdge[i].getterEnd(),end = '')
            print(" | weight %d" %self.listEdge[i].getterWeight(),end = '')
            print()