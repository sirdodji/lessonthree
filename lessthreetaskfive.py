from random import random
n = round(random() * 10)
i = 1
print("AI made a number. You have 3 tries")
while i <= 3:
    u = int(input(str(i) + '-try: '))
    if u > n:
        print('You lose')
    elif u < n:
        print('You lose')
    else:
        print('You win')
        break
    i += 1
else:
    print('Game over')
