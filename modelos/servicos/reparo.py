from modelos.servicos.item_servico import ItemServico

class Reparo(ItemServico):
    def __init__(self,descricao,mao_de_obra,valor_pecas):
        super().__init__(descricao,mao_de_obra)
        self._valor_pecas = valor_pecas

    def __str__(self):
        return self._descricao