# -*- coding: utf-8 -*-
class Node:
    def __init__(self, key, val, height, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.lchild = left
        self.rchild = right
        self.parent = parent
        self.height = height

    def hasLeftChild(self):
        return not self.lchild == None

    def hasRightChild(self):
        return not self.rchild == None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.maxHeight = 0

    # 插入
    def insert(self, key, val):
        if self.root:
            self._insert(key, val, self.root)
        else:
            self.root = Node(key, val, 1)
            self.size += 1

    def _insert(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, val, currentNode.lchild)
            else:
                currentNode.lchild = Node(key, val, currentNode.height + 1, parent=currentNode)
                self.size += 1
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._insert(key, val, currentNode.rchild)
            else:
                currentNode.rchild = Node(key, val, currentNode.height + 1, parent=currentNode)
                self.size += 1
        else:  # 如果key一致
            currentNode.value = val
            #print(val)
    # 寻找
    def search(self, key):
        if key == None:
            return None
        if self.root:
            result = self._search(key, self.root)
            if result:
                # print(result.value)
                return result
            else:
                return None
        else:
            return None

    def _search(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif node.key < key:
            return self._search(key, node.rchild)
        else:
            return self._search(key, node.lchild)

    # 移除
    def remove(self, key):
        if self.size > 1:
            nodeToRemove = self.search(key)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self.size -= 1
            else:
                return None
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            return None

    def _findMin(self, node):
        if node:
            currentNode = node
            while currentNode.lchild:
                currentNode = currentNode.lchild
            return currentNode

    def _remove(self, node):
        if not node.lchild and not node.rchild:
            if node == node.parent.lchild:
                node.parent.lchild = None
            else:
                node.parent.rchild = None
        elif node.rchild and node.lchild:
            minNone = self._findMin(node.rchild)
            self._remove(minNone)
            node.value = minNone.value
        else:
            if node.lchild:
                if node.parent and node.parent.lchild == node:
                    node.lchild.parent = node.parent
                    node.parent.lchild = node.lchild
                elif node.parent and node.parent.rchild == node:
                    node.lchild.parent = node.parent
                    node.parent.rchild = node.lchild
                else:
                    self.root = node.lchild
                    node.lchild.parent = None
                    node.lchild = None
            else:
                if node.parent and node.parent.lchild == node:
                    node.rchild.parent = node.parent
                    node.parent.lchild = node.rchild
                elif node.parent and node.parent.rchild == node:
                    node.rchild.parent = node.parent
                    node.parent.rchild = node.rchild
                else:
                    self.root = node.rchild
                    node.rchild.parent = None
                    node.rchild = None

    # 更新
    def update(self, key, value):
        if key == None or value == None:
            return None
        if self.search(key):
            self.search(key).value = value
            return self.search(key)
        else:
            return None

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None
        self.size = 0

    # 展示
    def showStructure(self):
        print("-" * 20)
        if self.size == 0:
            return 0
        else:
            self._printInorder(self.root)
            print("There are %d nodes in this BST." % self.size)
            print("The height of this BST is %d." % self.maxHeight)
        print("-" * 20)

    # def printInorder(self):
    #     if self.size==0:
    #         print("Empty Tree")
    #     else:
    #         self._printInorder(self.root)
    # 先序遍历
    def _printInorder(self, node):
        if node:
            self.maxHeight = max(self.maxHeight, node.height)
            self._printInorder(node.lchild)
            # print(node.value)
            self._printInorder(node.rchild)
        return

    # 更新树高
    def UpdateHeight(self, node):
        if node:
            if node.parent == None:
                node.height = 1
            else:
                node.height = node.parent.height + 1
            self._printInorder(node.lchild)
            self._printInorder(node.rchild)
        else:
            return


import re

bst = BST()
# 读入文件
f = open("testcases.txt", "r",encoding='utf8')
data = f.readlines()
f.close()
count = 0
# 正则化处理
for i in range(len(data)):
    data[i] = data[i].replace('"', "")
    data[i] = re.split('[,()]', data[i])
# 对读入操作符进行判断
for i in range(len(data)):
    j = 0
    if data[i][j] == '+':
        bst.insert(data[i][1], data[i][2])
        # bst.showStructure()
    elif data[i][j] == '-':
        if bst.search(data[i][1]):
            count += 1
            print("remove success ---%s %s" % (data[i][1], bst.search(data[i][1]).value))
            bst.remove(data[i][1])
        else:
            print("remove unsuccess ---%s" % data[i][1])
        bst.UpdateHeight(bst.root)
        # bst.showStructure()
    elif data[i][j] == '?':
        if bst.search(data[i][1]):
            print("search success ---%s %s" % (data[i][1], bst.search(data[i][1]).value))
        else:
            print("search unsuccess ---%s" % data[i][1])
    elif data[i][j] == '=':
        if bst.update(data[i][1], data[i][2]):
            print("update success ---%s %s" % (data[i][1], data[i][2]))
        else:
            print("update unsuccess ---%s %s" % (data[i][1], data[i][2]))
        # bst.showStructure()
    elif data[i][j] == '#\n':
        bst.showStructure()


