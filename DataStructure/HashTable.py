# 해시 테이블의 개념을 알 수 있다
# 기본적으로 해시테이블은 key와 value로 이루어진 자료구조이다 >> like Dictionary
# list와 다른점은, list에선 특정 값을 찾을 경우 O(n)의 시간을 사용한다 >> 처음부터 돌면서 확인해야함
# 하지만 Hash의 경우, Key를 이용해 찾기 때문에 상수시간을 사용한다 O(1)
# Hash에서 가장 중요한 것은, Hash Algorithm이다.
# 이는 Hash Function을 사용해 Hash Code를 설정하고, 이를 index화 하는데에 있어,
# 얼마나 고루고루 분포시킬지에 따라서 좋은 Algorithm인지, 아닌지를 판단한다.

# Step.1 리스트를 만든다
