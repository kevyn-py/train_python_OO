from modelos.carros import Carro
from modelos.servicos.reparo import Reparo
from modelos.servicos.revisao import Revisao
from modelos.servicos.pintura import Pintura

#intanciando com metodo contrutor
carro_civic = Carro('Civic','Honda',2004)

#Instanciando o serviço reparo
reparo_pintura = Reparo('Pintura no para-choque frontal',250,2)
 # aplicando o desconto 
reparo_pintura.aplicar_desconto()

#Instanciando o serviço revisao
revisao_oleo = Revisao('Revisão do Óleo',100,45,1)
#Aplicando o desconto
revisao_oleo.aplicar_desconto()

pintura_fosca = Pintura('Pintura do porta-malas',1200,'Metálica')
pintura_fosca.aplicar_desconto()


#Interligando com o objeto serviço e o objeto carro
carro_civic.adicionar_no_servico(reparo_pintura)
carro_civic.adicionar_no_servico(revisao_oleo)
carro_civic.adicionar_no_servico(pintura_fosca)


def main():
    carro_civic.exibir_servico

if __name__ == '__main__':
    main()