from abc import ABC, abstractmethod

class ItemServico(ABC):
    def __init__(self,descricao,mao_de_obra):
        self._descricao = descricao
        self._mao_de_obra = mao_de_obra

    #Criando um método abstrato - um molde para classes derivadas. Todas as classes derivadas terão que ter esse metodo abstrato
    @abstractmethod
    def aplicar_desconto(self):
        pass
    