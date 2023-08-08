# [필수] 3이하로 분할하기
# 재귀

def case(n):
	cnt = 0
	if(n >= 3):
		cnt += case(n-3)
	if(n >= 2):
		cnt += case(n-2)
	if(n >= 1):
		cnt += case(n-1)
	if(n == 0):
		return cnt + 1
	return cnt

T = int(input())
for _ in range(T):
	n = int(input())
	print(case(n))