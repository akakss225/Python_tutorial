# Hash Table
# 리스트는 search를 할 때 O(n)의 시간을 필요로 한다. 딕셔너리의 경우 리스트와는 다르게 search시간이 O(1)이다. 이는 키값과 밸류값이 있기 때문이다.
# 처리시간은 프로그래밍에서 가장 기초적으로 고려되어야 하는 것이다.

# 소수를 구하는 알고리즘
def prime(x):
    for i in range(2, x):
        if x % i == 0: # i 는 x보다 작은 수일수 밖에 없다.
            return False # 한번이라도 나누어지면, False를 return
    return True

def getPrime(n):
    import numpy as np
    is_prime = np.array(list(range(n+1)))   # n개의 빈 배열 생성
    #print(is_prime)
    N_max = int(np.sqrt(len(is_prime) - 1)) # N_max = sqrt(n), 100까지 구한 다면 sqrt(100) = 10 까지 검사하면 됨
    #print(N_max)
    for j in range(2, N_max + 1):
        is_prime[2*j::j] = 0
        #print(j, is_prime)
    is_prime = np.setdiff1d(is_prime,np.array([0,1])) # is_prime - [0,1]
    return is_prime[-1]

def getM(n):
    m1 = 3 * n
    m2 = getPrime(m1)
    return m2

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.link = None

# LinkedList Class: Linked List에 노드를 추가(append)하고 노드를 찾는(get) 메소드가 있다.
class LinkedList:
    def __init__(self):
        self.root = Node()
        self.cnt = 0
    # 리스트 마지막에 노드를 삽입한다.
    def append(self, key, value):
        # 추가할 새 노드를 만든다.
        newNode = Node(key, value)
        # 현위치를 루트로 지정하고 노드를 추가한다.
        curNode = self.root
        # 현 위치가 비어 있으면 현 위치에 삽입
        if curNode.key == None:
            self.root = newNode
            self.cnt += 1
        # 현 위치가 비어 있지 않으면 다음 노드로 옮기는 작업을 마지막 노드가 나타날 때 까지 반복한다.
        # 마지막 노드를 만나면 마지막 노드 다음에 새 노드를 삽입한다.
        else:
            while curNode.link != None:
                self.cnt += 1
                curNode = curNode.link
            curNode.link = newNode
        return self.cnt

    def get(self, key):
        cnt = 0
        curNode = self.root
        if curNode.key == key:
            return curNode.value, cnt
        else:
            while curNode.link != None:
                curNode = curNode.link
                cnt += 1
                if curNode.key == key:
                    return curNode.value, cnt
            return None

class ChainHash:
    def __init__(self, k): # k = key의 갯수
        # 데이터 수의 3배를 기준으로 소수 리턴한다.
        self.m = self._getPrime(3 * k)
        self.h = [None] * self.m

    def _getPrime(self, n):
        # 1~n 사이의 소수를 구하고 가장 큰 두 개의 소수를 리턴한다.
        import numpy as np
        is_prime = np.array(list(range(n+1)))
        N_max = int(np.sqrt(len(is_prime) - 1)) # looping 2 to sqrt(n)

        for j in range(2, N_max + 1):
            is_prime[2*j::j] = 0
        is_prime = np.setdiff1d(is_prime,np.array([0,1])) # is_prime - [0,1]
        return is_prime[-1]

    def insert(self, key, item):

        idx = key % self.m
        if self.h[idx] == None:
            self.h[idx] = LinkedList()
            self.h[idx].append(key, item)
        else:
            print(key, "충돌")
            curNode = self.h[idx].root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = Node(key, item)

    def get(self, key):
        idx = key % self.m
        xList = self.h[idx]
        return xList.get(key)


x = [25, 37, 18, 55, 22, 35, 50, 63] # keys, value = [a25, a37, a18, ... ]

h = ChainHash(len(x))

for val in x:
    h.insert(val, 'a'+str(val))

y = [26, 38, 19, 56, 23, 36, 51, 64]
for val in y:
    h.insert(val, 'a'+str(val))

for key in x:
    print(key, h.get(key))

for key in y:
    print(key, h.get(key))
