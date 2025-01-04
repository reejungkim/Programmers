

def solution(score):
    scores = [sum(s)/2 for s in score]
    sorted_scores = sorted(scores, reverse=True)
    
    ranks = [sorted_scores.index(score) +1 for score in scores]
    answer = ranks
    return answer