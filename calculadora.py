def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida!"
    return x / y

def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    opcao = input("Escolha a operação (1/2/3/4): ")

    if opcao in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite números válidos.")
            return

        if opcao == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif opcao == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif opcao == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcao == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calculadora()