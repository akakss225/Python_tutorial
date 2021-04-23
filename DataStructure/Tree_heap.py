# 힙의 장점은 특정 노드의 자식 혹은 부모노드를 구하기 쉽다.
# 이를테면, 특정 노드의 왼쪽 자식노드는 parent index * 2 + 1이 된다. >> H[k]의 왼쪽자식 노드 = H[k*2+1] / 오른쪽 자식 노드 = H[k*2+2]
# 반대로 H[k] 의 부모노드는 H[(k-1)//2]가 된다.
# 다만 쓰이지 않지만, 자리를 차지하게되는 element가 존재하게 되고, 메모리를 낭비하게 되는것과 같다.
# heap 성질 : 모든 부모노드의 key값은 자식노드의 key값보다 작지 않다.
# 따라서 heap 트리의 경우 힙성질과 모양을 모두 만족해야한다.(마지막 레벨을 제외한 모든 레벨은 꽉 채움과 동시에 key값의 분배를 나눔)
# heap의 경우 루트노드에 가장 큰 값이 들어간다.
# 제공해야하는 연산 : insert / find_max(return H[0]) / delete_max 
# heap Tree를 만드려면, 처음에 make heap과정을 거쳐야한다.

class Heap_Tree:
      def __init__(self):
            self.H = []
            
      def find_max(self):
            return self.H[0]
            
      def get_parent(self, idx):
            return int((idx - 1)/2)
      
      def get_L_child(self, idx):
            return 2 * idx +1
      
      def get_R_child(self, idx):
            return 2 * idx + 2
      
      def has_parent(self, idx):
            return self.get_parent(idx) >= 0
      
      def has_L_child(self, idx):
            return self.get_L_child(idx) < len(self.H)
      
      def has_R_child(self, idx):
            return self.get_R_child(idx) < len(self.H)
      
      def swap(self, i, j):
          self.H[i], self.H[j] = self.H[j], self.H[i]
      
      def insert_key(self, item):
          self.H.append(item)
          self.heapify_up(len(self.H) - 1)
      
      def heapify_up(self, i):
          while(self.has_parent(i) and self.H[i] > self.H[self.get_parent(i)]):
                self.swap(i, self.get_parent(i))
                i = self.get_parent(i)

      def heapify_down(self,i):
            while(self.has_L_child(i) or self.has_R_child(i)):
                  if self.H[self.get_L_child(i)] > self.H[self.get_R_child(i)]:
                        if self.H[i] < self.H[self.get_L_child(i)]:
                              self.swap(i, self.get_L_child(i))
                              i = self.get_L_child(i)
                  else:
                        if self.H[i] < self.H[self.get_R_child(i)]:
                              self.swap(i, self.get_R_child(i))
                              i = self.get_R_child(i)
                              
      def delete_max(self):
            self.swap(0, len(self.H) - 1)
            self.H.pop(len(self.H) - 1)
            self.heapify_down(0)
            
            
      def print_Heap(self):
            print(self.H)



h = Heap_Tree()
h.insert_key(10)
h.insert_key(30)
h.insert_key(12)
h.insert_key(45)
h.insert_key(44)
h.insert_key(60)
h.insert_key(13)
h.insert_key(1)
h.insert_key(17)
h.insert_key(52)
h.insert_key(33)
h.insert_key(41)

h.print_Heap()

h.delete_max()
h.print_Heap()

h.delete_max()
h.print_Heap()