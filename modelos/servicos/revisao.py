from modelos.servicos.item_servico import ItemServico

class Revisao(ItemServico):
    def __init__(self,descricao,mao_de_obra, km_veiculo, qtd_itens_checados):
        super().__init__(descricao,mao_de_obra)
        self._km_veiculo = km_veiculo
        self._qtd_itens_checados = qtd_itens_checados

    def __str__(self):
        return self._descricao