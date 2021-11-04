def solution(nums):
    take = len(nums)/2
    x = set(nums)
    if len(x) > take:
        return take
    else:
        return len(x)

nums = [3,1,2,3]