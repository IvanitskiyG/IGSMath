#Работа с матрицами
#©IGS Software, 2023

class Matrix:
    def __init__(self, content):
        self.content = content
        self.size = (len(content), len(content[0]))

    def getsize(self):
        return self.size
    
    def __add__(self, other):
        if self.size == other.size:
            res = Matrix(self.content)
            for i in range(self.size[0]):
                for j in range (self.size[1]):
                    res.content[i][j] += other.content[i][j]
            return res
        else:
            return Matrix([['ERROR']])

    def __mul__(self, other):
        ax, ay = self.size
        bx, by = other.size
        a = self.content
        b = other.content
        if ay == bx:
            resc = [([0] * by) for i in range(ax)]
            for i in range(ax):
                for j in range(by):
                    resc[i][j] = sum([a[i][k] * b[k][j] for k in range(ay)])
            return Matrix(resc)
        else:
            return Matrix([['ERROR']])

    def multipy(self, x):
        res = self.content
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] *= x
        return Matrix(res)

    def show(self):
        for line in self.content:
            print(*line, sep='\t')

    def det(self):
        if self.size[0] != self.size[1]:
            return 'ERROR'
        matrix = self.content
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        res = 0
        for i in range(n):
            minor = []
            for j in range(1, n):
                line = [matrix[j][k] for k in range(n) if k != i]
                minor.append(line)
            if i % 2:
                z = -1
            else:
                z = 1
            res += Matrix(minor).det() * z * matrix[0][i]
        return res
