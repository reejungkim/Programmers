def solution(numbers):
    
    l = len(str(max(numbers)))    
    arr = list(map(lambda x: str(x).ljust(l, '0') , numbers))
  
    arr = list(map(int, arr))
    d = dict(zip(numbers, arr)) 
    answer = list(sorted(d, key=lambda x:d[x], reverse=True))  
    
    answer = list(map(str, answer))
    answer = "".join(answer)
    return answer