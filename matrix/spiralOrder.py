
class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        
        result = []
        
        while left < right and top < bottom:
            
#           Cover Top Row
            for i in range(left,right):
                result.append(matrix[top][i])
            top += 1
            
#           Cover Right Col
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
#           Traverse Bottom Row
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom -= 1
            
#           Traverse Left Col
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left += 1
        
        return result
