num = int(input())
nlist = []
for _ in range(num):
	a, b = map(int, input().split())
	nlist.append((a, b))
	
alld = []
jumpd = []

for i in range(num-1):
	d = abs(nlist[i][0] - nlist[i+1][0]) + abs(nlist[i][1] - nlist[i+1][1])
	alld.append(d)
	if(i != num - 2):
		d = abs(nlist[i][0] - nlist[i+2][0]) + abs(nlist[i][1] - nlist[i+2][1])
		jumpd.append(d)

# print(alld, len(alld))
# print(jumpd, len(jumpd))

resultd = []

for i in range(len(jumpd)):
	d = sum(alld) - alld[i] - alld[i+1] + jumpd[i]
	resultd.append(d)

print(min(resultd))
	
		