def count_letters(text):
    counts = {}
    order = []
    for ch in text:
        if ch.isalpha():
            lower_ch = ch.lower()
            if lower_ch not in counts:
                counts[lower_ch] = 0
                order.append(lower_ch)
            counts[lower_ch] += 1
    return counts, order

def calculate_frequency(counts):
    total = sum(counts.values())
    freq = {}
    for letter, cnt in counts.items():
        # Оставляем число, но форматируем при выводе
        freq[letter] = cnt / total
    return freq

main_str = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо – песнь заводит,
Налево – сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""

letter_counts, appearance_order = count_letters(main_str)
frequencies = calculate_frequency(letter_counts)

for char in appearance_order:
    print(f"{char}: {frequencies[char]:.2f}")