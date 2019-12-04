#programmers 소수 찾기
def solution(n):
        answer = 0
        eratos = []
        for i in range(0, 1000002):
                eratos.append(True)
        
        for i in range(2, n + 1):
                if eratos[i]:
                        answer += 1
                        tmp = i + i
                        while tmp <= 1000000:
                                eratos[tmp] = False
                                tmp += i
        return answer
