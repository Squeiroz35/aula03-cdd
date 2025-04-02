E=4.90
G=5.80
tipo= input("qual o tipo de combustivel voce deseja?")
qntdecombustivel= float(input("digite quantos litros voce desejar colocar:"))
if tipo== "e":
    valor= E * qntdecombustivel
    print (f"total de litros: {valor}")
elif tipo== "g":
    valor= G * qntdecombustivel
    print (f"total de litros:{valor} ")
else:
    print ("digite um tipo de combustivel valido")

