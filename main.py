from conversor_medidas import ConversorDeMedidas

print('''
[1]. Centimetros para Metros
''')

escolha = input('Escolha uma opção: ')
value = float( input('Digite um valor: '))

if escolha == '1':
    result =  ConversorDeMedidas.centimetros_para_metros(value)

print('Result:',result)