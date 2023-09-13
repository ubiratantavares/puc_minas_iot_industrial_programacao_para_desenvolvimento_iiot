import funcoes as f

if __name__ == "__main__":

    temperatura = 100
    print("Temperatura: " + str(temperatura))
    f.verificar_status(temperatura)

    metros = f.ler("Digite o valor em metros: ")
    kilometros = f.converter_metro_para_kilometro(metros)
    f.imprimir("Medida da distância em kilometros: ", kilometros)

    celsius = f.ler("Digite o valor da temperatura em graus Celsius: ")
    fahrenheit = f.converter_temperatura_celsius_para_fahrenheit(celsius)
    f.imprimir("Medida da temperatura em graus fahrenheit: ", fahrenheit)

    tensao = f.ler("Digite o valor da tensão: ")
    corrente = f.calcular_corrente(tensao)
    f.imprimir('Valor da corrente: ', corrente)

    f.testar_dimensionamento_de_cabo(10, 7500, 220)
