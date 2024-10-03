# where my numRows is 5
def generate(self, numRows):
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0] # [0,1,0] in 1st iteration
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1]) # 0+1 in the 1st iteration
            res.append(row)
        return res
 

        # T : O(n^2) - n is total number of elements and another n is length of each n.
        # S : O(n)
        
        # pascal's triangle
        # formulae to find the number of rows present in pascal's triangle, when the rows is given; i.e rows = 5
        # 1+2+3+…+numRows = (numRows×(numRows+1)) /2
