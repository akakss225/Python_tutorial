def solution(nums):
    answer = 0
    take = len(nums)/2
    x = set(nums)
    if len(x) > take:
        return take
    else:
        return len(x)
    
    return answer

nums = [3,1,2,3]