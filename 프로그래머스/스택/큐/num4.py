# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices	            return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# 입출력 예 설명
# 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
# 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
# 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
# 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
# 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.




# 효율성 실패
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         count = 0
#         a = prices.pop(0)
#         for j in prices:
#             if a <= j:
#                 count += 1
#             else:
#                 if j:
#                     count+=1
#                 break
#         answer.append(count)
#     return answer

# 효율성 실패
# def solution(prices):
#     answer = []
#     while len(prices) != 0:
#         a = prices.pop(0)
#         count = 0
#         for i in prices:
#             if a <= i:
#                 count += 1
#             else:
#                 if i:
#                     count += 1
#                 break
#         if len(prices) == 0:
#             count = 0
#             answer.append(count)
#         else:
#             answer.append(count)
#     return answer

# 효율성 실패
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         count = 0
#         a = prices.pop(0)
#         for j in prices:
#             if a <= j:
#                 count += 1
#             else:
#                 if j:
#                     count+=1
#                 break
#         answer.append(count)
#     return answer

# 스택을 사용하지 않은 방법
# def solution(prices):
#     answer = [0 for i in range(len(prices))]
    
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             answer[i] += 1
#             if prices[i] > prices[j]:
#                 break
#     return answer


# 스택을 사용한 방법. 가장 빠르면 O(2n)의 시간으로 해결 가능.
def solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices) - i -1)
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                # 현재 시점과 스택에서 꺼낸 값의 차를 저장한다.
                answer[index] = i - index
                stack.pop()
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
        
    return answer




prices = [1, 2, 3, 2, 3]
print(solution(prices))

