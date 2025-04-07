
hora1=int(input("digite hora1: "))
minuto1=int(input("digite minuto1: "))
hora2=int(input("digite hora2: "))
minuto2=int(input("digite minuto2: "))
somahoras= hora1 + hora2
somaminutos= minuto1 + minuto2
if somahoras > 12:
    somahoras= somahoras -12
if somaminutos >= 60:
    somaminutos= somaminutos -60
    somahoras= somahoras +1
if somahoras > 24:
   somahoras= somahoras -24
print (f"{somahoras}:{somaminutos}")