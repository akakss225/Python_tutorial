from itertools import permutations
# def solution(numbers):
#     a = sorted(numbers)
#     max = 0
#     max_index = 0
#     check = 1
#     for i in range(len(a)):
#         if a[i] < 10:
#             max = a[i]
#             max_index = i
#         else:
#             check = 1
#             for j in range(1, len(str(a[i]))):
#                 if max > int(str(a[i])[j]):
#                     check = 0
#                     break
#                 if j == len(str(a[i]))-1 and max == int(str(a[i])[j]):
#                     check = 0
#                     break
#             if check == 0:
#                 continue
#             else:
#                 max = a[i]
#                 max_index = i
#     a.pop(max_index)
#     per = list(permutations(a, len(a)))
#     for i in range(len(per)):
#         cur = "".join(map(str,per[i]))
#         per[i] = cur
#     per.sort()
#     return str(max) + per[-1]

def solution(numbers):
    per = map(lambda x: int("".join(map(str, x))), permutations(numbers, len(numbers)))
    return str(max(per))


numbers = [3, 30, 34, 5, 9]
numbers = [114, 115, 23, 28, 9, 93]
# numbers = [6, 10, 2]
# numbers = [34, 3, 35, 33]

print(solution(numbers))

