def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for com in range(n): # 컴퓨터의 개수대로 dfs 돌면서
        if visited[com] == 0: # 아직 방문하지 않은 컴퓨터라면
            dfs(n, computers, com, visited)
            answer += 1 # 네트워크 수 count
    return answer

def dfs(n, computers, com, visited):
    visited[com] = 1
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: # 컴퓨터가 서로 연결됐다면
            if visited[connect] == 0:   # 그리고 방문 기록이 0이라면 
                dfs(n, computers, connect, visited) # 재귀 돌기 & 기록
