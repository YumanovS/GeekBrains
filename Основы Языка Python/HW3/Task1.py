numbers = {
    "zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
    "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"
}


def num_translate(word):
    try:
        return numbers[word]
    except:
        return None


print(num_translate("ten"))
