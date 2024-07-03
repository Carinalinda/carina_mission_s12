from conversor_medidas import ConversorDeMedidas

print('''
[1]. Centimetros para Metros
[2]. Metros para Centimetros 
''')

escolha = input('Escolha uma opção: ')
value = float( input('Digite um valor: '))

if escolha == '1':
    result =  ConversorDeMedidas.centimetros_para_metros(value)
elif escolha == '2':
    result = ConversorDeMedidas.metros_para_centimetros(value)
    
print('Result:',result)