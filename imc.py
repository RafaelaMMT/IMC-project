resposta = 'sim' #Laço de repetição início
while resposta == 'sim':
    def calcularIMC(peso, altura):
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        return imc

    # Pede as informações da pessoa
    nome = input("Digite o seu nome: ")
    altura = float(input("Digite a sua altura em metros: "))
    peso = float(input("Digite o seu peso em kg: "))
    
    
    # Calcula o IMC
    imc = calcularIMC(peso, altura)

    # Exibe o resultado do IMC
    print(f"{nome} o seu IMC é: {imc:.2f}")

    # Classificação do IMC
    # Utilização if/elif e else
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    elif 30 <= imc < 34.9:
        print("Classificação: Obesidade grau I")
    elif 35 <= imc < 39.9:
        print("Classificação: Obesidade grau II")
    else:
        print("Classificação: Obesidade grau III ou mórbida")
    
    # Laço de repetição final/ ele foi usado para caso a pessoa deseja fazer outro cálculo 
    resposta = input("Deseja calcular um novo IMC(escreva apenas sim ou não)?: ")
