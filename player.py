class Player:
    """
    Создаем класс игрока Player.
    """
    def __init__(self, user_name, words_used):
        """
        Метод инициализации класса Player.
        """
        self.user_name = user_name
        self.words_used = words_used

    def __repr__(self):
        """
        Метод сущности экземпляра.
        """
        return f'Вас зовут - {self.user_name}, вы ввели следующие слова - {self.words_used})'

    def count_words_used(self):
        """
        Метод получения количества использованных слов.
        """
        return len(self.words_used)

    def add_word(self, word):
        """
        Метод добавления слова в список использованных слов
        """
        self.words_used.append(word)

    def checking_use_word_before(self, word):
        """
        Метод проверки использованности слова
        """
        return word in self.words_used()
