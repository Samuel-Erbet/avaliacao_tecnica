import math

print('escolha um numero para analisar se ele está na sequência de fibonnaci: ')
num = int(input())
fibonacci=[]
for i in range(num):
    fib_num=  int((1/math.sqrt(5)) * (((1 + math.sqrt(5)) / 2)**i - ((1 - math.sqrt(5)) / 2)**i))
    fibonacci.append(fib_num)
    print(fibonacci)

if num in fibonacci:
    print('seu numero está na sequencia de fibonacci')
else:
    print('seu numero não está na sequência de fibonacci')