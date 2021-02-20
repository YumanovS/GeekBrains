import random

l = []
for i in range(1,21):
    l.append(round(random.uniform(1,100),2))
print(l)

for i in range(len(l)):
    temp = str(l[i]).rsplit(".")
    if len(temp[1]) == 2:
        print(temp[0] + " руб " + temp[1] + " коп")
    else:
        print(temp[0] + " руб " + temp[1] + "0" + " коп")
l.sort()
l1 = []
for i in range(len(l)):
    l1.append(l[i])
l1.reverse()
print(l)
print(l1)
print(l1[:5])