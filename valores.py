import json

with open('dados.json') as file:
    dados =json.load(file)

valores = sorted(item['valor'] for item in dados)
valores = [v for v in valores if v != 0]

total = sum(valores)
dias = len(valores)
media = total/dias

filtro = len([v for v in valores if v > media])

print('o numero de dias cujo o valor ultrapassou a média de R$ {:.2f}, foi: {}'.format(media,filtro))
print('o valor mais baixo do mês foi R$ {:.2f} e o menor R$ {:.2f}.'.format(valores[0], valores[-1]))
