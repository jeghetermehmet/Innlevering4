i = 0
my_list = []
while i < 10:
    my_list.append(i)
    i += 1
min_list = []
for i in range(10):
    min_list.append(i)

mine_tall = []
teller = 0
while teller< 20:
    mine_tall.append(teller)
    teller+=3
for tall in mine_tall:
    print(tall)

for indeks in range(len(mine_tall)):
    print(indeks)

for tall in range(len(mine_tall)):
    mine_tall[tall] *= 10
    print(mine_tall[tall])
    


        