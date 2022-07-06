class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        for i in range(numRows):
            add=[]
            for j in range(i+1):
                if i==j or j==0:
                    add.append(1)
                else:
                    add.append(lst[i-1][j-1]+lst[i- 1][j])
            lst.append(add)

                      
        return lst            
                    
        

        
