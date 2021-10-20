# programmers 정수 제곱근 판별
def solution(n):
        sqr = int(n ** 0.5)
        tmp = sqr
        if tmp ** 2 == n:
                return (sqr + 1) ** 2
        else:
                return -1
