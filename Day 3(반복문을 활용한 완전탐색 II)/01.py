# [필수] 덩치_KOI지역2013_초등부_2

num = int(input())
weight = []
height = []

for i in range(num):
	a, b = (map(int, input().split()))
	weight.append(a)
	height.append(b)

score = []
for i in range(num):
	cnt = 1
	for j in range(num):
		if(weight[i] < weight[j] and height[i] < height[j]):
			cnt += 1
	score.append(cnt)	

for i in range(num):
	print(score[i], end=' ')

print()