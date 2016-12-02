class Node(object):
      def __init__(self, value):
            self.value=value
            self.next=None
            self.prev=None

class List(object):
      def __init__(self):
            self.head=None
            self.tail=None

      def insert(self,n,x):
            if n!=None:
                  x.next=n.next
                  n.next=x
                  x.prev=n
                  if x.next!=None:
                        x.next.prev=x              
            if self.head==None:
                  self.head=self.tail=x
                  x.prev=x.next=None
            elif self.tail==n:
              self.tail=x
              
      def display(self):
            values=[]
            n=self.head
            while n!=None:
                  values.append(str(n.value))
                  n=n.next
            print(values)

      def NodeDelete(self, Node):
            if Node.prev != None:
                  Node.prev.next=Node.next
            else:
                  self.head=Node.next
            if Node.next != None:
                  Node.next.prev=Node.prev
            else:
                  self.tail=Node.prev




array=List()
a=Node(1)
b=Node(2)
c=Node(3)
array.insert(None,a)
array.insert(a,b)
array.insert(b,c)
array.display()
array.NodeDelete(a)
array.display()
