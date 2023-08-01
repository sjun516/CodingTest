# [필수] Counting Haybales_USACO_2016_DEC_SILVER_1

from bisect import bisect_left, bisect_right 

# upper_bound(k) – lower_bound(k) 를 하면 k의 개수를 알 수 있다.
# upper_bound(b) – lower_bound(a) 를 하면 a부터 b까지의 개수를 알 수 있다.

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(Q):
	a, b = map(int, input().split())
	print(bisect_right(arr, b) - bisect_left(arr, a))