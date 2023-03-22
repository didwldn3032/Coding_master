import collections
import math

def solution(progresses, speeds):
    answer = []
    cnt = 0
    
    # 100%가 될 때까지 걸리는 일수 기록
    days = [math.ceil((100-p)/speeds[i]) for i, p in enumerate(progresses) ]
    
    # 첫날 값으로 초기화
    release_day = days[0]
    
    for i, day in enumerate(days):
        if i > 0 and release_day < day:
            answer.append(cnt)
            release_day = day
            cnt = 1
        else:
            cnt += 1
        if i == len(days)-1:
            answer.append(cnt)

    return answer
