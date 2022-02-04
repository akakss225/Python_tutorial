from collections import deque
def solution(phone_book):
    q = deque(sorted(phone_book, key=len))
    while q:
        cur = q.popleft()
        for i in q:
            if i[0:len(cur)] == cur:
                return False
    return True

def solution(phone_book):
    d = dict()
    phone_book.sort(key = len)
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
        
    return True




phone = ["119", "97674223",  '9763' ,"195524421"]

print(solution(phone))


