print("Введите число: ")
number = input()
result = 0
while (int(number) > 0):
    f = int(number) % 10
    result = result + f
    number = int(number) / 10
print()
print(f"Cумма цифр в числе: {result}")