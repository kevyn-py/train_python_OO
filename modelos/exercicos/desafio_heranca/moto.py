from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self,marca,modelo,tipo):
        super().__init__(marca,modelo)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} + Tipo da moto: {self._tipo}'