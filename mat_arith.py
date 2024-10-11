# Sean A
# Matrix Arithmetic
# Use our new knowledge about matrixes to create

def get_dimensions(m1, m2):
    return len(m1), len(m2[0])


def mat_sum(m1, m2):
    height, width = get_dimensions(m1, m2)
    if height == len(m2) == len(m1[0]) == width:
        new = [[0] * width for _ in range(height)]
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                new[i][j] = m1[i][j] + m2[i][j]
        return new
    else:
        return "no solution"


def mat_mul(m1, m2):
    height, width = get_dimensions(m1, m2)
    if len(m1[0]) == len(m2):
        new = [[0] * width for _ in range(height)]
        columns = [[m2[x][y] for x in range(len(m2))] for y in range(width)]
        for y in range(height):
            for x in range(len(columns)):
                for i in range(len(columns[x])):
                    new[y][x] += m1[y][i] * columns[x][i]
        return new
    else:
        return "no solution"
