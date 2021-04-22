# 일반 List를 이용한 Binary Tree
# 기본적으로 List를 이용한 Tree의 경우, 자식의 인덱스를 2로 나눈값이 부모의 인덱스가 된다.(좌변)
# 다만, 이는 List의 첫번째 인덱스에 None을 넣은 경우에 한한다.


class BinaryTree:
    def __init__(self):
        self.t = [None] # 초기 생성자 생성시, 첫번째 인덱스에 None이 들어간 상태의 리스트를 만든다.
    
    def append(self, item):
        self.t.append(item) # 일반 리스트로 하기 때문에, 값을 넣어줄 때 간단히 append로 입력할 수 있다.
    
    def size(self):
        return len(self.t) - 1 # 0번째 인덱스에 None이 들어가기 때문에 -1 을 해준다.
    
    def getChild(self, item):
        if item in self.t:
            k = self.t.index(item)
            left = 2 * k
            right = 2 * k + 1
            if left <= self.size():
                leftNode = self.t[left]
            else:
                leftNode = None
            if right <= self.size():
                rightNode = self.t[right]
            else:
                rightNode = None
            return leftNode, rightNode
        else:
            print('item is not found')
            
    def getParent(self, item):
        if item in self.t:
            k = self.t.index(item)
            parent = k // 2
            if parent > 0:
                return self.t[parent]
            else:
                return None
        else:
            print('item is not found')

t = BinaryTree()
for i in range(12):
    t.append(chr(65+i))

print(t.t)

print(t.getChild('B'))
print(t.getChild('C'))

print(t.getParent('L'))
