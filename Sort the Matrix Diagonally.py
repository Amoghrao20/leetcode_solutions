class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])

        # looing over the top
        for diagonal in range(cols):

            # getting the diagonal elements in a list
            l = []
            i = 0
            j = diagonal
            while i < rows and j < cols:
                l.append(mat[i][j])
                i += 1
                j += 1

            # sorting and putting back the elements
            l.sort()
            i = k = 0
            j = diagonal
            while i < rows and j < cols:
                mat[i][j] = l[k]
                i += 1
                j += 1
                k += 1

        # looing over the right side
        for diagonal in range(rows):

            # getting the diagonal elements in a list
            l = []
            i = diagonal
            j = 0
            while i < rows and j < cols:
                l.append(mat[i][j])
                i += 1
                j += 1

            # sorting and putting back the elements
            l.sort()
            j = k = 0
            i = diagonal
            while i < rows and j < cols:
                mat[i][j] = l[k]
                i += 1
                j += 1
                k += 1

        return mat
