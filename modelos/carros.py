from modelos.avaliacao import Avaliacao

#Criação da classe
class Carro:
    '''Representa um carro e suas características'''

    #Metodo contrutor - Sempre que criar uma instância(objeto) de uma classe ele será chamado automaticamente. __init__ e self(instancia do objeto).
    #Esse metodo serve para garantir que todo objeto seja criado com todas as informações necessárias para funcionar corretamente.
    carros = []

    def __init__(self, nome, marca, ano):
        '''
        Inicializa uma instância de Carro.

        Parâmetros:
        - nome (str): o nome do carro
        - marca (str): A marca do carro
        - ano (int) : O ano do carro

        '''
        self._nome = nome.title() #Faz a primeira letra ser Maiuscula
        self._marca = marca.upper() #Faz todas as letras serem Maisculas
        self._ano = ano
        self._ativo = False  #._ é um atributo protegido, que nao deve ser mexido

        self._avaliacao = []

        Carro.carros.append(self) # Adicionando todos os carros numa lista

    #Metodo especial __str__ - Serve para exibir os valores atribuidos de um objeto em formato de string.
    def __str__(self):
        ''' Retorna uma representação em string de um carro '''

        return f'{self.nome} | {self.marca} | {self.ano} | {self.ativo}'
    
    # Metodo listar_carros - serve para exibir todos objetos que estão na lista
    @classmethod #Um metodo que está referenciando com a class
    def lista_carros(cls):
        ''' Exibe uma lista formatada de todos os carros '''

        print(f'{'Nome do carro'.ljust(25)} | {'Marca'.ljust(25)} | {'Ano'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'.ljust(25)}')
        for carro in cls.carros:
            print(f'{carro._nome.ljust(25)} | {carro._marca.ljust(25)} | {str(carro._ano).ljust(25)} | {str(carro.media_avaliacao).ljust(25)} | {carro.ativo.ljust(25)}')

    @property #Serve para mudar o modo de como o atributo vai ser lido
    def ativo(self):
        ''' Retornar um símbolo indicando o estado de atividade do carr o'''

        return '✔' if self._ativo else '✗'

    def alternar_estado(self):
        ''' Alterna o estado de atividade do restaurante '''

        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota): 
        '''
        Registra uma avaliação para o carro

        Parâmetro:
        - cliente (str): O nome do cliente que fez a avaliação
        - nota (float): A nota atribuída ao carro (entre 1 e 5)
        '''

        #Validação para criar um padrão de nota de 1 a 5
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente,nota) #intanciando avalicao
            self._avaliacao.append(avaliacao) # Adicionando na lista
        
    @property
    #Método media_avaliacao para fazer uma media da lista de avaliações do objeto instanciado
    def media_avaliacao(self):
        ''' Calcula e retorna a média das avaliações do carro '''
        #Tratativa para carro não tiver nenhuma avaliação
        if not self._avaliacao:
            return '-' 

        soma = sum(avaliacao._nota for avaliacao in self._avaliacao) # Somando todas as notas sendo que cada avaliação pegue somente o valor da nota 
        quantidade = len(self._avaliacao) #fazendo a contagem da quantidade de notas utilizando o len()
        media = round(soma/quantidade,1)# utiliando o round() para exibir apenas uma casa de decimal
        return media



    

