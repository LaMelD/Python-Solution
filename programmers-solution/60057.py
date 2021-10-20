#programmers 문자열 압축
def solution(s):
	ans = len(s)
    # 압축량에 따라서 확인한다.
	for x in range(1, int(len(s)/2) + 1):
        # 총 문자열의 길이
		d = 0
        # 비교 문자열
		comp = ''
        # same count
		c = 1
        
        # 문자열을 search한다.
		for i in range(0, len(s), x):
            #문자열 복사
			temp = s[i:i + x]
            
            # 비교
            # 같다면 count를 늘려준다.
			if comp == temp:
				c += 1
            # 다르다면
            # 총 문자열 길이를 더해주고
            # 비교 문자열을 갱신한다.
			else:
				d += len(temp)
                
                # 1이면 무시, 1초과라면 int형을 str으로 변환하여 길이를
                # 총 문자열 길이에 더한다.
				if c > 1:
					d += len(str(c))
				c = 1
				comp = temp
		
        # 남은 찌꺼기가 있으면
        if c > 1:
			d += len(str(c))
		
        ans = min(ans, d)
	return ans
