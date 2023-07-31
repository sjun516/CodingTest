# [필수] 표지

num = int(input())
new = []
old = ""
for i in range(num):
	if(i == 0):
		old = input()
	a = input()
	new.append(a)
	
cnt = 0
for i in range(num): # 문자열 한개 선택 
	sen = new[i]
	check = 0
	for j in range(len(sen)): # j+d*k 기준으로 체크
		if(check == 1):
			break
		for d in range(1, len(sen)):
			if(check == 1):
				break
				
			index = 0
			for k in range(len(sen)):
				if(j + k*d >= len(sen)): # 인덱스 범위 체크
					break
					
				if(sen[j+k*d] == old[index]): # 한글자 맞으면 다음글자 체크
					#print(sen, j ,d, k)
					index += 1
				else: # 한번이라도 틀릴시 다시
					index = 0
				
				if(index == len(old)): # 모든것이 다 맞음
					# print(sen)
					cnt +=1
					check += 1
					break
				
print(cnt)