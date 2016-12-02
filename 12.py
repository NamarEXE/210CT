#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)


def in_order(tree):
    stack=[]
    R=tree
    stack.append(R)
    R=R.left
    while(R!=None):
        stack.append(R)
        R=R.left
        if(R==None) and stack!=[]:
            poppeditem=stack.pop()
            print(poppeditem.value)
            while poppeditem.right==None:
                poppeditem=stack.pop()
                print(poppeditem.value)
            if poppeditem.right!=None:
                R=poppeditem.right


def Tree_Sort(Array):
    tree=tree_insert(None,Array[0])
    for i in range(len(Array)-1):
        tree_insert(tree,Array[i+1])
    in_order(tree)




