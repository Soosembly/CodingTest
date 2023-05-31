def solution(start, end):
    answer = []
    
    for i in range(start, end+1):
        answer.append(i)
    return answer
    
    

# lambda

solution = lambda start, end: [i for i in range(start, end+1)]

