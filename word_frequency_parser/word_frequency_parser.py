import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List


class WordFrequencyParser:
    """
    Класс для парсинга и анализа текста с веб-страниц.
    """

    def __init__(self, initial_links: List[str], text_analyzer):
        """
        Инициализация парсера.

        Args:
            initial_links (List[str]): Список начальных ссылок для парсинга.
            text_analyzer: Экземпляр класса для анализа текста.
        """
        self.links = initial_links
        self.text_analyzer = text_analyzer
        self.words_frequency = {}
        self.base_urls = set(initial_links)  # Преобразуем список в множество для уникальности базовых URL

    def parse_links(self, link: str) -> None:
        """
        Парсит ссылки на веб-странице и анализирует текст.

        Args:
            link (str): Ссылка на веб-страницу.

        Returns:
            None
        """
        try:
            response = requests.get(link)
            response.raise_for_status()  # Проверяем статус ответа
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            self.text_analyzer.analyze_text(text)
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                absolute_url = urljoin(link, href)  # Преобразуем относительную ссылку в абсолютную
                if any(absolute_url.startswith(base_url) for base_url in self.base_urls):  # Проверяем, что ссылка начинается с одного из базовых URL
                    if absolute_url not in self.links:
                        self.links.append(absolute_url)
                        print(absolute_url)
        except Exception as e:
            print(f"Error parsing link {link}: {str(e)}")

    def start_parsing(self) -> None:
        """
        Начинает процесс парсинга, обходя все ссылки.

        Returns:
            None
        """
        while self.links:
            link = self.links.pop(0)
            self.parse_links(link)

        self.text_analyzer.filter_non_english_words()
        self.text_analyzer.filter_by_allowed_pos()

    def get_words_frequency(self) -> List[str]:
        """
        Возвращает список уникальных слов, которые соответствуют заданным условиям.

        Returns:
            List[str]: Список слов.
        """
        return self.text_analyzer.get_word_frequency()
