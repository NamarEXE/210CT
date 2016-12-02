class Node(object):
      def __init__(self, value):
            self.value=value
            self.edges=[]
            self.edgesvalues=[]


class Graph(object):
    def __init__(self):
        ### list of nodes
        self.nodes=[]
        

    def AddNode(self,node):
        self.nodes.append(node)

    def AddEdge(self,fromNode,toNode):
        fromNode.edges.append((toNode))
        toNode.edges.append((fromNode))
        fromNode.edgesvalues.append((toNode.value))
        toNode.edgesvalues.append((fromNode.value))
              
    def Display(self):
        for i in range(len(self.nodes)):
            print(str((self.nodes[i]).value)+str((self.nodes[i]).edgesvalues))


    def DFS(self,v):
        Stack=[]
        Visited=[]
        Visited2=[]
        Stack.append(v)
        while len(Stack) != 0:
            poppeditem=Stack.pop()
            if poppeditem not in Visited:
                Visited.append(poppeditem)
                Visited2.append(poppeditem.value)
                for i in range(len(poppeditem.edges)):
                    Stack.append(poppeditem.edges[i])
        return Visited2


    def BFS(self,v):
        queue=[]
        visited=[]
        visited2=[]
        queue.append(v)
        while len(queue) !=0:
            nextitem=queue[0]
            queue=queue[1:]
            if nextitem not in visited:
                visited.append(nextitem)
                visited2.append(nextitem.value)
                for i in range(len(nextitem.edges)):
                      queue.append(nextitem.edges[i])
        return visited2
        
g=Graph()

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

g.AddNode(node1)
g.AddNode(node2)
g.AddNode(node3)
g.AddNode(node4)
g.AddNode(node5)

g.AddEdge(node1,node2)
g.AddEdge(node2,node3)
g.AddEdge(node3,node4)
g.AddEdge(node4,node5)
g.Display()




g.DFS(node2)
g.BFS(node2)
