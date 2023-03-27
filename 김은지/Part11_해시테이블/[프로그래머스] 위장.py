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
