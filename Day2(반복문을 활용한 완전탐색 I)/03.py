# Milk Pails_USACO_2016_FEB_BRONZ_1

numbers = list(map(int, input().split()))

sum = 0
for i in range(0, numbers[2]//numbers[0]+1):
	for j in range(0, numbers[2]//numbers[0]+1):
		if(sum == 0 or (i*numbers[0]+j*numbers[1]<=numbers[2] and sum <= i*numbers[0]+j*numbers[1])):
			sum = i*numbers[0]+j*numbers[1]

print(sum)