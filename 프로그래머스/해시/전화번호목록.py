from collections import deque
import heapq


def solution(phone_book):
    q = deque(sorted(phone_book, key=len))
    while q:
        cur = q.popleft()
        for i in q:
            if i[0:len(cur)] == cur:
                return False
    return True

def solution(phone_book):
    s = sorted(phone_book, key=len)
    while s:
        cur = s.pop()
        for i in s:
            if i[0:len(cur)] == cur:
                return False
    return True

def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return True

def solution(phone_book):
    l = "/" + "/".join(phone_book)
    for i in phone_book:
        n = l.count("/" + i)
        if n > 1:
            return False
    return True

def solution(phone_book):
    l = "/" + "/".join(phone_book)
    for i in phone_book:
        n = l.count("/" + i)
        if n > 1:
            return False
    return True

def solution(pb) :
    heapq.heapify(pb)
    p = heapq.heappop(pb)
    while pb :
        if p==pb[0][:len(p)] : return False
        p = heapq.heappop(pb)
    return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


phone = ["119", "97674223",  '9763' ,"195524421"]

print(solution(phone))


