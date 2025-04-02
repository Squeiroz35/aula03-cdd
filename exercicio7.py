E=4.90
G=5.80
valor=0
tipo= input("qual o tipo de combustivel voce deseja?")
qntdecombustivel= float(input("digite quantos litros voce desejar colocar:"))
if tipo== "e" or tipo== "E":
    valor= E * qntdecombustivel
    print (f"Litros {qntdecombustivel}L\n")
    f"Valor: {valor}"
elif tipo== "g" or tipo== "G":
    valor= G * qntdecombustivel
    print (f"Litros {qntdecombustivel}L\n ")
    f"Valor: {valor}"
else:
    print ("digite um tipo de combustivel valido")

