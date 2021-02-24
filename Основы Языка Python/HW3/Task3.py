from random import choice

nouns = ["автомобиль" , "лес" , "огонь" , "город" , "дом"]
adverbs = ["сегодня" , "вчера" , "завтра" , "позавчера" , "ночью"]
adjectives = ["веселый" , "яркий" , "зеленый" , "утопичный" , "мягкий"]

def get_jokes(number , indicator = False):

    i = 1
    l = []

    length_nouns = len(nouns)
    length_adverbs = len(adverbs)
    length_adjectives = len(adjectives)

    min_length = min(length_adverbs, length_nouns, length_adjectives)

    """ 
    Проверяем введеный аргумент на допустимость при запрете повторов
    Отбераем случайные слова из списков
    Удаляем использованные слова
    """
    if indicator:
        if number <= min_length:
            while i <= number:
                noun = choice(nouns)
                adverb = choice(adverbs)
                adjective = choice(adjectives)
                l.append(f"{noun} {adverb} {adjective}")
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
                i += 1
            return l

        else:
            print("Введено слишком большое число")
            return None

        """
        Добавляем случайные слова без удаления из исходных списков, т.к. повторы разрешены
        """

    else:
        while i <= number:
            noun = choice(nouns)
            adverb = choice(adverbs)
            adjective = choice(adjectives)
            l.append(f"{noun} {adverb} {adjective}")
            i += 1
        return l

print(get_jokes(4,True))