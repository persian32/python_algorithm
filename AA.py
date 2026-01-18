import sys
# 1. 입력 받기 (input.txt에 숫자 하나만 있다고 가정)
sys.stdin = open("input.txt", "rt")
n = int(input())

# 2. 체크 리스트 만들기 (패턴 1)
ch = [0] * (n + 1)
cnt = 0

# 3. 배수 지우기 로직 (패턴 2)
for i in range(2, n + 1):
    if ch[i] == 0:  # 지워지지 않았다면 소수!
        cnt += 1
        for j in range(i, n + 1, i): # i의 배수들 몽땅 지우기
            ch[j] = 1

print(cnt)