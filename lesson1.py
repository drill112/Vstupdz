# num = input("Введіть тризначне число: ")
#
# a = int(num[0])
# b = int(num[1])
# c = int(num[2])
#
# if a < b < c:
#     print("зростаюче")
# elif a > b > c:
#     print("спадаюче")
# else:
#     print("різне")

#2
# password = input("Введіть пароль (4 цифри): ")
#
# digits = list(password)
# unique_digits = set(digits)
#
# if len(unique_digits) == 1:
#     print("відкрито")
# elif len(unique_digits) == 2:
#     print("тривога")
# else:
#     print("нічого")

#3
profit = int(input("Введіть прибуток: "))

if profit < 10000:
    bonus = profit * 0.05
elif profit <= 50000:
    bonus = profit * 0.07
else:
    bonus = profit * 0.10

if profit % 10 == 7:
    bonus *= 2

print("Бонус:", bonus)


