
- 스택과 큐를 구분하여 사용하기 번거로우므로 한 번에 두 자료형의 특징을 모두 갖고 있는 복합 자료형이 있다면 훨씬 더 편하게 사용 가능
    
    → 데크가 등장!
    
- 데크 = 스택과 큐의 연산 모두 갖고 있는 복합 자료형
- 우선순위 큐 = 추출 순서가 일정하게 정해져 있지 않음

- 원형 큐 구현
    - Front() : 큐의 연산 O
    - Rear() : 큐에 정의되어 있지 않은 연산(데크에 존재하는 연산)

- 데크 = Double-Ended Queue의 줄임말. 글자 그대로 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상 자료형(ADT)
    - 양쪽에서 삭제와 삽입을 모두 처리할 수 있음.
    - 배열이나 연결리스트로 모두 구현이 가능하지만 이중 연결 리스트로 구현하는 편이 가장 잘어울림.
    
    ```python
    >>> import collections
    >>> d = collections.deque()
    >>> type(d)
    <class 'collections.deque'>
    ```
