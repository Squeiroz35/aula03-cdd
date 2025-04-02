E=4.90
G=5.80
valor=0
tipodecombustivel=input("qual é o tipo de combustivel desejado?")
qantcombustivel= float(input("quantos Litros deseja colocar?"))
if tipodecombustivel == "g" or tipodecombustivel == "G":
    valor=qantcombustivel*G
    print (f"voce abasteceu {qantcombustivel}L\n"
           f"e voce gastou {valor} ")
elif tipodecombustivel == "e" or qantcombustivel == "E":
    valor=qantcombustivel*E
    print (f"voce abasteceu {qantcombustivel}L\n"
           f"e vc gastou {valor}")
else:
    print ("digite um combustivel valido")
