#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:30:42 2019
@author: tiago
"""
from random import choice

#Cria a classe dos jogadores. Por padrão, todo jogador começa uma partida com 1000 dinheiros e ativo no jogo
class Jogador(object):
    cartas_valores = {'A':11,'J':10,'Q':10,'K':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    mao_cartas_jogador = []
    soma = 0
    def __init__(self, nome, carteira=1000, status=True, status_rodada=True, apostas=0):
        self.nome = nome
        self.carteira = carteira
        self.status = status
        self.status_rodada = status_rodada
        self.apostas = apostas
    
    def aposta(self):
        while True:
            try:
                valor = int(input(f'{self.nome}, digite o valor da aposta: '))
            except:
                print('Digitar apenas valores inteiros.')
                continue
            if valor > self.carteira:
                print('Não há saldo suficiente. Disponível em carteira: ', self.carteira)
                continue
            else:
                self.carteira -= valor
                self.apostas = valor
                print('Saldo restante: ', self.carteira)
                break
        return valor

    def mao_cartas(self, carta, nome):
        c = 0
        if carta[0].isalpha() or carta[0] != '1':
            self.mao_valor = self.cartas_valores[carta[0]]
            self.soma += self.mao_valor
            self.mao_cartas_jogador.append(carta)
        else:
            self.mao_valor = 10
            self.soma += self.mao_valor
            self.mao_cartas_jogador.append(carta)
        for checa_as in self.mao_cartas_jogador:
            if self.mao_cartas_jogador[c][0] == 'A' and self.soma > 21:
                self.soma -= 10
            c += 1
        return print(self.nome, self.mao_cartas_jogador, self.soma)
    
    def reset_mao(self):
        self.mao_cartas_jogador = []
        self.soma = 0
        self.status_rodada=True
        return self.mao_cartas_jogador
    
    def add_dindin(self, valor):
        self.carteira += valor
        return self.carteira
    
    def tira_dindin(self, valor):
        if valor >= self.carteira:
            self.status = False
            self.carteira = 0
            print('Você perdeu tudo. Se lascou.')
        else:
            self.carteira -= valor
            self.apostas += valor
        return self.carteira

#Cria a classe do dealer, com devido level. O level configura o valor da banca, total de dinheiro do dealer.    
class Dealer(object):
    cartas_valores = {'A':11,'J':10,'Q':10,'K':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    mao_cartas_dealer = []
    soma = 0
    def __init__(self, banca=0, level=0):
        self.banca = banca
        self.level = level
                
    def add_dindin(self,valor):
        self.banca += valor
        return self.banca
    
    def tira_dindin(self,valor):
        if valor >= self.banca:
            self.banca = 0
            print('Dealer perdeu tudo. Se lascou.')
        else:
            self.banca -= valor
        return self.banca
    
    def mao_dealer(self, carta):
        c = 0
        if carta[0].isalpha() or carta[0] != '1':
            self.mao_valor = self.cartas_valores[carta[0]]
            self.soma += self.mao_valor
            self.mao_cartas_dealer.append(carta)
        else:
            self.mao_valor = 10
            self.soma += self.mao_valor
            self.mao_cartas_dealer.append(carta)
        for checa_as in self.mao_cartas_dealer:
            if self.mao_cartas_dealer[c][0] == 'A' and self.soma > 21:
                self.soma -= 10
            c += 1
        return print('Dealer', self.mao_cartas_dealer, self.soma)
    
    def reset_mao(self):
        self.mao_cartas_dealer = []
        self.soma = 0
        return self.mao_cartas_dealer
    
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

def registra_jogador():
    global jogadores
    jogadores = [input('Digite nome do jogador: ')]
    novo = input('deseja registrar novo jogador? Sim, Não: ').lower()
    if novo[0] == 's':
        jogadores.append(input('Digite nome do jogador: '))
    return jogadores

def criar_jogadores():
    global jogadores
    n = 0
    for x in jogadores:
        jogadores[n] = Jogador(x)
        n += 1
    return

def nova_partida():
    registra_jogador()
    criar_jogadores()
    dealer.set_level()
    rodada1()
    return
    
def rodada1():
    global jogadores
    n = 0
    for x in jogadores:
        if jogadores[n].status == True:
            jogadores[n].aposta()
            jogadores[n].reset_mao()
            jogadores[n].mao_cartas(baralho.tira_carta(), jogadores[n].nome)
            jogadores[n].mao_cartas(baralho.tira_carta(), jogadores[n].nome)
        n += 1
    dealer.mao_dealer(baralho.tira_carta())
    dealer.mao_dealer(baralho.tira_carta())
    rodada2()
    return

def reset_rodada():
    print('terminar de configurar a função reset_rodada')
    baralho.reset()
    dealer.reset_mao()
    j = 0
    for reset in jogadores:
        jogadores[j].reset_mao()
        jogadores[j].apostas = 0
        j += 1
    return

def checa_fim():
    f = 0
    for fim in jogadores:
        if jogadores[f].carteira == 0:
            jogadores[f].status = False
        f += 1
    if jogadores[0].status == False and jogadores[1].status == False:
        print('Game Over! Configurar input de fim de jogo')
    elif dealer.banca == 0:
        print('Parabéns! Vocês venceram! Bateram a banca!')
    else:
        print('Ninguém ganhou ainda, nem perdeu. Todo mundo perdeu.')
    return 'Dealer', dealer.banca, jogadores[0].nome, jogadores[0].carteira, jogadores[1].nome, jogadores[1].carteira

def dealer_rodada():
    y = 0
    for deal in jogadores:
        if jogadores[y].status_rodada == True:
            while dealer.soma < 17 or dealer.soma <= jogadores[y].soma:
                dealer.mao_dealer(baralho.tira_carta())
            if dealer.soma <=21:
                if dealer.soma > jogadores[y].soma and jogadores[y].status_rodada == True:
                    dealer.add_dindin(jogadores[y].apostas)
                    print(dealer.banca)
                    y += 1
                elif dealer.soma < jogadores[y].soma and jogadores[y].status_rodada == True:
                    dealer.tira_dindin(jogadores[y].apostas)
                    jogadores[y].add_dindin(jogadores[y].apostas*2)
                    print(jogadores[y].carteira)
                    print(dealer.banca)
                    y += 1
                elif dealer.soma == jogadores[y].soma and jogadores[y].status_rodada == True:
                    jogadores[y].add_dindin(jogadores[y].apostas)
                    print(jogadores[y].carteira)
                    print(dealer.banca)
                    y += 1
                else:
                    print('alguma merda deu errado, pq não tem else aqui. Logica dealer')
            elif dealer.soma > 21 and jogadores[y].status_rodada == True:
                jogadores[y].add_dindin(jogadores[y].apostas*2)
                dealer.tira_dindin(jogadores[y].apostas)                     
                print('dealer estourou')
                print(jogadores[y].nome,jogadores[y].carteira)
                print(dealer.soma, dealer.banca)
                y += 1
        else:    
            y += 1
            print('Essa porra imprimiu certo?', dealer.soma)
    return

def rodada2():
    global jogadores
    z = 0
    for y in jogadores:
        if jogadores[z].soma < 21 and jogadores[z].status == True:
            decisao = input(f'O que você deseja fazer, {jogadores[z].nome}?\nHit (H), Double (D), Parar (P): ').upper()
            if decisao[0] == 'H':
                jogadores[z].mao_cartas(baralho.tira_carta(), jogadores[z].nome)
                if jogadores[z].soma < 21:
                    decisao2 = input(f'O que você deseja fazer, {jogadores[z].nome}?\nHit (H), Parar (P): ').upper()
                    while decisao2[0] == 'H' and jogadores[z].soma < 21:
                        jogadores[z].mao_cartas(baralho.tira_carta(), jogadores[z].nome)
                        if jogadores[z].soma < 21:
                            decisao2 = input(f'O que você deseja fazer, {jogadores[z].nome}?\nHit (H), Parar (P): ').upper()
                    if decisao2[0] == 'H' and jogadores[z].soma == 21:
                        print('21! no looping do decisao2')
                        z += 1
                    elif decisao2[0] == 'H' and jogadores[z].soma > 21:
                        jogadores[z].status_rodada = False
                        dealer.add_dindin(jogadores[z].apostas)
                        print(dealer.banca)
                        print('estourou no looping do decisao2')
                        z += 1
                    elif decisao2[0] == 'P':
                        print('Parou, caraio no looping da decisao2')
                        z += 1
                elif jogadores[z].soma == 21:
                    print('21!')
                    z += 1
                else:
                    jogadores[z].status_rodada = False
                    dealer.add_dindin(jogadores[z].apostas)
                    print(dealer.banca)
                    print('estourou no primeiro hit antes do looping do decisao2')
                    z += 1
            elif decisao[0] == 'D':
                apostas_ = jogadores[z].apostas
                jogadores[z].tira_dindin(apostas_)
                print('Saldo restante: ', jogadores[z].carteira)
                jogadores[z].mao_cartas(baralho.tira_carta(), jogadores[z].nome)
                if jogadores[z].soma > 21:
                    jogadores[z].status_rodada = False
                    dealer.add_dindin(jogadores[z].apostas)
                    print(dealer.banca)
                    print('Se lascou no Double, estourou')
                    z += 1
                elif jogadores[z].soma == 21:
                    print('21 no double, caceeete!')
                    z += 1
                else:
                    z += 1
            elif decisao[0] == 'P':
                print('Parou de apostar')
                z += 1         
        elif jogadores[z].soma == 21 and jogadores[z].status == True:
            ('BlackJack, porra!')
            z += 1
        else:
            z += 1
    dealer_rodada()
    checa_fim()
    reset_rodada()
    rodada1()
    return

jogadores = []
baralho = Baralho()
dealer = Dealer()

print('Bem-vindo ao jogo de BlackJack em texto para iniciantes do python ^^')
nova_partida()






