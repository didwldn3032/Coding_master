"""
내 풀이
"""
answer = 0 # 전역변수로 answer 초기화
def solution(numbers, target):
    global answer # answer 전역변수 선언(재귀 돌꺼니까)
    
    def dfs(idx, res):
        global answer # answer 전역변수 선언(재귀 돌꺼니까)
        if idx == len(numbers): # numbers의 끝에 도달했다면
            if res == target:
                answer += 1
            return
        else:
            dfs(idx + 1, res + numbers[idx]) # 덧셈
            dfs(idx + 1, res - numbers[idx]) # 뺼셈
            
    dfs(0,0) # idx = 0, res = 0으로 초기화 한 후 시작
    return answer
  
  
  """
  다른 방법 풀이
  """
  def solution(numbers, target):
    answer = 0
    overVal = (sum(numbers) - target)//2  # 잉여 값 구하기. 이 값을 만들 경우의 수를 구해야함
    length = len(numbers)

    def recursive(target, idx, cnt):  # 목표 숫자, 리스트에서 현재 위치, 경우 갯수
        for i in range(idx, length):
            temp = target
            temp -= numbers[i]
            if temp == 0:
                cnt += 1
            elif temp > 0:
                cnt += recursive(temp, i+1, 0)
            elif temp < 0:
                continue
        return cnt

    return recursive(overVal, 0, 0)
