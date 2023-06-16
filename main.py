# для работы необходимо установить библиотеку numpy
import numpy as np


# извлечение матрицы из файла происходит в матрицу numpy
def getting_matrix_from_file_and_using_floyd_warshall_algorithm(file_name):
    with open(f'{file_name}', 'r') as f:
        elems = f.read().replace('~', str(np.iinfo(np.int32).max)).split('\n')
        if elems[-1] == '':
            elems = elems[:-1]

    vertex_1, vertex_2 = elems[-1].split(' ')
    elems = elems[1:-1]

    matrix = np.array([[np.int64(x) for x in el.split(" ")] for el in elems])
    matrix_with_steps = np.tile(np.arange(matrix.shape[0]), (matrix.shape[0], 1))

    floyd_warshall(matrix, matrix_with_steps)
    find_min_between_two_vertexes(matrix_with_steps, vertex_1, vertex_2)

    return


# алгоритм Флойда по поиску минимального пути между парами вершин
def floyd_warshall(matrix, matrix_with_steps):
    for k in range(matrix.shape[0]):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[0]):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    matrix_with_steps[i][j] = k  # номер промежуточной вершины между i и j

    with open('output.txt', 'w') as f:
        for row in matrix:
            f.write((' '.join(map(str, row)).replace(str(np.iinfo(np.int32).max), '~')) + '\n')
    return


# поиск минимального пути между вершинами
def find_min_between_two_vertexes(matrix, vertex_1, vertex_2):
    start = np.int64(vertex_1) - 1
    end = np.int64(vertex_2) - 1
    path = [start + 1]

    while end - 1 != start - 1:
        start = matrix[start][end]
        path.append(start + 1)

    with open('output.txt', 'a') as f:
        f.write(' '.join(map(str, path)))

    return


if __name__ == '__main__':
    getting_matrix_from_file_and_using_floyd_warshall_algorithm('input.txt')
