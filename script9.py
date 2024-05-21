lets = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
class Graph:
    def __init__(self, size):
        self.size = size
        self.distances_matrix = [[0] * size for i in range(size)]  # матрица смежности
        self.vershins = [lets[i] for i in range(size)]

    def set_edge(self, v1, v2, w1, w2):
        # если w1 и w2 совпадают, то это ребро
        # если w1 или w2 равен нулю, то это дуга
        # иначе - 2 дуги
        self.distances_matrix[v1][v2] = w1
        self.distances_matrix[v2][v1] = w2

    def deikstra(self, vershina):
        sv_ind = self.vershins.index(vershina)
        distances = [float("inf")] * self.size
        predecessors = [None] * self.size
        distances[sv_ind] = 0  # изначальная вершина
        visited = [False] * self.size

        for i in range(self.size):
            min_distance = float("inf")
            v = None

            # смотрим, от какой вершины отталкиваемся
            for j in range(self.size):
                if not visited[j] and distances[j] < min_distance:
                    min_distance = distances[j]
                    v = j

            if v is None:
                break

            visited[v] = True

            # отмечаем расстояние от этой вершины до соседей, если оно меньше ранее найденного
            for j in range(self.size):
                if self.distances_matrix[v][j] != 0 and not visited[j]:
                    distance = distances[v] + self.distances_matrix[v][j]
                    if distance < distances[j]:
                        distances[j] = distance
                        predecessors[j] = v

        return distances, predecessors

    def get_path(self, predecessors, start, end):
        path = []
        current = self.vershins.index(end)
        while current is not None:
            path.append(self.vershins[current])
            current = predecessors[current]
            if current == self.vershins.index(start):
                path.append(start)
                break

        return path[::-1]


