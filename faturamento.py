sp= float(67.83643)
rj= float(36.67866)
mg= float(9.22988)
es= float(7.16548)
outros= float(19.84953)
total= sp+rj+mg+es+outros
res = ''

print('escolha um estado para saber a porcentagem:')
est=str(input())
if est == 'sp':
    res = (sp*100)/total
    print('a porcentagem de são paulo é {:.2f}%'.format(res))
elif est == 'rj':
    res =(rj*100)/total
    print('a porcentagem do rj é {:.2f}%'.format(res))
elif est == 'mg':
    res =(mg*100)/total
    print('a porcentagem de mg é {:.2f}%'.format(res))
elif est == 'es':
    res =(es*100)/total
    print('a porcentagem do rj é {:.2f}%'.format(res))    
elif est == 'outros':
    res =(outros*100)/total
    print('a porcentagem do rj é {:.2f}%'.format(res))    
else:
    print('ERRO, insira o nome de um estado válido.')