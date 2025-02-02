class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Изменение имени невозможно")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        raise AttributeError("Изменение автора невозможно")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Страницы: {self.pages}"

    def __repr__(self):
        return f"{super().__repr__().rstrip(')')}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}. Продолжительность: {self.duration:.2f} часов"

    def __repr__(self):
        return f"{super().__repr__().rstrip(')')}, duration={self.duration!r})"