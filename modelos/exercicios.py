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

#Intanciando objeto
cliente_roberto = Cliente('Roberto',51,'roberto@sememail.com.br','11 99999-9999')

print(cliente_roberto)