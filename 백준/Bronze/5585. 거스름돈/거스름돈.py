import sys

taro = 1000-int(sys.stdin.readline())

moneys = [500,100,50,10,5,1]

result = 0 

for money in moneys:
    if taro//money > 0:
        result+=taro//money
        taro%=money

    if taro == 0:
        break

print(result)