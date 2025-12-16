disk_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_bytes = disk_mb * 1024 * 1024
book_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

books_count = int(disk_bytes // book_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
