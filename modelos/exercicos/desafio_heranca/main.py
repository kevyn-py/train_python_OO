from carro import Carro
from moto import Moto

#Intanciando para Carro
carro1 = Carro('Honda','i30',4)
carro2 = Carro('Chevrolet','Celta',2)
carro3 = Carro('Renault','Spin',6)

#Instanciando para moto
moto1 = Moto('Honda','Hornet','Esportiva')
moto2 = Moto('Honda','Bisnaguinha','Casual')
moto3 = Moto('Honda','Ninja','Esportiva')

#Criando o def main
def main():
    print(carro1)
    print(carro2)
    print(carro3)
    print()
    print(moto1)
    print(moto2)
    print(moto3)

#padronização do arquivo  
if  __name__ == '__main__':
    main()