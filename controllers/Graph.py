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
    
    def __init__(self) :
        self.vertex = 6
        self.graph = [None] * self.vertex
        self.listEdge = []
        self.addEdge(0, 1, 10)
        self.addEdge(0, 3, 30)
        self.addEdge(0, 4, 45)
        self.addEdge(1, 2, 50)
        self.addEdge(1, 4, 40)
        self.addEdge(1, 5, 25)
        self.addEdge(2, 4, 35)
        self.addEdge(2, 5, 15)
        self.addEdge(3, 5, 20)
        self.addEdge(4, 5, 55)

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
        outList = []
        outText = ""
        for i in range(self.vertex) :
            outText = outText + (" V[%d]"%i)
            list = self.graph[i]
            if(list == None) :
                outText = outText + (" --> None")
                continue
            while (list != None) :
                outText = outText + (" --> V[%d]" %list.edge.getterEnd())
                outText = outText + (" | %d" %list.edge.getterWeight())
                list = list.next
            outList.append(outText)
            outText = ""
        return outList
        
    def printEdge(self) :
        print("Edges :")
        for i in range(len(self.listEdge)) :
            print(" [%d]"%(i+1),end = '')
            print(" Start %d" %self.listEdge[i].getterStart(),end = '')
            print(" --> End %d" %self.listEdge[i].getterEnd(),end = '')
            print(" | weight %d" %self.listEdge[i].getterWeight(),end = '')
            print()