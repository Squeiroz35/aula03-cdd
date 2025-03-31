name= input("digite seu nome: ")
age= int(input("dgite sua idade: "))
wage= float(input("digite seu salario: "))
print (f"welcome {name}, your age is: {age}, and your wage is {wage}:")
aumento= float(input("digite em quantos porcentos foi o aumento do seu salario:"))
valoraumento = wage*(aumento/100)
print(f"seu aumento foi de: {valoraumento}")
salarionovo= wage+valoraumento
print(f"seu salario depois do aumento é: {salarionovo}")
