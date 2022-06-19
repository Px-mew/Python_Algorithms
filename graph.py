from collections import deque

"""Создание графа и обход графа в ширину. Вершины графа называются целыми числами начиная с 0."""

# Вводится количество вершин и количество ребер
num_vertex, num_edge = map(int, input('Введите количство вершин и количество ребер через пробел: ').split())

# Представление графа - списки смежности
graph = {i: set() for i in range(num_vertex)}
start_vertex = ''
for i in range(num_edge):
    # Ввод ребра.
    v1, v2 = map(int, input('Введите начальную и конечную вершину ребра через пробел: ').split())
    # Вершина для начала обхода
    if start_vertex == '':
        start_vertex = v1
    # Добавляется смежность двух вершин
    graph[v1].add(v2)
    graph[v2].add(v1)

# Массив расстояний по умолчанию None
distances = [None] * num_vertex
# Расстояние до себя = 0
distances[start_vertex] = 0
# Создание очереди
queue = deque([start_vertex])
# Пока очередь не пуста
while queue:
    # Достаем 1 элемент
    cur_v = queue.popleft()
    # Перебор всех его "соседей"
    for neigh_v in graph[cur_v]:
        # Если "сосед" еще не посещен
        if distances[neigh_v] is None:
            # Считается расстояние
            distances[neigh_v] = distances[cur_v] + 1
            # "Сосед" добавляется в очередь, чтобы перебрать его "соседей"
            queue.append(neigh_v)
# Вывод расстояния
print(distances)