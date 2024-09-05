string = str(input('insira a frase que você quer que fique invertida: '))
res = ''.join(res[::-1] for res in string.split()) 
print(res)