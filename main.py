from modelos.carros import Carro
#intanciando com metodo contrutor
carro_civic = Carro('Civic','Honda',2004)
carro_kicks = Carro('Kicks','Nissan',2018)
carro_corsa  = Carro('Celta','Chevrolet',2000)

#instanciando receber_avalicao
carro_civic.receber_avaliacao('Guilherme',10)
carro_civic.receber_avaliacao('livia',9)
carro_civic.receber_avaliacao('manuela',1)

def main():
    Carro.lista_carros()

if __name__ == '__main__':
    main()