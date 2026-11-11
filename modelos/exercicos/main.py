from veiculo import Carro

#Intanciando objeto carro
carro1 = Carro('honda','civic',2004)
carro2 = Carro('Chevrolet','prisma',2016)
carro3 = Carro('Volkswagen','Up',2019)

print(f'{'Marca'.ljust(25)} | {'MODELO'.ljust(25)} | {'ANO'.ljust(25)}')
print(f'{carro1._marca.ljust(25)} | {carro1._modelo.ljust(25)} | {carro1._ano}')
print(f'{carro2._marca.ljust(25)} | {carro2._modelo.ljust(25)} | {carro2._ano}')
print(f'{carro3._marca.ljust(25)} | {carro3._modelo.ljust(25)} | {carro3._ano}')



