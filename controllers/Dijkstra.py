import sys
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

class Dijkstra(Graph) :

    def __init__(self, vertex):
        super().__init__(vertex)
        super().addEdge(0, 1, 10)
        super().addEdge(0, 3, 30)
        super().addEdge(0, 4, 45)
        super().addEdge(1, 2, 50)
        super().addEdge(1, 4, 40)
        super().addEdge(1, 5, 25)
        super().addEdge(2, 4, 35)
        super().addEdge(2, 5, 15)
        super().addEdge(3, 5, 20)
        super().addEdge(4, 5, 55)

    def dijkstra(self, start) :
        newS = start
        vertex = self.vertex
        setV = {start}
        dist = [[0]*2 for i in range(vertex)]
        
        for i in range(0, vertex) :
            if(i != start) : 
                dist[i][0] = sys.maxsize

        print(dist)

        while(len(setV) != vertex) :
            list = self.graph[newS]

            while(list != None) :
                sum = dist[newS][0] + list.edge.getterWeight()
                end = list.edge.getterEnd()

                if((end not in setV) and (sum < dist[end][0])) :
                    dist[end][0] = sum
                    dist[end][1] = newS
                
                list = list.next

            min = 0
            for i in range(vertex) :
                if(i not in setV) :
                    min = i
                    break
            
            for i in range(vertex) :
                if((i not in setV) and (dist[i][0] < dist[min][0])) :
                    min = i
            
            setV.add(min)
            newS = min
        
        print(dist)

    def printDijkstra(self, dist, start) :

        end = int(input("Enter End Vertex from Vertex "+str(start)+" (-1 to exit) : "))
        
        while(end != -1) :
            print("Shortest Path from V[%d] to V[%d] = %d" %(start, end, dist[end][0]))
            curr = end
            print(" V[%d]"%start, end='')
            p = None

            while(curr != start) :
                q = self.graph[curr]
                #if(q == None) :
                #    print(" --> null\n")
                #    break
    
                while(q.edge.getterEnd() != dist[curr][1]) :
                    q = q.next
                
                temp = self.Node(q.edge)
                temp.next = p
                p = temp
                
                #q.next = p
                #p = q

                curr = dist[curr][1]

            #if(p == None) :
            #    end = int(input("Enter End Vertex from Vertex "+str(start)+" (-1 to exit) : "))
            #    continue
                
            while(p != None) :
                print(" --> V[%d] | %d"%(p.edge.getterStart(), p.edge.getterWeight()), end='')
                p = p.next
            print()
            print("------------------------------------------------------------")

            end = int(input("Enter End Vertex from Vertex "+str(start)+" (-1 to exit) : "))

