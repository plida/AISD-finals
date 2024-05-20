import sorting
import random
import timeit
import test_sorting

print("-= ЗАДАНИЕ №3 =-")
ARR = [[random.randint(1, 100) for i in range(100)], [random.randint(1, 100) for i in range(1000)],
       [random.randint(1, 100) for i in range(10000)]]


def get_trio(arr, type, table):
    results = test_sorting.test(arr)
    to_round = 5
    table.append([len(arr), type, round(results[0], to_round), round(results[1], to_round), round(results[2], to_round)])
    table.append([len(arr), type, round(results[0], to_round), round(results[1], to_round), round(results[2], to_round)])
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
print("o" + "-"*60 + "o")
for row in table:
    print("|{:<8} {:<15} {:<11} {:<11} {:<11}|".format(*row))
print("o" + "-"*60 + "o")
print("-= ЗАДАНИЕ №8 =-")


print("-= ЗАДАНИЕ №9 =-")