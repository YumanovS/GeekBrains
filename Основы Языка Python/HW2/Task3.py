llist = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
length = len(llist)
s = [0] * length
s1 = [0] * length



for i in range(length):
    llist[i] = ("Привет, " + (((llist[i]).rsplit(" ",1)[-1]).lower()).capitalize() + "!")

for i in range(length):
    print(llist[i])