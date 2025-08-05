# coleta de dados do jogador
name = input('Digite seu nome: ')
print(f'Bora conferir sua posição no ranque {name}!\n')

vitorias = int(input('Digite o seu número de vitorias: '))
print(f'Perfeito, você tem {vitorias} vitórias!\n')

derrotas = int(input('Digite o seu número de derrotas: '))
print(f'Você perdeu {derrotas} vezes :(\n')

# a função deve ser uma ação para calcular o rank do jogador


def calcular_rank(vitorias, derrotas):
    saldo = vitorias - derrotas
    return f'{name}, você tem um saldo de {saldo} vitórias e está no nível {nivel}.\n'


# condições para saber o nível do jogador
if vitorias < 10:
    nivel = 'Ferro'
elif 11 <= vitorias <= 20:
    nivel = 'Bronze'
elif 21 <= vitorias <= 50:
    nivel = 'Prata'
elif 51 <= vitorias <= 80:
    nivel = 'Ouro'
elif 81 <= vitorias <= 90:
    nivel = 'Diamante'
elif 91 <= vitorias <= 100:
    nivel = 'Lendário'
elif vitorias >= 101:
    nivel = 'Imortal'

# Exibir resultado da função através de uma variável
resultado = calcular_rank(vitorias, derrotas)
print(resultado)

# se vitórias for menor do que 10 = Ferro
# se vitórias for entre 11 e 20 = Bronze
# se vitórias entre 21 e 50 = Prata
# se vitórias for entre 51 e 80 = Ouro
# se vitórias for entre 81 e 90 = Diamante
# se vitórias for entre 91 e 100 = Lendário
# se vitórias for maior ou igual a 101 = Imortal
