class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        f,ans=[],[]
        for i in mat:
            f+=i
        for i in range(r):
            ans+=[f[i*c:i*c+c]]
        return ans
        