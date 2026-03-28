def cadastro():
    nome = input("Digite seu nome: ")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Diretoria")
    cargo = int(input("Sua função: "))

    if(cargo == 1):
        idade = int(input("Digite sua idade: "))
        curso = input("Digite seu curso: ")
        serie = input("Digite sua série: ")
        matricula = input("Digite sua matrícula: ")
        escolha()

    if(cargo == 2):
        id = int(input("Digite seu Identificador(ID): "))
        mat = input("Digite a sua área de ensino: ")
        professor()

def escolha():
        
    print("1 - Biblioteca")
    print("2 - Cárdapio")
    print("3 - Horário")
    print("4 - Avaliar Professor")
    print("5 - Checar Média")
    print("0 - Sair do Sistema")

    opcao = int(input("O que fazer? Escolha: "))

    if(opcao == 1):
        biblioteca()
    elif(opcao == 2):
        cardapio()
    elif(opcao == 3):
        hora()
    elif(opcao == 4):
        ava()
    elif(opcao == 5):
        media()
    elif(opcao == 0):
        print("Fim do Sistema.")
    else:
        print("Escolha Inválida!")
        escolha()

def biblioteca():
            
            print("Livros Disponiveis: ")

            print("1 - O Guarani")
            print("2 - Jujutsu Kaisen")
            print("3 - Blue Lock")
            print("4 - Extraordinário")
            print("5 - O Conto de Ratão")
            print("6 - Sair da Biblioteca")

            op1 = int(input("Digite sua escolha: "))

            if(op1 == 6):
                escolha()

            if(op1 == 1):
                print("Você alugou 'O Guarani'!")
                escolha()
            if(op1 == 2):
                print("Você alugou 'Jujutsu Kaisen'!")
                escolha()
            if(op1 == 3):
                print("Você alugou 'Blue Lock'!")
                escolha()
            if(op1 == 4):
                print("Você alugou 'Extraordinário'! ")
                escolha()
            if(op1 == 5):
                print("Você alugou 'O Conto de Ratão'!")
                escolha()

def cardapio():
    print("--------- CARDÁPIO ---------")
    print("Seg-Ter: Arroz com Feijão/Frango Assado")
    print("Qua-Qui: Arroz com Macarrão/Frango Cozido")
    print("Sex: Arroz/Feijoada")

    escolha()

def hora():
     
    print("1 - Segunda")
    print("2 - Terça")
    print("3 - Quarta")
    print("4 - Quinta")
    print("5 - Sexta")

    hor = int(input("Escolha qual dia checar: "))

    if(hor == 1):
        print("Geografia")
        print("Geografia")
        print("Matemática")
        print("Matemática")
        print("Português")
        print("Português")
        escolha()
    elif(hor == 2):
        print("História")
        print("História")
        print("Projeto de Vida")
        print("Artes")
        print("Educação Fisica")
        print("Educação Fisica")
        escolha()
    elif(hor == 3):
        print("Inglês")
        print("Inglês")
        print("Matemática")
        print("Matemática")
        print("Português")
        print("Biologia")
        escolha()
    elif(hor == 4):
        print("Fisica")
        print("Fisica")
        print("Quimica")
        print("Quimica")
        print("Português")
        print("Português")
        escolha()
    elif(hor == 5):
        print("Geografia")
        print("Geografia")
        print("Matemática")
        print("Matemática")
        print("Português")
        print("Português")
        escolha()
    else:
        print("Escolha Inválida!")
        escolha()

def ava():
    print("Escolha o Professor")
    print("1 - Joana/Port")
    print("2 - Jonas/Geo")
    print("3 - Lucas/Mat")
    print("4 - Salvador/Hist")
    
    prof = input("Qual professor você quer avaliar? Digite: ")
    avl = input("Qual a nota você dá para esse professor(a)? Nota: ")

    escolha()

def media():
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    n3 = float(input("Digite sua terceira nota: "))

    media = (n1+n2+n3)/3

    print(f"Sua média é {media}")

    if(media > 6):
         print("Você foi aprovado!")
         escolha()
    else:
         print("Você foi reprovado. Melhore!")
         escolha()
def professor():

    print("1 - Turmas")
    print("2 - Cárdapio")
    print("3 - Horário")
    print("4 - Passar Notas")
    print("5 - Material")
    print("0 - Sair do Sistema")

    opcao = int(input("O que fazer? Escolha: "))

    #if(opcao == 1):
    #    turmas()
    #elif(opcao == 2):
    #    cardapio()
    #elif(opcao == 3):
    #    horap()
    #elif(opcao == 4):
    #    pnota()
    #elif(opcao == 5):
    #    mat()
    #elif(opcao == 0):
    #    print("Fim do Sistema.")
    #else:
    #    print("Escolha Inválida!")
    #    professor()
    





cadastro()