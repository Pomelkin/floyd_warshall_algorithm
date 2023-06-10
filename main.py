import numpy as np


# функция извлечение матрицы из файла в матрицу numpy
def get_matrix_from_file(file_name):
    with open(f'Data/{file_name}', 'r') as f:
        elems = f.read().replace('~', str(np.iinfo(np.int32).max)).split('\n')
    vertex_1, vertex_2 = elems[-1].split(' ')
    elems = elems[1:-1]

    with open('Data/for_test.txt', 'w') as f:
        f.write('\n'.join(elems).replace(' ', ', '))

    matrix = np.array([[np.int64(x) for x in el.split(" ")] for el in elems])
    print(matrix)
    matrix_for_steps = np.tile(np.arange(matrix.shape[0]), (matrix.shape[0], 1))
    floyd_warshall(matrix, matrix_for_steps)
    find_min_between_two_vertexes(matrix_for_steps, vertex_1, vertex_2)


# алгоритм Флойда по поиску минимального пути между парами вершин
def floyd_warshall(matrix, matrix_for_steps):
    for k in range(matrix.shape[0]):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[0]):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    matrix_for_steps[i][j] = k

    with open('Data/output.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


# поиск минимального пути между вершинами
def find_min_between_two_vertexes(matrix, vertex_1, vertex_2):
    start = np.int64(vertex_1) - 1
    end = np.int64(vertex_2) - 1
    path = [end + 1]
    while end - 1 != start - 1:
        end = matrix[end][start]
        path.append(end + 1)
    path = path[::-1]

    with open('Data/output.txt', 'a') as f:
        f.write(' '.join(map(str, path)))


if __name__ == '__main__':
    get_matrix_from_file('input.txt')
