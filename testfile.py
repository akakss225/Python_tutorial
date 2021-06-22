'''
1. 논리적 추론 == 거짓말 A, 빵먹 B

2. 페턴찾기 == 답 71

3. 반복구조 답 == 15

4. 조건식 == count < 101

5. 논리식 == 3번 (year % 4 != 0 && year % 100 == 0) || year % 400 != 0
'''

# 6 번 구현
'''
arr = [3,2,4,4,2,5,2,5,5]
answer = [0] * len(arr)
result = []

for i in arr:
    answer[i-1] += 1
for i in answer:
    if i > 1:
        result.append(i)
if result:
    print(result)
else:
    print(-1) 
'''

