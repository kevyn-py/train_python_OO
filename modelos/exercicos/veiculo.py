from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo


    @abstractmethod
    def ligar():
        pass


class Carro(Veiculo):
    def __init__(self,marca,modelo,ano):
        super().__init__(marca,modelo)
        self._ano = ano

    def ligar(self):
        print(f'O carro {self._modelo} está ligado')


