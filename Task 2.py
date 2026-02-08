class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")