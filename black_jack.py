#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:30:42 2019
@author: tiago

Objetos:

# BLACKJACK: ÀS E OUTRA CARTA QUE VALE 10 PONTOS    

Funções:
    
hit()
stop()
double()
split()

primeira_rodada() #primeira rodada se diferencia por permitir split e double e por ser a única que distribui duas cartas. É na primeira rodada que os jogadores apostam.
rodada() #a cada rodada, podemos chamar as funcoes: hit, stop, double. E checar se tem condicoes da funcao split e 21.
checa_as() # sempre checar se existe uma carta 'Às' na mao dos jogadores. 'Às' pode ser 1 ou 11, se o 'Às' + outras cardas <= 21
checa_estouro() #a cada rodada, eu checo se jogador ou dealer estourou
checa_split() #a cada rodada eu checo se tenho opção split (duas cartas com o mesmo valor pode splitar)
maior_mao() #antes da rodada do dealer, verifica quais as maiores mãos que irão jogar contra dealer. Pode ser uma ou mais, apenas se empatarem no maior valor.
dealer_vencendo() #dealer checa se está vencendo, para decidir se continua apostando ou não. Se dealer está perdendo, tenta ganhar ou empatar sempre.
dealer_acao()
vencedor() #Checa se todos os jogadores + dealer já deram stop ou estouro e calcula o vencedor
ver_fimdejogo() # Ao final de cada turno, verificar se atingiu as condições de final de jogo
fim_jogo()
# Mostra campeão: Jogador com maior valor de dinheiro, se dealer igual a zero, ou Game Over.
# Game over: Se dealer tem dinheiro e os demais não. Se todos os jogadores saíram do jogo em algum começo de turno.


Observações:
Considerar ativo na partida todo jogador cujo status = True. Se jogador sair ou zerar, status == False. 

"""
from random import choice

jogadores = []

#Cria a classe dos jogadores. Por padrão, todo jogador começa uma partida com 1000 dinheiros e ativo no jogo
class Jogador(object):
    def __init__(self, nome, carteira=1000, status=True):
        self.nome = nome
        self.carteira = carteira
        self.status = status
    
    def aposta(self):
        while True:
            try:
                valor = int(input('Digite o valor da aposta: '))
            except:
                print('Digitar apenas valores inteiros.')
                continue
            if valor > self.carteira:
                print('Não há saldo suficiente. Disponível em carteira: ', self.carteira)
                continue
            else:
                self.carteira -= valor
                print('Saldo restante: ', self.carteira)
                break
        return valor
    
    def add_dindin(self, valor):
        self.carteira += valor
        return self.carteira
    
    def tira_dindin(self, valor):
        if valor >= self.carteira:
            self.status = False
            self.carteira = 0
        return print('Você perdeu tudo. Se lascou.')

#Cria a classe do dealer, com devido level. O level configura o valor da banca, total de dinheiro do dealer.    
class Dealer(object):
    def __init__(self, banca=0, level=0, mao_dealer=[]):
        self.banca = banca
        self.level = level
        self.mao_dealer = mao_dealer
        
    def add_dindin(self,valor):
        self.banca += valor
        return self.banca
    
    def tira_dindin(self,valor):
        self.banca -= valor
        return self.banca
    
    def add_carta(self,carta):
        self.mao_dealer.append(carta)
        return self.mao_dealer
    
    def reset_mao(self):
        self.mao_dealer = []
        return self.mao_dealer
    
    def set_level(self):
        while True:
            try:
                self.level = int(input('Insira o level que deseja jogar (1 - fácil, 2 - normal, 3 - hard): '))
            except:
                print('Digite um número entre 1 e 3')
                continue
            if self.level == 1:
                self.banca = 5000
                break
            elif self.level == 2:
                self.banca = 10000
                break
            elif self.level == 3:
                self.banca = 50000
                break
            else:
                print('Digite um nível válido: ')
                continue
        return self.level, self.banca

# Cria o baralho, com todas as cartas e ações dentro do baralho, para tirar cartas aleatoriamente e resetar o baralho para novo turno.
class Baralho(object):
    cartas = ['JOuros', '9Ouros', '9Copas', 'KCopas', '5Paus', '6Ouros', '2Ouros', '3Copas', 'QPaus', 'JCopas', '2Espadas', '4Ouros', '9Espadas', '8Paus', '10Copas', '10Paus', '2Paus', '7Espadas', 'KEspadas', '6Paus', '5Espadas', 'AOuros', 'KOuros', '5Copas', '10Ouros', '4Espadas', '10Espadas', '7Ouros', 'QCopas', '2Copas', '8Copas', '7Paus', '9Paus', 'ACopas', '3Espadas', '8Ouros', '5Ouros', 'KPaus', '3Paus', '4Paus', '3Ouros', '4Copas', '7Copas', '6Espadas', 'JEspadas', '6Copas', 'AEspadas', 'QEspadas', '8Espadas', 'QOuros', 'APaus', 'JPaus']
    def __init__(self):
        pass
        
    def tira_carta(self):
        carta_vez = choice(self.cartas)
        self.cartas.remove(carta_vez)
        return carta_vez
        
    def reset(self):
        self.cartas = ['JOuros', '9Ouros', '9Copas', 'KCopas', '5Paus', '6Ouros', '2Ouros', '3Copas', 'QPaus', 'JCopas', '2Espadas', '4Ouros', '9Espadas', '8Paus', '10Copas', '10Paus', '2Paus', '7Espadas', 'KEspadas', '6Paus', '5Espadas', 'AOuros', 'KOuros', '5Copas', '10Ouros', '4Espadas', '10Espadas', '7Ouros', 'QCopas', '2Copas', '8Copas', '7Paus', '9Paus', 'ACopas', '3Espadas', '8Ouros', '5Ouros', 'KPaus', '3Paus', '4Paus', '3Ouros', '4Copas', '7Copas', '6Espadas', 'JEspadas', '6Copas', 'AEspadas', 'QEspadas', '8Espadas', 'QOuros', 'APaus', 'JPaus']
        return self.cartas
    
# Cria as regras das mãos que serão jogadas por todos os jogadores a cada turno.
class Mao(object):
    cartas_valores = {'A':1,'J':10,'Q':10,'K':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    mao_cartas_jogador = []
    soma = 0
    def __init__(self,jogador):
        self.jogador = jogador
        
    def add_jogador(self,jogador):
        mao_jogador = self.jogador
        return mao_jogador
    
    def mao_cartas(self, carta):
        if carta[0].isalpha() or carta[0] != '1':
            self.mao_valor = self.cartas_valores[carta[0]]
            self.soma += self.mao_valor
            self.mao_cartas_jogador.append(carta)
        else:
            self.mao_valor = 10
            self.soma += self.mao_valor
            self.mao_cartas_jogador.append(carta)
        return self.mao_cartas_jogador, self.soma

def registra_jogador():
    global jogadores
    jogadores = [input('Digite nome do jogador: ')]
    novo = input('deseja registrar novo jogador? Sim, Não: ').lower()
    if novo[0] == 's':
        jogadores.append(input('Digite nome do jogador: '))
    return jogadores






# Continuar daqui
def criar_jogadores():
    global jogadores
    for x in jogadores:
        jogadores[0] = Jogador(x)
    return


registra_jogador()
criar_jogadores()
print(jogadores[0].nome)
print(jogadores[0].carteira)
print(jogadores[0].status)


    
    
    
    
    
    
    
    

