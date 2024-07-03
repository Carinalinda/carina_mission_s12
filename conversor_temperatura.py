class ConversorDeTemperatura:
    def __init__():
        pass

    def celsius_para_fahrenheit(valor_celsius):
        return valor_celsius * (9/5) + 32

    def fahrenheit_para_celsius(fah_value):
        return (fah_value - 32) / (9/5)

#Area de Teste
result = ConversorDeTemperatura.fahrenheit_para_celsius(32)
print('result', result)