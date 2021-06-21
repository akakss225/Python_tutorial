# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.
# 입출력 예
# begin	target	words	return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.

# 예제 #2
# target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.


# def solution(begin, target, words):
#     answer = 0
#     if not target in words:
#         return answer
    
#     graph = []
#     for i in words:
#         temp = []
#         for j in i:
#             temp.append(ord(j) - 96)
#         graph.append(temp)
    
#     start = []
#     end = []
#     for i in range(len(begin)):
#         start.append(ord(begin[i])-96)
#         end.append(ord(target[i])-96)

#     i = 0
#     while len(list(set(end) - set(start))) != 1:
#         if len(list(set(graph[i]) - set(start))) == 1:
#             start = graph[i]
#             answer += 1
#             graph.pop(i)
#             if len(graph) == i:
#                 i = 0
#         else:
#             i += 1
#     answer += 1
#     return answer


def solution(begin, target, words):
    answer = 0
    # target이 목록 내에 없다면 0 을 리턴
    if target not in words:
        return answer
    
    start = list(begin) # 시작 단어를 list형태로 저장. 쉬운 비교를 위함.
    end = list(target) # 표적 단어또한 똑같이.
    
    stack = [start] # DFS를 위한 스택 생성
    while True:
        cur = stack[-1] # 최종적으로 탐색 순서를 stack의 길이로 출력하기 위해 pop이 아닌 peek으로.
        differ1 = 0 # 목적하는 단어와의 차이를 확인하기 위한 변수
        for i in range(len(cur)):
            if cur[i] != end[i]: differ1 += 1
        if differ1 == 1: return len(stack)
        
        for word in words: # 목록을 돌면서 확인 시작
            differ2 = 0
            for j in range(len(start)): 
                if cur[j] != word[j]: differ2 += 1 # stack의 마지막 원소와 목록 내의 단어의 구성이 다를떄마다 differ += 1
            if differ2 == 1: # 만약 차이가 1개뿐이면,
                stack.append(list(word)) # 스택에 넣어주고
                words.remove(word) # 그 단어를 지워줌.
                break # 스택에 넣었으면 for 문을 종료 << while 문을 통해 다시 for 문으로 돌아올 예정.

begin = 'hit'
target = 'cog'
words = ['cog', 'log', 'lot', 'dog', 'dot', 'hot'] 
words = ["hot", "dot", "dog", "lot", "log", "cog"]

begin = "hit"
target = "hhh"
words = ["hhh","hht"]

print(solution(begin, target, words))