llist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(llist)):
    if llist[i][0] in ['+',"-"]:
        if len(llist[i][1:]) == 1:
            llist[i] = "\"" + llist[i][0] + "0" + llist[i][1:] + "\""
        else:
            llist[i] = llist[i]
    elif llist[i].isdigit():
        if len(llist[i]) == 1:
            llist[i] = "\"" + "0" + llist[i] + "\""
        else:
            llist[i] = "\"" + llist[i] + "\""
    else:
        llist[i] = llist[i]
print(llist)