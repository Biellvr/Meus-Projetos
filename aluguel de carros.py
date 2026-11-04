dias = int(input("quantos dias o carro foi alugado?"))
km = float (input("qual a quantidade de kms rodados?"))
pago = (dias * 60) + (km * 0.15)
print ('o total a pagar é de R$ {:.2F}' .format(pago))