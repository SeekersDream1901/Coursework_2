# Импортируем необходимые классы и функции
# from basic_word import BasicWord
from player import Player
from utils import *

# Спрашиваем у игрока его имя и присваиваем его переменной user_name
user_name = input("Введите имя игрока\n")

# Создаем экземпляр класса Player
# Первая переменная имя, вторая список использованных слов (по умолчанию пустой)
player = Player(user_name, [])

DATA_SOURCE = "https://jsonkeeper.com/b/AYX4"
# Используя функцию получаем случайное слово для игры из списка
random_word = load_random_word(DATA_SOURCE)

# Программа здаровается с игроком, высвечивает необходимую информацию и предлагает начать
welcome_message(player, random_word)

# Запускаем цикл
# Пока список использованных слов не будет равен списку допустимых слов
while player.count_words_used() != random_word.count_acceptable_words():
    # Получаем ввод от игрока
    player_input = input().lower()
    # Если ввод игрока равен "stop" или "стоп", то игра прекращается с подсчетом правильных ответов
    if player_input == "stop" or player_input == "стоп":
        break

    # Иначе играем
    else:
        # Если введенное слово игроком есть в списке уже использованных слов
        if player_input in player.words_used:
            print("Уже использовано")

        # Если введенное слово игроком есть в списке слов программы
        elif player_input in random_word.acceptable_words:
            # Добавляем его в список использованных слов
            player.add_word(player_input)
            print('Верно')

        # Если длина введенного слова игроком меньше чем длинна самого маленького слова в списке
        elif len(player_input) < min_len_acceptable_words(random_word.acceptable_words):
            print("Слишком короткое слово")

        # Если введенное слово игроком нет в списке допустымых слов
        elif player_input not in random_word.acceptable_words:
            print("Неверно")

# Если колличество отгаданных слов равно колличеству допустимых слов
if player.count_words_used() == random_word.count_acceptable_words():
    print("Вы отгадали все слова")
else:
    print(f'Игра завершена, вы угадали {player.count_words_used()} слов!')
