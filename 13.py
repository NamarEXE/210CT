class Node(object):
      def __init__(self, value):
            self.value=value
            self.edges=[]




class Graph(object):     
      def __init__(self):
          ### list of nodes in graph
            self.nodes=[]
            
      def AddNode(self,node):
            self.nodes.append(node)

      def AddEdge(self,fromNode,toNode):
            fromNode.edges.append((toNode.value))
            toNode.edges.append((fromNode.value))
            
            
      def Display(self):
            for i in range(len(self.nodes)):
                  print(str((self.nodes[i]).value)+str((self.nodes[i]).edges))



# instanciate graph                  
g = Graph()

#instanciate nodes
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

#add node function adds nodes to graph
g.AddNode(node1)
g.AddNode(node2)
g.AddNode(node3)
g.AddNode(node4)

#add edge function
g.AddEdge(node2,node4)
g.AddEdge(node1,node3)
g.AddEdge(node4,node3)

##displays graph as a adjacency list
g.Display()




