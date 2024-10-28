class Matrix:
    def __init__(self, n, m, fill=0):
        self.n = n
        self.m = m
        self.data = [[fill for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        return self.data[i][j]

    def set(self, i, j, value):
        self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError(
                "Nr coloane al primei matrice trebuie sa fie egal cu numarul de randuri al celeilalte matrice.")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                value = sum(self.get(i, k) * other.get(k, j) for k in range(self.m))
                result.set(i, j, value)
        return result

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)


matrix = Matrix(3, 3, fill=1)
print("Matrice initiala:")
print(matrix)

matrix.set(0, 1, 5)
print("\nMatrice dupa modificarea unui element:")
print(matrix)

transposed_matrix = matrix.transpose()
print("\nMatrice transpusa:")
print(transposed_matrix)

other_matrix = Matrix(3, 3, fill=2)
result_matrix = matrix.multiply(other_matrix)
print("\nRezultat inmultire:")
print(result_matrix)

matrix.apply(lambda x: x * 2)
print("\nMatrice aplicare lambda (inmultire cu 2):")
print(matrix)
