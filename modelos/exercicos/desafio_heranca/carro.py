from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,modelo,portas):
        super().__init__(marca,modelo)
        self._portas = portas

    def __str__(self):
        return f'{super().__str__()} - Portas: {self._portas}' #Aplicando o modelos especial str que estenda da classe Pai(veiculo) e inclu mais informações da classe filha(carro)
