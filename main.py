import sorting
import random
import timeit
import test_sorting
import script8

print("-= ЗАДАНИЕ №3 =-")
ARR = [[random.randint(1, 100) for i in range(100)],
       [random.randint(1, 100) for i in range(1000)]]


def get_trio(arr, type, table):
    results = test_sorting.test(arr)
    to_round = 5
    table.append([len(arr), type, round(results[0], to_round), round(results[1], to_round), round(results[2], to_round)])


table = []

for arr in ARR:
    results = test_sorting.test(arr)
    arr_sorted = results[3]
    arr_reversed = arr_sorted[::-1]
    get_trio(arr, "случайный", table)
    get_trio(arr_sorted, "отсорт.", table)
    get_trio(arr_reversed, "отсорт. обрат", table)

print("o" + "-"*60 + "o")
print("|{:<8} {:<15} {:<11} {:<11} {:<11}|".format("Длина", "Тип массива", "Гибрид", "Heapsort", "Quicksort"))

c = 0
for row in table:
    if c % 3 == 0:
        print("|" + "-" * 60 + "|")
    print("|{:<8} {:<15} {:<11} {:<11} {:<11}|".format(*row))
    c += 1

print("o" + "-"*60 + "o")
print("-= ЗАДАНИЕ №8 =-")
res, words = script8.get_count("prestuplenie-i-nakazanie.txt")
print("Кол-во слов:", len(words))
print("Уникальное кол-во слов:", len(sorted(set(words))))
c = 0
print("o" + "-" * 26 + "o")
for r in res:
    print("|{:<15} {:>10}|".format(*r))
    c += 1
    if c == 10:
        break
print("o" + "-" * 26 + "o")
print("-= ЗАДАНИЕ №9 =-")