nota1= float(input("digite sua primeira nota: "))
nota2= float(input("digite sua segunda nota: "))
nota3= float(input("digite sua terceira nota: "))
media= (nota1+nota2+nota3)/3
if media>=7:
    print(f"sua media foi {media}, aprovado")
else:
    print (f"sua media foi {media}, aluno reprovado")