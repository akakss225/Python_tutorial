class BNode:
    def __init__(self, item = None):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        
    def inOrder(self):
        if self.item != None:
            if self.left:
                self.left.inOrder()
            print(self.item, end=" ")
            if self.right:
                self.right.inOrder()

class BST:
    def __init__(self):
        self.root = BNode()
        self.size = 0
        
    def find(self, item): # 찾고자하는 item이 존재하면, 그 값을 return하고, 만약 없다면 그 부모node를 return한다.
        if self.size == 0:
            return None
        else:
            curNode = self.root
            preNode = None
            while curNode != None:
                if curNode.item == item:
                    return curNode
                elif curNode.item < item:
                    preNode = curNode
                    curNode = curNode.right
                else:
                    preNode = curNode
                    curNode = curNode.left
            return preNode

    def insert(self, item):
        preNode = self.find(item)
        if preNode == None or preNode.item != item:
            newNode = BNode(item)
            if preNode == None:
                self.root = newNode
            else:
                newNode.parent = preNode
                if preNode.item > newNode.item:
                    preNode.left = newNode
                else:
                    preNode.right = newNode
            self.size += 1
            return newNode
        else:
            print('삽입하려는 value가 이미 존재합니다.')
            return preNode
                    
    def print(self):
        self.root.inOrder()
                
    
                
      
b = BST()

b.insert(16)
b.insert(8)
b.insert(4)
b.insert(20)
b.insert(18)
b.insert(5)
b.insert(9)
b.insert(6)
b.insert(14)
b.insert(7)
b.insert(2)
b.insert(3)
b.insert(12)
b.insert(1)

b.print()