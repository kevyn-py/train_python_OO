from modelos.carros import Carro
from modelos.servicos.reparo import Reparo
from modelos.servicos.revisao import Revisao

#intanciando com metodo contrutor
carro_civic = Carro('Civic','Honda',2004)
reparo_pintura = Reparo('Pintura no para-choque frontal',250,2)
revisao_oleo = Revisao('Revisão do Óleo',100,45,1)


def main():
    print(reparo_pintura)
    print(revisao_oleo)

if __name__ == '__main__':
    main()