# 처음 풀이 4/20
import collections

def solution(priorities, location):
    answer = 0 # 내가 원하는 원소의 위치
    
    # 내가 원하는 원소의 위치만 1로 나머지는 0으로 deque 생성
    idxs = [0] * len(priorities)
    idxs[location] = 1
    idxs = collections.deque(idxs)
    
    queue = collections.deque(priorities)
    
    while queue:
        doc = queue.popleft()
        # doc보다 큰 값이 있으면
        if doc < max(queue):
            idx = idxs.popleft()
            idxs.append(idx)
            queue.append(doc)
        # doc보다 큰 값이 없으면
        else:
            return idxs.index(1) + 1
    
    return idxs.index(1) + 1
  
  
# 맞은 풀이
import collections

def solution(priorities, location):
    answer = 0 # 내가 원하는 원소의 위치
    
    # 내가 원하는 원소의 위치만 1로 나머지는 0으로 deque 생성
    idxs = [0] * len(priorities)
    idxs[location] = 1
    idxs = collections.deque(idxs)
    print(idxs)
    
    queue = collections.deque(priorities)
    
    while queue:
        doc = queue.popleft()
        idx = idxs.popleft()
        #print(idx)
        # doc보다 큰 값이 있으면
        if len(queue) > 1 and doc < max(queue):
            idxs.append(idx)
            queue.append(doc)
        # doc보다 큰 값이 없으면
        else:
            answer += 1
            if idx == 1:
                return answer
    
    return answer
