# LinkedList

class Node:
    def __init__(self, item = None):
        # 뼈대에 들어갈 각 노드의 기본 설정값
        self.item = item
        self.link = None

class LinkedList:
    def __init__(self):
        # node들이 담길 뼈대를 생성.
        self.l = []
        # 리스트의 첫 값을 설정해줌.
        self.root = Node()

    def append(self, item):
        # 현재의 노드가 가리키는 노드를 변수로 지정해줌.
        curNode = self.root
        # 새로 추가될 node를 newNode라는 이름으로 만들어줌.
        newNode = Node(item)
        # 만약 리스트가 비어있으면?
        if self.root.item == None:
            # root에 새로 추가될 node를 넣어줌.
            self.root = newNode
        # 리스트가 비어있지않다면?
        else:
            # 우선 현재 위치를 가장 끝부분으로 옮겨줌.
            while curNode.link != None:
                curNode = curNode.link
            # 그리고 가장 끝 node의 link에 newNode를 연결해주면 끝
            curNode.link = newNode
        
    def insert(self, index, item):
        # 중간에 삽입하고 싶다면?
        newNode = Node(item)
        curNode = self.root
        
        # 만약 첫번인덱스, 즉 root에 삽입하고 싶다면
        if index == 0:
            # root에 newNode를 넣어주고, newNode의 link에 기존의 루트를 연겷해줌.
            self.root = newNode
            newNode.link = curNode
        else:
            # 그게 아니라면
            for i in range(index):
                # 삽입하고자하는 노드와 그 전 노드를 한칸씩 밀어주며 이동한다.(삽입하고자 하는 인덱스까지)
                preNode = curNode
                curNode = curNode.link
            # preNode와 newNode를 연결하고, newNode의 link에 현재 curNode를 연결한다.
            preNode.link = newNode
            newNode.link = curNode
            
    def delete(self, item):
        # 삭제하고자 하는 node와 그 전 node를 return 해줄 node를 생성
        preNode = self.root
        curNode = self.root
        # 만약 리스트가 비었다면
        if self.root.item == None:
            # None을 return
            return None
        # 아니라면
        else:
            # 지우고자하는 item이 root일때
            if self.root.item == item:
                # root에 그냥 다음 node를 넣어준다.
                self.root = curNode.link
            # 아닐때
            else:
                # 일단 item을 찾음
                while curNode.item != item:
                    preNode = curNode
                    curNode = curNode.link
                # 만약 item을 찾았다면,
                if curNode.item == item:
                    # 그 전 node와 삭제할 node의 다음 node를 연결해줌.
                    preNode.link = curNode.link
                # item 을 못찾았다면
                else:
                    # None을 return
                    return None
            
    

    def print(self):
        curNode = self.root
        if self.root != None:
            while curNode != None:
                print(curNode.item, end=" ")
                curNode = curNode.link
        print()

l = LinkedList()

l.append('사과')
l.append('귤')
l.append('배')
l.append('포도')

l.print()

l.delete('사과')

l.print()

l.delete('포도')

l.print()

l.insert(1, '망고')

l.print()

l.insert(3, '수박')

l.print()

l.insert(0, '블루베리')

l.print()