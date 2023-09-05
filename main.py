from word_frequency_parser.text_file_processor import TextFileProcessor
from word_frequency_parser.text_analyzer import TextAnalyzer
from word_frequency_parser.word_frequency_parser import WordFrequencyParser

if __name__ == "__main__":
    # Задаем начальные ссылки для парсинга
    initial_links = ["https://go.dev"]

    # Определяем разрешенные части речи и минимальную частоту вхождения
    allowed_pos = ['NN', 'VB', 'JJ', 'RB']  # Подлежащее, глагол, прилагательное, наречие
    min_frequency = 20  # Минимальное количество вхождений слова

    # Создаем экземпляр класса TextAnalyzer с заданными параметрами
    text_analyzer = TextAnalyzer(allowed_pos, min_frequency)

    # Создаем экземпляр класса WordFrequencyParser, который будет анализировать текст
    # и получать частоту встречаемости слов
    parser = WordFrequencyParser(initial_links, text_analyzer)

    # Начинаем процесс парсинга
    parser.start_parsing()

    # Получаем частоту встречаемости слов
    words_frequency = parser.get_words_frequency()

    # Задаем путь к текстовому файлу, в который мы хотим добавить слова
    file_path = "words.txt"

    # Создаем экземпляр класса TextFileProcessor, который будет работать с файлом
    file_processor = TextFileProcessor(file_path)

    # Читаем строки из файла
    lines_from_file = file_processor.read_file_lines()

    # Объединяем слова из файла и слова, полученные после анализа
    # и перезаписываем файл с обновленными данными
    file_processor.merge_lists_and_write_to_file(lines_from_file, words_frequency)

    # Выводим список слов
    print(words_frequency)
