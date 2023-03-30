- 문제 이해
    - begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾기
    - 단 변환 규칙은 아래와 같음
        - 한 번에 한 개의 알파벳만 바꿀 수 있다.
        - words에 있는 단어로만 변환할 수 있다.
    - ex) begin : “hit”, target : “cog”, words : [”hot","dot","dog","lot","log","cog”]
    
- 문제 접근 방향
    - begin의 단어를 words에서 찾고 visted = 1처리
    - begin의 한 글자를 바꿨을 때 그 글자가 words에 있는지 check
    or begin과 words에 begin을 제외한 글자 중 다른 글자가 하나인 글자 찾기
    - 위의 조건을 확인한 후 한 글자 바꿔서 또 위의 과정 반복 (이럴때마다 cnt+=1)
    - words를 다 탐색할 때까지 target이 나오면 cnt 횟수 출력, 아니면 0 출력하도록 return
