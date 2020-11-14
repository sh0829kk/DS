# -*- coding: utf-8 -*-

class Node:
    def __init__(self,key,height,left=None,right=None,parent=None):
        self.key=key
        self.value=[]
        self.lchild=left
        self.rchild=right
        self.parent=parent
        self.height=height
    def hasLeftChild(self):
        return not self.lchild==None
    def hasRightChild(self):
        return not self.rchild==None
class BST:
    def __init__(self):
        self.root=None
        self.size=0
        self.maxHeight=0
    def insert(self,key,val_new):
        if self.root:
            self._insert(key,val_new,self.root)
        else:
            self.root=Node(key,1)
            self.root.value.append(val_new)
        self.size+=1
    def _insert(self,key,val_new,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key,val_new,currentNode.lchild)
            else:
                currentNode.lchild=Node(key,currentNode.height+1,parent=currentNode)
                currentNode.lchild.value.append(val_new)
        elif key>currentNode.key:
            if currentNode.hasRightChild():
                self._insert(key,val_new,currentNode.rchild)
            else:
                currentNode.rchild=Node(key,currentNode.height+1,parent=currentNode)
                currentNode.rchild.value.append(val_new)
        else:#如果key一致
            currentNode.value.append(val_new)
    def printInorder(self):
        if self.size==0:
            print("Empty Tree")
        else:
            self._printInorder(self.root)
    def Helpprint(self,node):
        str2=''
        for i in node.value:
            str2=str2+str(i)
            if i!=node.value[len(node.value)-1]:
                str2=str2+' ' 
        return str2
    def _printInorder(self,node):
        if node is None:
            return
        self._printInorder(node.lchild)
        print("[",node.key,"---- <",self.Helpprint(node),">]")
        self._printInorder(node.rchild)

import re
bst=BST()
f=open("article.txt","r",encoding='ISO-8859-1')
data=f.readlines()
f.close()
for i in range(len(data)):
    data[i]=re.compile(r'\b[a-zA-Z]+\b',re.I).findall(data[i])
for i in range(len(data)):
    for j in data[i]:
        bst.insert(j,i)
bst.printInorder()
   