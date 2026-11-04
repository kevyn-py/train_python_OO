#Criação da classe
class Carro:
    #Metodo contrutor - Sempre que criar uma instância(objeto) de uma classe ele será chamado automaticamente. __init__ e self(instancia do objeto).
    #Esse metodo serve para garantir que todo objeto seja criado com todas as informações necessárias para funcionar corretamente.
    carros = []

    def __init__(self, nome, marca, ano):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.ativo = False
        Carro.carros.append(self) # Adicionando todos os carros numa lista

    #Metodo especial __str__ - Serve para exibir os valores atribuidos de um objeto em formato de string.
    def __str__(self):
        return f'{self.nome} | {self.marca} | {self.ano} | {self.ativo}'
    
    # Metodo listar_carros - serve para exibir todos objetos que estão na lista
    def lista_carros():
        for carro in Carro.carros:
            print(f'{carro.nome} | {carro.marca} | {carro.ano} | {carro.ativo}')


#Instanciando um objeto nesta classe Carro com metodo contrutor
carro_mustang = Carro('Mustang','Ford',1984)
carro_celta = Carro('Celta','Chevrolet',1943)


#Exibindo todos os carros de uma vez só.
Carro.lista_carros()

