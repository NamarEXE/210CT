class Node(object):
      def __init__(self, value):
            self.value=value
            #list of nodes connected
            self.edges=[]
            #dict with key being node value and the value being the weight
            self.edgeweights={}

            
class Graph(object):
    def __init__(self):
        ### list of nodes
        self.nodes=[]
        

    def AddNode(self,node):
        self.nodes.append(node)

    def AddEdge(self,fromNode,toNode,weight):

        fromNode.edges.append((toNode))
        toNode.edges.append((fromNode))
        
        fromNode.edgeweights[toNode.value]=(weight)
        toNode.edgeweights[fromNode.value]=(weight)


    def Display(self):
        for i in range(len(self.nodes)):
            print(str((self.nodes[i]).value)+str((self.nodes[i]).edgeweights))



def dijkstras(Graph,source,destination):
      currentnode=source
      
      for node in Graph.nodes:
            node.tw=1000
      source.tw=0
      visited=[]

      while currentnode!=destination:
            for adjacentnodes in currentnode.edges:
                  # if the new path to the adjacent node is shorter than the previous shortest path it now equals the shortest path
                  if currentnode.tw+currentnode.edgeweights[adjacentnodes.value]<adjacentnodes.tw:
                        adjacentnodes.tw=currentnode.tw + currentnode.edgeweights[adjacentnodes.value]
                        adjacentnodes.path=currentnode

            visited.append(currentnode)
            minim=1000
            
            for node in Graph.nodes:
                  if node not in visited and node.tw<minim:
                        currentnode=node
                        minim=node.tw

      #calculating the final shortest path at this point current node equals destination so we go back to find the path it took to get here
      path=[]
      while currentnode!=source:
            path.append(currentnode.path.value)
            currentnode=currentnode.path
      path.reverse()
      path.append(destination.value)
      
      return ("the tw of the node is " + str(destination.tw)+ " and the path taken is " + str(path))

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)

g=Graph()

g.AddNode(node1)
g.AddNode(node2)
g.AddNode(node3)
g.AddNode(node4)
g.AddNode(node5)
g.AddNode(node6)

g.AddEdge(node1,node2,3)
g.AddEdge(node1,node5,6)
g.AddEdge(node2,node3,4)
g.AddEdge(node3,node4,2)
g.AddEdge(node5,node4,1)
g.AddEdge(node4,node6,5)

g.Display()

dijkstras(g,node1,node4)
dijkstras(g,node1,node5)
dijkstras(g,node1,node2)
dijkstras(g,node1,node3)
