- 문제 이해
    - 스파이는 매일 다른 옷 조합
    - 의상이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return
    - cloth = [["yellow_hat", "headgear"],
        
                     ["blue_sunglasses", "eyewear"], 
                     ["green_turban", "headgear"]]
        
    - 2차원 배열은 [의상 종류, 의상 분류]가 원소로 들어가있음
    - 같은 의상 분류가 2번 이상 들어가서는 안됨.
    - 가능한 조합
    
    ```
    1. yellow_hat
    2. blue_sunglasses
    3. green_turban
    4. yellow_hat + blue_sunglasses
    5. green_turban + blue_sunglasses
    ```
    
- 문제 접근 방향
    
    처음 접근 방향
    
    - 의상 분류별로 의상 저장해놓는 딕셔너리 생성
        
        {headgear : [yellow_hat, green_turban],
        
        eyewear : [blue_sunglasses] }
        
    - 딕셔너리 키의 개수만큼 for문 돌면서,
        
        1개짜리 조합의 개수
        2개짜리 조합의 개수
        
        …
        
        len(dict)개짜리 조합의 개수
        의 총 합을 구하려고 했음.
        
    
    그러나.. 방법이 떠오르지 않음
    
    ```python
    import collections
    from itertools import product
    
    def solution(clothes):
        answer = 0
        
        dict_clothes = collections.defaultdict(list)
        
        for c, category in clothes:
            dict_clothes[category].append(c)
        
        for i in range(len(dict_clothes)):
            product(dict_clothes[i], dict_clothes[i+1])
        
        return answer
    ```
    
    정답 접근 방향
    
    - 가상의 옷을 하나 생성해서 그 옷과의 조합으로 구하기
    
    ```python
    import collections
    
    def solution(clothes):
        answer = 0
        
        dict_clothes = collections.defaultdict(list)
        
        for c, category in clothes:
            dict_clothes[category].append(c)
        
        res = 1
        for v in dict_clothes.values():
            res *= (len(v) + 1)
        return res - 1
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/34ba2ce4-547a-4097-af2e-cbbbef2f0eeb/Untitled.png)
