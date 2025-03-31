from selectors import SelectSelector

time1= input("digite nome do primeiro time: ")
time2= input("digite nome do segundo time: ")
golstime1= float(input(f"quantos gols o {time1} fez? "))
golstime2= float(input(f"quantos gols o {time2} fez? "))
if golstime1>golstime2:
    print (f"vitoria do {time1}")
else:
    if golstime1==golstime2:
        print ("empate")
    else:
        print(f"derrota do {time1}")
