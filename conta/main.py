from monopoly import ContaCorrente, CartaoCredito

conta_mark = ContaCorrente("Mark", "111.111.111.11", "1234", "34062")
cartao_mark = CartaoCredito("Mark", conta_mark)
conta_igor = ContaCorrente("Igor", "999.999.999.99", "0001", "123456")

print(cartao_mark.__dict__)