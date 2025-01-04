def solution(A, B):
    

    return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]


def solution(arr1, arr2):
    answer = []
    
    for i,j in zip(arr1, arr2):
        sum = []
        for n,m in zip(i,j):
            sum.append(n+m)
        answer.append(sum)
    
    return answer