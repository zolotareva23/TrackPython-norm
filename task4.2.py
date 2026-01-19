import csv
import json

# TODO импортировать необходимые модули
# ← уже сделано: import csv, import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Первая строка — заголовки
        for row in reader:
            # Создаём словарь: {столбец: значение}
            record = dict(zip(headers, row))
            data.append(record)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    # Для проверки: выводим содержимое output.json
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end='')