import nltk
from nltk.corpus import words
from nltk import word_tokenize, pos_tag
from typing import List

# Загрузка необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')


class TextAnalyzer:
    """
    Класс для анализа текста, включая фильтрацию по частям речи и частоте встречаемости.
    """

    def __init__(self, allowed_pos: List[str] = None, min_frequency: int = 1):
        """
        Инициализация анализатора текста.

        Args:
            allowed_pos (List[str], optional): Список разрешенных частей речи для анализа. По умолчанию None.
            min_frequency (int, optional): Минимальная частота вхождения слова в текст для сохранения. По умолчанию 1.
        """
        self.words_frequency = {}
        self.allowed_pos = allowed_pos
        self.min_frequency = min_frequency
        self.english_words = set(words.words())

    def analyze_text(self, text: str) -> None:
        """
        Анализирует текст и обновляет словарь частотности слов.

        Args:
            text (str): Текст для анализа.

        Returns:
            None
        """
        # Разбиваем текст на слова
        tokens = word_tokenize(text)
        # Проводим анализ каждого слова и обновляем словарь частотности
        for token in tokens:
            self.update_word_frequency(token)

    def update_word_frequency(self, word: str) -> None:
        """
        Обновляет словарь частотности слов.

        Args:
            word (str): Слово для обновления.

        Returns:
            None
        """
        word = word.lower()
        if word.isalpha():
            self.words_frequency[word] = self.words_frequency.get(word, 0) + 1

    def filter_non_english_words(self) -> None:
        """
        Фильтрует слова, оставляя только английские и частотой вхождения не менее min_frequency.

        Returns:
            None
        """
        self.words_frequency = {word: freq for word, freq in self.words_frequency.items() if
                                word in self.english_words and freq >= self.min_frequency}

    def filter_by_allowed_pos(self) -> None:
        """
        Фильтрует слова по разрешенным частям речи.

        Returns:
            None
        """
        if self.allowed_pos is None:
            return
        tagged_words = pos_tag(self.words_frequency.keys())
        self.words_frequency = {word: freq for (word, pos), freq in zip(tagged_words, self.words_frequency.values()) if
                                pos in self.allowed_pos}

    def get_word_frequency(self) -> List[str]:
        """
        Возвращает список уникальных слов, которые соответствуют заданным условиям.

        Returns:
            List[str]: Список слов.
        """
        return list(self.words_frequency.keys())
