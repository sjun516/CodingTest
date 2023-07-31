# 방 배정하기_KOI전국2017_초등부_2_중등부_1

numbers = list(map(int, input().split()))

for i in range(0, numbers[3]//numbers[0]+1):
	for j in range(0, numbers[3]//numbers[0]+1):
		for k in range(0, numbers[3]//numbers[0]+1):
			if(i*numbers[0]+j*numbers[1]+k*numbers[2] == numbers[3]):
				print(1)
				exit()
print(0)