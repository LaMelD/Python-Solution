# programmers 예산
def solution(d, budget):
        d.sort()
        answer = 0
        for idx in d:
                if idx <= budget:
                        budget -= idx
                        answer += 1
        return answer
