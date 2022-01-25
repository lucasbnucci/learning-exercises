class Banco:
    def __init__(self, name, saldo = 0):
        self.nomebanco = name
        self.saldoconta = saldo
    def nome(self):
        print(self.nomebanco)
    def saldo(self):
        print(self.saldoconta)
    def saldobonito(self):
        print(self.nomebanco," você tem ",self.saldoconta)
    def deposito(self, n):
        self.saldoconta += n   

duts = Banco('duts', 90)

duts.nome()
duts.saldo()
duts.deposito(90)
duts.saldobonito()

lucas = Banco('Lucas')

lucas.nome()
lucas.saldo()
lucas.saldobonito()