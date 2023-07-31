# [필수] 평균이 들어있는 구간 구하기

num = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(num):
	for j in range(i, num):
		sum = 0
		for k in range(i, j+1):
			sum += nums[k]
		avg = sum / (j-i+1)
		for k in range(i, j+1):
			if(nums[k] == avg):
				cnt += 1
				break

print(cnt)