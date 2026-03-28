class animal:
    def _init_(self, especie, idade=None, peso=None, nome=None, dono=None):
        self.especie = especie
        if idade is None:
            idade = input("Digite a nome do animal: ")
        self.nome = nome
        if peso is None:
            peso = input("Digite o peso do animal: ")
        self.peso = peso
        if nome is None:
            nome = input("Digite o idade do animal: ")
        self.idade = nome
        if dono is None:
            dono = input("Digite o nome do dono do animal: ")
        self.dono = dono

    
class cachorro(animal):
    def _init_(self, especie=None, idade=None, peso=None, nome=None, raca=None, dono=None):
        if especie is None:
            especie = "cachorro"
        super()._init_(especie, idade, peso, nome, dono)
        if raca is None:
            raca = input("Digite a raça do cachorro: ")
        self.raca = raca
    def apresentar(self):
        return f"a especie do animal é {self.especie}, seu nome é {self.nome}, sua raça é {self.raca} seu peso é {self.peso}, sua idade é {self.idade}, seu dono é {self.dono}"
class gato(animal):
    def _init_(self, especie=None, idade=None, peso=None, nome=None, raca=None, dono=None):
        if especie is None:
            especie = "gato"
        super()._init_(especie, idade, peso, nome, dono)
        if raca is None:
            raca = input("Digite a raça do gato: ")
        self.raca = raca
    def apresentar(self):
        return f"a especie do animal é {self.especie}, seu nome é {self.nome}, sua raça é {self.raca} seu peso é {self.peso}, sua idade é {self.idade}, seu dono é {self.dono}"
class tartaruga(animal):
    def _init_(self, especie=None, idade=None, peso=None, nome=None, raca=None, dono=None):
        if especie is None:
            especie = "tartaruga"
        super()._init_(especie, idade, peso, nome, dono)
        if raca is None:
            raca = input("Digite a raça do tartaruga: ")
        self.raca = raca
    def apresentar(self):
        return f"a especie do animal é {self.especie}, seu nome é {self.nome}, sua raça é {self.raca} seu peso é {self.peso}, sua idade é {self.idade}, seu dono é {self.dono}"
class passarinho(animal):
    def _init_(self, especie=None, idade=None, peso=None, nome=None, raca=None, dono=None):
        if especie is None:
            especie = "passarinho"
        super()._init_(especie, idade, peso, nome, dono)
        if raca is None:
            raca = input("Digite a raça do passarinho: ")
        self.raca = raca
    def apresentar(self):
        return f"a especie do animal é {self.especie}, seu nome é {self.nome}, sua raça é {self.raca} seu peso é {self.peso}, sua idade é {self.idade}, seu dono é {self.dono}"
class Furão(animal):
    def _init_(self, especie=None, idade=None, peso=None, nome=None, raca=None, dono=None):
        if especie is None:
            especie = "furão"
        super()._init_(especie, idade, peso, nome, dono)
        if raca is None:
            raca = input("Digite a raça do furão: ")
        self.raca = raca
    def apresentar(self):
        return f"a especie do animal é {self.especie}, seu nome é {self.nome}, sua raça é {self.raca} seu peso é {self.peso}, sua idade é {self.idade}, seu dono é {self.dono}"
cachorro1 = cachorro()
print(cachorro1.apresentar()) 

gato1 = gato()
print(gato1.apresentar())

tartaruga1 = tartaruga()

print(tartaruga1.apresentar())

passarinho1 = passarinho()
print(passarinho1.apresentar())

furão1 = Furão()
print(furão1.apresentar())