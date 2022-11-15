# Импортируем необходимые модули и классы
import json
import requests
import random
from basic_word import BasicWord


def load_random_word(source):
    """
    Функция получения случайного слова из файла json,
    в котором содержаться слова и список из слов
    которые можно составить.
    """
    # Получаем ответ на запрос источника данных
    response = requests.get(source)

    # Распаковываем файл json
    content = json.loads(response.text)

    # Получаем случайное слово
    random_word = random.choice(content)

    # Создаем экземпляр класса BasicWord, используя случайное слово
    word_for_game = BasicWord(random_word["word"], random_word["subwords"])

    # Возвращаем экземпляр класса
    return word_for_game


def welcome_message(player, random_word):
    """
    Приветственное сообщение
    """
    # Программа здоровается с игроком используя имя экземпляра класса Player.
    print(f"Привет, {player.user_name}!")
    # Считает колличество слов в списке допустимых слов и выводит значение.
    # Считывает слово, подобранное для игры.
    print(f"Составьте {random_word.count_acceptable_words()} слов из слова {random_word.word}")
    # Находит наименьшее слово в списке допустимых слов и выводит его длину.
    print(f"Слова должны быть не короче {min_len_acceptable_words(random_word.acceptable_words)} букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop" ')
    print("Поехали, ваше первое слово?")


def min_len_acceptable_words(acceptable_words):
    """
    Возвращает минимальную длинну слова из списка допустимых слов
    """
    # Задаем первоначальное значение минимальной длины
    minimum_length = 4

    # Перебираем слова из списка допустимых слов
    for word in acceptable_words:

        # Если длина слова меньше, чем значение минимальной длины
        if len(word) < minimum_length:
            # Призваиваем новое значение минимальной длины
            minimum_length = len(word)

    return minimum_length
