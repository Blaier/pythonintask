# Задача 3. Вариант 45.
# Напишите программу, которая выводит имя "Мартин Андерсен", и запрашивает его псевдоним. Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Burmistrov V.D.
# 17.03.2016

name = "Мартин Андерсен"
print("Герой нашей сегоднящней программы - " + name)
alias = input("Под каким же именем мы знаем этого человека? Ваш ответ: ")

print("Все верно: " + name + " - " + alias)

input("\n\nНажмите Enter для выхода.")
