def ler(mensagem):
    return float(input(mensagem))

def verificar_status(temperatura):
    if temperatura > 100:
        status = "Emergência"
    else:
        status = "Ok"
    print("Status: " + status)

def converter_metro_para_kilometro(valor_metros):
    return valor_metros/1000

def converter_temperatura_celsius_para_fahrenheit(valor_celsius):
    return 9 * valor_celsius / 5 + 32

def calcular_corrente(tensao, resistor=0.1):
    return tensao/resistor

def imprimir(mensagem, valor):
    print(mensagem + str(valor))

def testar_dimensionamento_de_cabo(secao, potencia, tensao):
    # secao tranversal do cabo: corrente suportada pela seção nominal
    dic = {1.5: 15.5, 2.5: 21, 4: 28, 6: 36, 10: 50, 16: 66, 25: 89, 
           35: 111, 50: 134, 70: 171, 95: 207, 
           120: 239, 150: 272, 185: 310, 240: 364, 
           300: 419, 400: 502, 500: 578} 
    if secao in list(dic.keys()):
        # potencia = tensao * corrente
        corrente = potencia / tensao
        if corrente <= dic[secao]:
            print("Bom")
        else:
            print("Ruim")