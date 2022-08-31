

class Carro:
    def __init__(self, marca, rodas, cor):
        self.marca = marca
        self.rodas = rodas
        self.cor = cor
    
    def Andar(self):
        print("Estou dirigindo o carro")

    def ExibirInformacao(self):
        print(self.marca, self.rodas, self.cor)




carro1 = Carro("gol", 4, "azul")
carro1.Andar()
carro1.ExibirInformacao()
