tomlist = []
tall = 1 
while tall!= 0:
    tall = int(input("Skriv et tall!: "))
    tomlist.append(tall)
for element in tomlist:
    print(element)
minSum = 0
for element in tomlist:
    minSum += element
print("Min sum er: ", minSum)

minst = tomlist[0]
for min in tomlist:
    if min < minst:
        minst = min
print("Minste element i listen er: ", minst)

max = tomlist[0]
for min in tomlist:
    if min > max:
        max = min
print("Største verdi i listen er: ", max)

    
