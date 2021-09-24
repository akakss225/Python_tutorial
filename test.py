def solution(numbers, hand):
    answer = []
    arr = numbers
    main = hand
    
    key = [
        [10, 7, 4, 1],
        [0, 8, 5, 2],
        [11, 9, 6, 3]
    ]
    lHand = 10
    rHand = 11
    
    for i in arr:
        if i == 1 or i == 4 or i == 7:
            answer.append("L")
            lHand = key[0].index[i]
        elif i == 3 or i == 6 or i == 9:
            answer.append("R")
            rHand = key[2].index[i]
        else:
            
    
    return answer


