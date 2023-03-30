from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0]) # word 와 cnt를 같이 queue에 저장함(한꺼번에 확인하려고)
    visited = [0 for i in range(len(words))] # 방문 기록 생성

    while queue: # queue가 빌때까지
        word, cnt = queue.popleft() 
        if word == target: # target 값에 도달했을 경우
            answer = cnt # answer에 cnt저장하고 출력
            break
        for i in range(len(words)): # words를 돌면서
            ndiff = 0 # 다른 문자 개수 셀 변수 초기화
            if visited[i] == 0: # 방문하지 않은 word라면
                for j in range(len(word)): # 해당 문자열의 문자 하나씩 따져보면서
                    if word[j] != words[i][j]:  # 다른 문자와 비교
                        ndiff += 1  # 다른 문자 개수 세기
                if ndiff == 1:  # 만약 서로 다른 문자가 1개 뿐이라면
                    queue.append([words[i], cnt+1]) # 교환!
                    visited[i] = 1 # 해당 문자는 방문했다는 표시 하기

    return answer
