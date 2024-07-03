from conversor_medidas import ConversorDeMedidas
from conversor_temperatura import ConversorDeTemperatura

print('''
[1]. Centimetros para Metros
[2]. Metros para Centimetros 
[3]. Celsius para fahrenheit
[4]. Fahrenheit para celsius
''')

escolha = input('Escolha uma opção: ')
value = float( input('Digite um valor: '))

if escolha == '1':
    result =  ConversorDeMedidas.centimetros_para_metros(value)
elif escolha == '2':
    result = ConversorDeMedidas.metros_para_centimetros(value)
elif escolha == '3':
    result = ConversorDeTemperatura.celsius_para_fahrenheit(value)
else:
    result = ConversorDeTemperatura.fahrenheit_para_celsius(value)
print('Result:',result)