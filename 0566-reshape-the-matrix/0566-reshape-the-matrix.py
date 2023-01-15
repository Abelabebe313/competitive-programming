class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        converted = []
        reshaped = []
        if (r * c) == len(mat) * len(mat[0]):
            for m in range(len(mat)):
                for n in range(len(mat[0])):
                    converted.append(mat[m][n])
            for row in range(r):
                temp = []
                for col in range(c):
                    temp.append(converted[0])
                    converted.pop(0)
                reshaped.append(temp)
            return reshaped
        else:
            return mat
                