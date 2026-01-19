import sys
sys.stdin = open("input.txt", "rt")

# 입력받기
n = int(input())
a = list(map(int, input().split()))

print("읽어온 리스트:", a)

sum = 0   # 총 점수
cnt = 0   # 연속 맞힘 횟수 (가산점 카운트)

for x in a:
    if x == 1:
        cnt += 1      # 맞히면 카운트를 1 증가
        sum += cnt    # 증가된 카운트만큼 점수에 누적
    else:
        cnt = 0       # 틀리면 카운트를 0으로 초기화 (중요!)

print(sum)