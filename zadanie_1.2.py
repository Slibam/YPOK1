print("Введите число: ")
num = input()
Sum1 = int(num[0]) + int(num[1]) + int(num[2])
Sum2 = int(num[3]) + int(num[4]) + int(num[5])
if len(num)==6:
        if Sum1 == Sum2:
                print (f"билетик с номером {num} является счастливым")
        else:
                print(f"билетик с номером {num} не является счастливым")