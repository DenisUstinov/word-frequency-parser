from typing import List


class TextFileProcessor:
    """
    Класс для обработки текстовых файлов.
    """

    def __init__(self, file_path: str):
        """
        Инициализация обработчика текстового файла.

        Args:
            file_path (str): Путь к текстовому файлу.
        """
        self.file_path = file_path

    def read_file_lines(self) -> List[str]:
        """
        Считывает строки из файла и возвращает их в виде списка.

        Returns:
            List[str]: Список строк из файла.
        """
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []

    def merge_lists_and_write_to_file(self, first_list: List[str], second_list: List[str]) -> None:
        """
        Объединяет два списка и перезаписывает файл новыми данными.

        Args:
            first_list (List[str]): Первый список.
            second_list (List[str]): Второй список.

        Returns:
            None
        """
        merged_list = list(set(first_list) | set(second_list))
        try:
            with open(self.file_path, 'w') as file:
                for item in merged_list:
                    file.write(item + '\n')
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
