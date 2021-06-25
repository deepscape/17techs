import random


# 랜덤 값을 열번 출력
for i in range(1, 10):
    # seed 값을 0 으로 고정
    random.seed(0)
    print(random.randrange(1, 10))