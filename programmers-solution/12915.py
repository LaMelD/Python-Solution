#programmers 문자열 내 마음대로 정렬하기
def solution(strings, n):
        # n번째로 인덱스로 정렬하고, 그 인덱스가 같다면 사전순으로 정렬
        strings.sort(key = lambda text : (text[n], text))
        return strings
