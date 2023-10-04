import random
dado = []

num = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6

def lancamento():
    num = random.randint(1, 6)
    dado.append(num)

for i in range(99):
    lancamento()

count = dado.count(num)
count2 = dado.count(num2)
count3 = dado.count(num3)
count4 = dado.count(num4)
count5 = dado.count(num5)
count6 = dado.count(num6)

print(dado)

print(f'O número {num} apareceu {count} vezes na lista.')
print(f'O número {num2} apareceu {count2} vezes na lista.')
print(f'O número {num3} apareceu {count3} vezes na lista.')
print(f'O número {num4} apareceu {count4} vezes na lista.')
print(f'O número {num5} apareceu {count5} vezes na lista.')
print(f'O número {num6} apareceu {count6} vezes na lista.')