'''
#Crie uma classe Musica com os atributos nome,artista e duração. E depois, instancia 3 objetos desta classe
class Musica:
    musicas = []

    #Metodo Contrutor
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self) # Cada objeto será inserido numa lista

    #Metodo especial __str__ (para exibir os valores atribuidos no objeto)
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    #Criando um novo modelo para listar todas musicas que tem na lista Musicas
    def listar_todos():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

        
#Instanciado o objeto
musica_sertaneja = Musica('Caso indefinido','Cristiano Araújo',100)
musica_trap = Musica('Isso é sério', 'Matuê', 120)
musica_mpb = Musica('Amiga da minha mulher', 'São Jorge', 145)

#Chamando a função listar todos da class Musica, para exibir todos os objetos que estão na lista
Musica.listar_todos()


#Criação da classe Carro
class Carro:
    #Criando o metodo contrustor
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    #Criando o metodo __str__
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

#Instanciando objeto
carro_uno = Carro('Uno','Verde',1999)
print(carro_uno)


#Criação da classe Restaurante
class Restaurante:
    # Metodo contrutor com o atributo 'ativo' ativado
    def __init__(self,nome,categoria,endereco,avaliacao, ativo = True ):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.avaliacao = avaliacao
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.endereco} | {self.avaliacao}'

#Instanciando objeto
restaurante_lepore = Restaurante('Lepore','Hamburgueria','Rua Sem nome',7.6)

print(restaurante_lepore)


#Criando a classe Cliente
class Cliente:
    def __init__(self,nome,idade,email,telefone):
        self.nome = nome 
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.email} | {self.telefone}'

#Intanciando objeto.
cliente_roberto = Cliente('Roberto',51,'roberto@sememail.com.br','11 99999-9999')

print(cliente_roberto)
'''

'''
class Pessoa:
    def __init__(self,nome,idade,profissao = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    #Metódo instancia
    def aniversario(self):
        self.idade += 1
    #
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá, sou {self.nome}'


pessoa_cleber = Pessoa('Cleber',21,'Mecânico')
pessoa_carlos = Pessoa('Carlos',45)
print(pessoa_cleber)
pessoa_cleber.aniversario()
print(pessoa_cleber)
print(pessoa_cleber.saudacao)
print(pessoa_carlos)
'''

'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular.ljust(15)} | Saldo da Conta: {self._saldo}'

    def ativar_conta(self):
        self._ativo =  not self._ativo

conta1 = ContaBancaria('Cleber',1111)
conta2 = ContaBancaria('Joao', 2222)

print(conta1)
print(conta2)
conta1.ativar_conta()
print(conta1._ativo)
'''

'''
#Refatorando a classe ContaBancaria utilizando uma abordagem pythonica
class ContaBancariaPythonica:
    def __init__(self,titular,saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    def ativar_conta(self):
        self._ativo = not self._ativo

    def __str__(self):
        return f'Titular da Conta: {self._titular} | Saldo da conta: {self._saldo} | Status: {self._ativo}'

conta = ContaBancariaPythonica('Roberto', 500)
print(conta)
conta.ativar_conta()
print(conta)

class ClienteBanco:
    def __init__(self,nome,idade,endereco,profissao,cpf):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._profissao = profissao
        self._cpf = cpf

    #Criando um metodo de classe
    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta = ContaBancariaPythonica(titular,saldo_inicial)
        return conta
#Neste caso eu so instancio apenas uma vez, pois o metodo criar_conta está instanciando na classe ContaBancariaPythonica
conta_cliente1 = ClienteBanco.criar_conta('Ana',200)
print(f'Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}')
'''

class Livro:
    def __init__(self,titulo,autor,ano_publicacao):
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Título do livro: {self._titulo.ljust(25)} | Autor: {self._autor.ljust(25)} | Ano de Publicação: {self._ano_publicacao}'

    #Metodo instância
    def emprestar(self):
        self._disponivel = not self._disponivel

    #Método estático
    @staticmethod # Uma função que pertence à classe em si
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

    

livro1 = Livro('Harry Potter','Cristina Alves',2005)
livro2 = Livro('Verity','Colllen Hoover',2018)

print(livro1)
print(livro2)

livro3 = Livro('Diário de um Banana','Jorge Cruz', 2010)
print(f'Antende de emprestar o livro: {livro3._disponivel}')
livro3.emprestar()
print(f'Depois de emprestar o livro {livro3._disponivel}')

Livro.livros = [livro1,livro2,livro3]