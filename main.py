import sorting
import random
import timeit
import test_sorting
import script8
import script9

print("-= ЗАДАНИЕ №3 =-")
ARR = [[random.randint(1, 100) for i in range(100)],
       [random.randint(1, 100) for i in range(1000)]]


def get_trio(arr, type, table):
    results = test_sorting.test(arr.copy())
    to_round = 5
    row = [len(arr), type, round(results[0], to_round), round(results[1], to_round), round(results[2], to_round)]
    print("|{:<8} {:<15} {:<11} {:<11} {:<11}|".format(*row))

table = []
print("o" + "-"*60 + "o")
print("|{:<8} {:<15} {:<11} {:<11} {:<11}|".format("Длина", "Тип массива", "Гибрид", "Heapsort", "Quicksort"))
for arr in ARR:
    print("|" + "-" * 60 + "|")
    results = test_sorting.test(arr)
    arr_sorted = results[3]
    arr_reversed = arr_sorted[::-1]
    get_trio(arr, "случайный", table)
    get_trio(arr_sorted, "отсорт.", table)
    get_trio(arr_reversed, "отсорт. обрат", table)
print("o" + "-"*60 + "o")
print("-= ЗАДАНИЕ №8 =-")
res, words = script8.get_count("prestuplenie-i-nakazanie.txt")
c = 0
print("o" + "-" * 26 + "o")
for r in res:
    print("|{:<15} {:>10}|".format(*r))
    c += 1
    if c == 10:
        break
print("o" + "-" * 26 + "o")


print("-= ЗАДАНИЕ №9 =-")

g = script9.Graph(7)

g.set_edge(3, 3, 4, 4)
g.set_edge(3, 4, 2, 2)
g.set_edge(0, 2, 3, 3)
g.set_edge(0, 4, 4, 4)
g.set_edge(4, 2, 4, 4)
g.set_edge(4, 6, 5, 0)
g.set_edge(2, 5, 0, 5)
g.set_edge(1, 2, 2, 2)
g.set_edge(1, 5, 2, 2)
g.set_edge(6, 5, 5, 0)


distances, predecessors = g.deikstra('Г')
data = []
print("o" + "-" * 35 + "o")
print("|Рассматриваемая вершина: Г" + " "*9 + "|")
print("|" + "-" * 35 + "|")
for i in range(len(distances)):
    path = ">".join(g.get_path(predecessors, 'Г', g.vershins[i]))
    print(f"|{path[-1]}: {path:<{g.size*2}} Расстояние: {distances[i]:<{5}}|")
print("o" + "-" * 35 + "o")
