def soma(x, y):
    print(x + y)

def sub(x, y):
    print(x - y)

def multi(x, y):
    print(x*y)

def div(x, y):
    print(x/y)

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Escolha uma operação: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if(opcao == 1):
    soma(num1, num2)

if(opcao == 2):
    sub(num1, num2)

if(opcao == 3):
    multi(num1, num2)

if(opcao == 4):
    if(num1 != 0 // num2 != 0):
        div(num1, num2)
    else:
        print("Não é possível dividir algum número por 0!")