string = "процент"
number = int(input("Введите число: "))

if number <= 1:
    print(f"{number} {string}")
elif number < 5:
    print(f"{number} {string}а")
else:
    print(f"{number} {string}ов")

for number in range(1,20):
    if number <= 1:
        print(f"{number} {string}")
    elif number < 5:
        print(f"{number} {string}а")
    else:
        print(f"{number} {string}ов")
