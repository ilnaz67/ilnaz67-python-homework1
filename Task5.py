numbers_input = input("Введите числа через пробел: ")

numbers = list(map(int, numbers_input.split()))

squares = list(map(lambda x: x ** 2, numbers))

print("Результат:", *squares)