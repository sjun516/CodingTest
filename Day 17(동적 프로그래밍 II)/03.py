# [필수] 최장 길이 공통 부분 문자열

# 최장 공통 문자열 (공통문자열이 완벽히 일치)
# LCS[i][j] := 문자열 S의 i번째, 문자열 T의 j번째로 끝나는 공통 문자열의 최대 길이
# • S[i] == T[j]: LCS[i][j] = LCS[i-1][j-1]
# • S[i] != T[j]: LCS[i][j] = 0

# 최장 공통 부분 수열 
# LCS[i][j] := 문자열 S의 i번째, 문자열 T의 j번째 문자까지 고려했을 때, LCS 값
# • S[i] == T[j]: LCS[i][j] = LCS[i-1][j-1]
# • S[i] != T[j]: LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]











# 잘못된 풀이 모든걸 처음부터 맞추려고함 굳이 그렇게 안해도됨
arr = list(input())
arr2 = list(input())

dp = [[0 for _ in range(len(arr)+1)] for _ in range(len(arr2)+1)]

cnt = -1
for i in range(1, len(arr2)+1):
	for j in range(1, len(arr)+1):
		dp[i][j] = max(dp[i-1][j], dp[i][j-1])
		if(dp[i][j] < i):
			if(arr2[i-1] == arr[j-1] and j-1 > cnt):
				cnt = j-1
				dp[i][j] += 1
		print(i, j)
		print(dp[i][j])
		
