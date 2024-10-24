from datetime import datetime
from random import randint
import pytz

class ContaCorrente():
    
   
    def __init__(self, nome, cpf, agencia, numconta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 100
        self.limite = None
        self.agencia = agencia
        self.numconta = numconta
        self.transacoes = []
        self.cartoes = []
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_br  =datetime.now(fuso_BR)
        return horario_br.strftime('%y-%m-%d %H:%M:%S')
    
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass
    
    def deposita_dinheiro(self, valor):
        self.saldo += valor           
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
    
    def sacar_dinheiro(self, valor):
        if self.saldo -valor < self.limit_conta():
            print("Saldo insuficiente!")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass
    
    def limit_conta(self):
        self.limite = -1000
        return self.limite
    
    def historico(self):
        for transacao in self.transacoes:
            if len(transacao) == 4: #se forem 4 elementos, nesse caso a conta_destino
                valor, saldo, data_hora, tipo = transacao
            else:
                valor, saldo, data_hora = transacao 
                tipo = "Saque" if valor < 0 else "Depósito"

            print(f"{tipo}: R${abs(valor):,.2f}, Saldo: R${saldo:,.2f}, Data/Hora: {data_hora}")

    
    def transfere(self, valor, conta_destino):
        if self.saldo - valor < self.limit_conta():
            print("Saldo insuficiente para transferir!")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora(), "Transferência"))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora(), "Transferência"))


class CartaoCredito:
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(10**15, 10**16 - 1)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self )
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR  =datetime.now(fuso_BR)
        return horario_BR
    
    