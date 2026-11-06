#Criação da classe
class Carro:
    #Metodo contrutor - Sempre que criar uma instância(objeto) de uma classe ele será chamado automaticamente. __init__ e self(instancia do objeto).
    #Esse metodo serve para garantir que todo objeto seja criado com todas as informações necessárias para funcionar corretamente.
    carros = []

    def __init__(self, nome, marca, ano):
        self._nome = nome.title() #Faz a primeira letra ser Maiuscula
        self._marca = marca.upper() #Faz todas as letras serem Maisculas
        self._ano = ano
        self._ativo = False  #._ é um atributo protegido, que nao deve ser mexido
        Carro.carros.append(self) # Adicionando todos os carros numa lista

    #Metodo especial __str__ - Serve para exibir os valores atribuidos de um objeto em formato de string.
    def __str__(self):
        return f'{self.nome} | {self.marca} | {self.ano} | {self.ativo}'
    
    # Metodo listar_carros - serve para exibir todos objetos que estão na lista
    @classmethod #Um metodo que está referenciando com a class
    def lista_carros(cls):
        print(f'{'Nome do carro'.ljust(25)} | {'Marca'.ljust(25)} | {'Ano'.ljust(25)} | {'Status'.ljust(25)}')
        for carro in cls.carros:
            print(f'{carro._nome.ljust(25)} | {carro._marca.ljust(25)} | {carro._ano.ljust(25)} | {carro.ativo.ljust(25)}')

    @property #Serve para mudar o modo de como o atributo vai ser lido
    def ativo(self):
        return '✔' if self._ativo else '✗'

    def alternar_estado(self):
        self._ativo = not self._ativo

#Instanciando um objeto nesta classe Carro com metodo contrutor
carro_mustang = Carro('Mustang','Ford','1991')
carro_mustang.alternar_estado() #Alternando o status do objeto
carro_celta = Carro('Celta','Chevrolet','1998')


#Exibindo todos os carros de uma vez só.
Carro.lista_carros()

