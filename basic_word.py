class BasicWord:
    """
    Создаем класс слов и допустимых слов игры
    """
    def __init__(self, word, acceptable_words):
        """
        Метод инициализации класса BasicWord.
        """
        self.word = word
        self.acceptable_words = acceptable_words

    def __repr__(self):
        """
        Метод сущности экземпляра.
        """
        return f'Выбранное слово - {self.word}, а его допустимый набо слов - {self.acceptable_words})'

    def checking_word(self, user_input):
        """
        Метод , проверяющий, является ли слово подсловом
        """
        if user_input in self.acceptable_words:
            return True
        else:
            return False

    def count_acceptable_words(self):
        """
        Метод получения количества подслов
        """
        return len(self.acceptable_words)
