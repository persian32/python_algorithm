import sys
sys.stdin = open("input.txt", "rt") # 파일로 입력받을 때 사용

# 패턴 A: 숫자 뒤집기
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10    # 마지막 자리 숫자 추출
        res = res * 10 + t
        x = x // 10   # 마지막 자리 제거
    return res

# 패턴 B: 소수 판별하기
def isPrime(x):
    if x == 1: # 1은 소수가 아님
        return False
    # 2부터 자기자신의 절반(또는 제곱근)까지 나누어 떨어지는지 확인
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

# 메인 실행부
n = int(input()) # 숫자의 개수 (예: 3)
a = list(map(int, input().split())) # 숫자 리스트 (예: 32 55 62)

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')