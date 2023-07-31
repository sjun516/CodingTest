# [필수] 3장으로 하는 블랙잭

a, b = map(int, input().split())
numbers = list(map(int, input().split()))

sum = 0
for i in range(a):
	for j in range(i+1, a):
		for k in range(j+1, a):
			num = numbers[i] + numbers[j] + numbers[k]
			if(num <= b and (sum == 0 or sum < num)):
				sum = num
				
print(sum)