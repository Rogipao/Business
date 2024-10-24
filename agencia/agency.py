from random import randint
from unicodedata import numeric


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def catbox(self):
        if self.caixa < 1000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor de Caixa está normal. Caixa Atual: {}'.format(self.caixa))
            
            
    def emprestimo(self, valor, cpf, juros):
        if valor < self.caixa:
            self.emprestimos.append((valor, cpf, juros))
            print("Empréstimo concedido com sucesso!")
        else:
            print('Empréstimo Bloqueado. O valor passa a quantidade do caixa')
            
            
            
    def add_client(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
            
class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)
        self.caixa = 10000
        self.caixa_paypal = 0
     
       
    def depositopp(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        
    def saquepp(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
    pass
class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj,randint(1001, 9999))
        self.caixa = 10000
    pass
class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj,randint(1001, 9999))
        self.caixa = 10000000
    
    def add_clientpm(self, nome, cpf, patrimonio):
        if patrimonio >10000000:
            self.clientes.append((nome, cpf, patrimonio))
        else:
            print("Cliente não possui o patrimonio minimo")
    pass
            
agencia1 = Agencia(22223333, 2000000, 4568)
agencia1.caixa = 1000
agencia1.add_client('Igor', 11122233344, 10000)



agenciavr = AgenciaVirtual('www.paypal.com',22224444, 1520000000, 100)
agenciavr.catbox()
print(agenciavr.__dict__)
print("\n")
agenciacm = AgenciaComum(22224444, 1520000000)
agenciavr.catbox()
print(agenciacm.__dict__)
print("\n")
agenciapm = AgenciaPremium(22224444, 1520000000)
agenciapm.catbox()
print(agenciapm.__dict__)
print("\n")
print("\n")
agenciavr.depositopp(200000)
print(agenciavr.caixa)
print(agenciavr.caixa_paypal)
print("\n")
#agenciacm.depositopp(1000)
#print(agenciacm.caixa)
#print(agenciavr.caixa_paypal)

agencia1.add_client('Igor', 11122233344, 10000)
print('Cliente agencia1:',agencia1.clientes) 
print("\n")

agenciavr.add_client('Igor', 11122233344, 10000)
print('Cliente agencia1:',agenciavr.clientes) 
print("\n")

agenciacm.add_client('Igor', 11122233344, 10000)
print('Cliente agencia1:',agenciacm.clientes) 
print("\n")

agenciapm.add_client('Igor', 11122233344, 10000)
print('Cliente agencia1:',agencia1.clientes) 