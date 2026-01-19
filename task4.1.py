import json


def calculate_sum_from_file(file_path):
    """
    Вычисляет сумму произведений score * weight из JSON файла
    и возвращает результат, округленный до 3 знаков после запятой
    """
    try:
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Если данные не обернуты в массив, добавляем квадратные скобки
        if not content.strip().startswith('['):
            # Удаляем лишние запятые в конце, если они есть
            content = content.rstrip(',\n')
            content = f'[{content}]'

        # Парсинг JSON
        data = json.loads(content)

        # Вычисление суммы произведений
        total = 0.0
        for item in data:
            score = item.get('score', 0)
            weight = item.get('weight', 0)
            total += score * weight

        # Округление до 3 знаков после запятой
        rounded_total = round(total, 3)

        return rounded_total

    except Exception:
        return None


# Основная часть программы
if __name__ == "__main__":
    # Вычисляем сумму из файла data.json
    result = calculate_sum_from_file('input.json')

    # Выводим только результат (число)
    if result is not None:
        print(result)