from modelos.servicos.item_servico import ItemServico

class Pintura(ItemServico):
    def __init__(self,descricao,mao_de_obra,tipo_pintura):
        super().__init__(descricao,mao_de_obra)
        self._tipo_pintura = tipo_pintura

    def __str__(self):
        return self._descricao

    #Método abstrato
    def aplicar_desconto(self):
        self._mao_de_obra -= (self._mao_de_obra * 0.15)