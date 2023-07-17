# [필수] 삼각화단 만들기(S)

num = int(input())

cnt = 0
for i in range(1, num-1):
	for j in range(i, num-1):
		for k in range(j, num-1):
			if(i+j+k == num and k < i+j):
				cnt+=1
print(cnt)