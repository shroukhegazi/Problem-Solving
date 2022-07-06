
import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n= len(mat)
        m= len(mat[0])
        if n*m ==r*c:
            np_arr=np.array(mat)
            reshaped_mat= np.reshape(mat, (r, c))
            return reshaped_mat  
        else:
            return mat

        
