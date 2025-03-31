nome= input("digite seu nome: ")
idade= int(input("dgite sua idade: "))
salario= float(input("digite seu salario: "))
print (f"bem vindo {nome}, sua idade é: {idade}, e seu salario é: {salario}")
aumento= float(input("digite em quantos porcentos foi o aumento do seu salario:"))
valoraumento = wage*(aumento/100)
print(f"seu aumento foi de: {valoraumento}")
salarionovo= wage+valoraumento
print(f"seu salario depois do aumento é: {salarionovo}")

