numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)

total_sum = sum(num for num in numbers if num is not None)

average = total_sum / len(numbers)

numbers[none_index] = average

print("Измененный список:", numbers)