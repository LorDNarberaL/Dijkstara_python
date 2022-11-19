from Controllers.Graph import Graph
import sys

class Dijkstra(Graph) :

    def __init__(self):
        super().__init__()
        

    def dijkstra(self, start) :
        newS = start
        vertex = self.vertex
        setV = {start}
        dist = [[0]*2 for i in range(vertex)]
        
        for i in range(0, vertex) :
            if(i != start) : 
                dist[i][0] = sys.maxsize

        dist[start][1] = "None" 

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
        
        return dist

    def printDijkstra(self, dist, start, end) :
        
        outText = ("Shortest Distance from V[%d] to V[%d] = %d" %(start, end, dist[end][0]))
        outList = []
        outList.append(outText)
        outText = "Shortest Path : "

        outText = outText + (" V[%d]"%start)
        
        curr = end
        p = None

        while(curr != start) :
            q = self.graph[curr]
    
            while(q.edge.getterEnd() != dist[curr][1]) :
                q = q.next
                
            temp = self.Node(q.edge)
            temp.next = p
            p = temp

            curr = dist[curr][1]
             
        while(p != None) :
            outText = outText + (" --> V[%d] | %d"%(p.edge.getterStart(), p.edge.getterWeight()))
            p = p.next
        
        outList.append(outText)
        return outList        
