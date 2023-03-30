from collections import deque

def solution(maps):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    r = len(maps)
    c = len(maps[0])

    graph = [[0 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1 # (1,1)부터 시작하므로 1 넣어주고 시작

    while queue:
        y, x = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1: 
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    answer = graph[-1][-1] # 1,1부터 탐색하기 위해 -1,-1 넣어줌
    return answer
