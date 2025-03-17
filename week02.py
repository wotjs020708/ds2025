import random

r = random.randint(1, 100)

c = 7

for i in range(c):
    n = int(input("정수 입력 : "))
    if r > n:
        print("정답보다 숫자가 큽니다.")
    elif  r < n:
        print("정답보다 숫자가 작습니다.")
    else:
        print("정답입니다.")
        break
    c -= 1
    print("남은 횟수는:", c)
