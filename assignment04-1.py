#1.using list
#Addition of two matrices using lists.
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = [[0,0],[0,0]]

for i in range(2):
    for j in range (2):
        C[i][j] = A[i][j]+B[i][j]
        
        print("Resultant Matrix:")
        print(C)
        
        
        