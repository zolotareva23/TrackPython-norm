class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Свойство только для чтения: название книги"""
        return self._name

    @property
    def author(self) -> str:
        """Свойство только для чтения: автор книги"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None  # Инициализируем приватный атрибут
        self.pages = pages  # Используем сеттер для проверки

    @property
    def pages(self) -> int:
        """Свойство для получения количества страниц"""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Сеттер для количества страниц с проверкой"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        # Перегружаем __str__ для добавления информации о страницах
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        # Перегружаем __repr__ для отображения всех атрибутов
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float | str | int):
        """
        Args:
            name: Название книги
            author: Автор книги
            duration: Продолжительность (может быть float, int или строкой с числом)
        """
        super().__init__(name, author)
        self._duration = None  # Инициализируем приватный атрибут
        self.duration = duration  # Используем сеттер для проверки

    @property
    def duration(self) -> float:
        """Свойство для получения продолжительности"""
        return self._duration

    @duration.setter
    def duration(self, value: float | str | int):
        """Сеттер для продолжительности с проверкой"""
        # Проверяем, можно ли преобразовать значение к float
        try:
            float_value = float(value)
        except (TypeError, ValueError):
            raise TypeError("Продолжительность должна быть числом")

        if float_value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float_value

    def __str__(self):
        # Перегружаем __str__ для добавления информации о продолжительности
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} ч."

    def __repr__(self):
        # Перегружаем __repr__ для отображения всех атрибутов
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования:
if __name__ == "__main__":
    # Создаем книги
    book = Book("1984", "Джордж Оруэлл")
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)

    # Создаем аудиокниги с разными типами продолжительности
    audio_book1 = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 15.5)  # float
    audio_book2 = AudioBook("Преступление и наказание", "Федор Достоевский", 20)  # int
    audio_book3 = AudioBook("Маленький принц", "Антуан де Сент-Экзюпери", "8.75")  # str

    print(book)
    print(repr(book))
    print()

    print(paper_book)
    print(repr(paper_book))
    print()

    print(audio_book1)
    print(repr(audio_book1))
    print()

    print(audio_book2)
    print(repr(audio_book2))
    print()

    print(audio_book3)
    print(repr(audio_book3))
    print()

    # Проверка валидации
    try:
        invalid_paper_book = PaperBook("Тест", "Автор", -100)
    except ValueError as e:
        print(f"Ошибка валидации страниц: {e}")

    try:
        invalid_audio_book = AudioBook("Тест", "Автор", "не число")
    except TypeError as e:
        print(f"Ошибка валидации продолжительности: {e}")

    # Демонстрация, что свойства name и author нельзя изменить
    print(f"\nИмя книги: {book.name}")
    print(f"Автор книги: {book.author}")

    # Попытка изменить напрямую вызовет ошибку
    # book.name = "Новое название"  # AttributeError: can't set attribute
    # book.author = "Новый автор"   # AttributeError: can't set attribute