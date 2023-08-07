# [필수] 출퇴근

N = int(input())
arr = set()
for _ in range(N):
	staff, record = input().split()
	if(record == "leave"):
		arr.remove(staff)
	else:
		arr.add(staff)
sub = list(arr)
sub.sort()
print(len(arr))
for a in sub:
	print(a)