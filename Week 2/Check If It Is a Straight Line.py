# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

 

# Constraints:

#     2 <= coordinates.length <= 1000
#     coordinates[i].length == 2
#     -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#     coordinates contains no duplicate point.

#    Hide Hint #1  
# If there're only 2 points, return true.
#    Hide Hint #2  
# Check if all other points lie on the line defined by the first 2 points.
#    Hide Hint #3  
# Use cross product to check collinearity.







class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        print(len(coordinates))
        c=len(coordinates)
        if c==2:
            return True
        
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        for i in range(2,c):
            x,y=coordinates[i]
            if (y1-y0)*(x-x0)!=(y-y0)*(x1-x0):
                return False
        return True
#         x=coordinates[1][0]-coordinates[0][0]
#         y=coordinates[1][1]-coordinates[0][1]
        
#         s=y/x
#         print(s)
#         print(x,y)
#         m=[]
#         n=[]
#         for i in coordinates:
#             print(i)
#             m.append(i[0])
#             n.append(i[1])
#         print(m,n)
#         l=s
#         for i in range(0,(c-1)):
            
#             k=(n[i+1]-n[i])/(m[i+1]-m[i])
            
#             if (l==k):
#                 pass
#             else:
#                 return False
#             l=k
        # [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
               
            
            
        
        
        
