#https://myjamong.tistory.com/317
import sys

a_word = list(sys.stdin.readline().rstrip())
b_word = list(sys.stdin.readline().rstrip())
dp = [0]*(len(b_word))
for i in range(len(a_word)):
    cnt = 0 # 한 행씩 크기 비교
    for j in range(len(b_word)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif a_word[i] == b_word[j]:
            dp[j] = cnt+1
print(max(dp))