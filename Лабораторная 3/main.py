from typing import Union


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Инициализируем экземпляр класса Book

        :param name: название книги
        :param author: имя автора
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть типа str")
        self._author = author

    def __str__(self) -> str:
        """
        Магический метод отвечает за читабельный вывод экземпляра класса

        :return: строка формата - Книга 'название книги'. Автор: имя автора
        """
        return f"Книга '{self.name}'. Автор: {self.author}"

    def __repr__(self) -> str:
        """
        Магический метод отвечает за вывод экземпляра класса, по которому можно инициализировать экземпляр класса

        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """
        Свойство возвращает защищенный атрибут - название книги

        :return: значение _name
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Свойство возвращает защищенный атрибут - имя автора

        :return: значение _author
        """
        return self._author


class PaperBook(Book):
    """Дочерний от Book класс бумажной книги"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экземпляра класса PaperBook с конструктором родительского класса

        :param name: название книги
        :param author: имя автора
        :param pages: количество страниц в книге
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """
        Магический метод отвечает за вывод экземпляра класса, по которому можно инициализировать экземпляр класса

        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        """
        Свойство возвращает защищенный атрибут - количество страниц в книге

        :return: значение _pages
        """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """
        Свойство устанавливает защищенный атрибут - количество страниц в книге

        :param new_pages: количество страниц в книге
        :return:
        """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация экземпляра класса PaperBook с конструктором родительского класса

        :param name: название книги
        :param author: имя автора
        :param duration: длительность аудио-записи в минутах
        """
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        """
        Магический метод отвечает за вывод экземпляра класса, по которому можно инициализировать экземпляр класса

        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> int:
        """
        Свойство возвращает защищенный атрибут - длительность аудио-книги

        :return: значение _duration
        """
        return self._duration

    @duration.setter
    def duration(self, new_duration: Union[int, float]) -> None:
        """
        Свойство устанавливает защищенный атрибут - длительность аудио-книги

        :param new_duration: длительность аудио-записи в минутах
        :return:
        """
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Длительность должна быть типа int или float")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = new_duration


if __name__ == '__main__':
    simple_book = Book("Война и мир", "Лев Толстой")
    paper_book = PaperBook("Похождения бравого солдата Швейка", "Ярослав Гашек", 800)
    audio_book = AudioBook("Вишневый сад", "Антон Чехов", 138.5)

    for book in [simple_book, paper_book, audio_book]:
        print(book)
        print(repr(book))
