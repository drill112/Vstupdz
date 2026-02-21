# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average_grade(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#
# student1 = Student("Alice", [90, 85, 88])
#
# print("Имя:", student1.name)
# print("Средний балл:", student1.average_grade())

#2
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average_grade(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#
# class StudentGroup:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def best_student(self):
#         if not self.students:
#             return None
#         return max(self.students, key=lambda s: s.average_grade())
#
#     def __iter__(self):
#         return iter(self.students)
#
#
#
# s1 = Student("Alice", [90, 85, 88])
# s2 = Student("Bob", [75, 80, 70])
# s3 = Student("Charlie", [95, 92, 96])
#
# group = StudentGroup()
# group.add_student(s1)
# group.add_student(s2)
# group.add_student(s3)
#
# best = group.best_student()
# print("Самый успешный:", best.name, round(best.average_grade(), 2))
#
# print("Все студенты:")
# for student in group:
#     print(student.name, round(student.average_grade(), 2))

#3
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        elif amount <= 0:
            print("Сумма должна быть положительной")
        else:
            self.balance -= amount
            print(f"Снятие {amount}. Новый баланс: {self.balance}")

    def get_balance(self):
        return self.balance



account = BankAccount("123456789", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

print("Текущий баланс:", account.get_balance())