# IDEA
# 제공된 number의 index는 고정된 상태로, 제거할 숫자의 갯수 k가 주어졌을 때
# 제거후, 가장 큰 숫자가 되게 해야함
# 1. 되도록이면, max값이 맨 앞에 오는게 좋음
# 2. 앞에서부터 확인해서, 작은 숫자를 일단 지우는게 좋음
# 3. 만약 제거할 숫자만큼 앞 숫자가 작은것만 있다면, 앞숫자만 다 지우는게 좋음
# 4. 맨앞에 적당히 큰 숫자가 왔다면, 그 뒤의 숫자 중 작은걸 지우면 됨.


# 4 * n * (n - 1) ? 대략 O(4N^2)...
def solution(number, k):
    # k 번 반복하는 반복문
    # 연산을 최소화하기 위해 for문 사용
    for i in range(k):
        # 각 숫자를 비교하기 위한 list생성
        # 반복문을 줄이기 위해 첫번째 element를 미리 넣어줌
        nums = [number[1:]]
        
        # 숫자를 선택했는지 체크함
        check = 0
        
        # 두번째 숫자부터 split하기 때문에 1로 설정
        idx = 1
        while idx < len(number):
            # 만일, 현재 인덱스 넘버가 0 이라면, 지우면됨.
            # 0 보다 작은 수는 없기 때문
            if number[idx] == "0":
                number = number[:idx] + number[idx+1:]
                check = 1
                break
            
            # 반복되는 숫자를 건너뛰기 위한 반복문
            while idx < len(number) - 1:
                if number[idx] == number[idx + 1]:
                    idx += 1
                else:
                    break
                
            # 이후 split 된 숫자가 list 마지막 요소보다 크거나 같다면
            # list에 넣어주고, 다음 숫자를 찾으러 감.
            num = number[:idx] + number[idx+1:]
            if nums[-1] <= num:
                nums.append(num)
                idx += 1
            # 만일 split된 숫자가 list 마지막 요소보다 작다면
            # list 마지막 요소가 가장 큰 수가 됨.
            else:
                check = 1
                number = nums[-1]
                break
        # 반복문을 그냥 빠져나온건지 확인
        # 그냥 빠져나왔다면, 마지막 요소가 가장 큰 수가 됨.
        if check == 0:
            number = nums[-1]
    return number


number = "1924"
k = 2
# number = "1231234"
# k = 3
# number = "4177252841"
# k = 4
number = '77777777777777777777778'
k = 3
# number = "1000000000000000000000000000000000000000000"
# k = 1


print(solution(number, k))