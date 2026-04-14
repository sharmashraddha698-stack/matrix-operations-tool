import numpy as np

#Determining size of matrix:
no_of_rows=int(input("Enter number of rows in matrix:"))
no_of_columns=int(input("Enter number of columns in matrix:"))

#Taking row-wise matrix input:
matrix=[]
print("\nEnter matrix row-wise:\n")
for i in range(no_of_rows):
    row=list(map(int,input(f"\nEnter element of row{i+1} with spaces:").split()))
    matrix.append(row)
print("\nMatrix:",matrix) 

#Converting in a numpy array:
matrix=np.array(matrix)
print(matrix)

#making operation choice:
print("\nMenue:\n1.Transpose\n2.Addition\n3.Multiplication\n4.Subtraction\n5.Exit\nChoice:")
choice=int(input("Make your choice:"))
if choice==1:
    print("\nTranspose of given matrix is:",matrix.T)
elif choice==2:
    print("\nEnter second matrix:\n")  
    matrix_2=[]
    print("\nEnter matrix row-wise:\n")
    for i in range(no_of_rows):
        row=list(map(int,input(f"\nEnter element of row{i+1} with spaces:").split()))
        matrix_2.append(row)
    print("\nMatrix 2:",matrix_2) 

    #Converting in a numpy array:
    matrix_2=np.array(matrix_2)
    print(matrix_2) 
    print("\nAddition of two matrices",matrix+matrix_2) 
elif choice==3:
    no_of_rows_2=no_of_columns
    no_of_columns_2=int(input("Enter number of columns in matrix 2:"))
    print("\nEnter second matrix:\n")  
    matrix_2=[]
    print("\nEnter matrix row-wise:\n")
    for i in range(no_of_rows_2):
        row=list(map(int,input(f"\nEnter element of row{i+1} with spaces:").split()))
        matrix_2.append(row)
    print("\nMatrix 2:",matrix_2) 

    #Converting in a numpy array:
    matrix_2=np.array(matrix_2)
    print(matrix_2) 
    print("\nMultiplication of two matrices:",np.dot(matrix,matrix_2))
elif choice==4:
    print("\nEnter second matrix:\n")  
    matrix_2=[]
    print("\nEnter matrix row-wise:\n")
    for i in range(no_of_rows):
        row=list(map(int,input(f"\nEnter element of row{i+1} with spaces:").split()))
        matrix_2.append(row)
    print("\nMatrix 2:",matrix_2) 

    #Converting in a numpy array:
    matrix_2=np.array(matrix_2)
    print(matrix_2) 
    print("\nSubtraction  of two matrices",matrix-matrix_2)
elif choice==5:
    print("\nExited..")
else:
    print("\nInvalid input!!")    





