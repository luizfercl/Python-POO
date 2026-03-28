class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")

    def frear(self, valor):
        self.velocidade -= valor

        if self.velocidade < 0:
            self.velocidade = 0
            print(f"{self.modelo} reduziu para {self.velocidade} km/h.")

    def detalhes(self):
         return (f"{self.marca} {self.modelo} ({self.ano}) - " f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")
    
moto1 = Moto("Yamaha", "Tracer 900", 2020, "Azul")
moto2 = Moto("Ducati", "Panigale V6 S", 2025, "Prata")

moto1.acelerar(50)
#print(moto1.detalhes())

moto2.acelerar(100)
#print(moto2.detalhes())

if (moto1.velocidade > moto2.velocidade):
    print(f"{moto1.modelo} está em {moto1.velocidade} km/h, maior que a de {moto2.modelo}, que está em {moto2.velocidade}.")
else:
    print(f"{moto2.modelo} está em {moto2.velocidade} km/h, maior que a de {moto1.modelo}, que está em {moto1.velocidade}.")

moto1.frear(60)
#print(moto1.detalhes())
moto2.frear(110)
#print(moto2.detalhes())
