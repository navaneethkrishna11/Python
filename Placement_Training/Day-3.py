"""
Read and Print a Matrix
"""
n=int(input("enter the row : "))
m=int(input("enter the col : "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        a=int(input("enter the element :"))
        row.append(a)
    matrix.append(row)

for i in range(n):
    for j in range(m):
      print(matrix[i][j],end=" ")
    print()
  """
  Guess a number between a limit of random numbers.
  """
import random as rd

lower=int(input("enter the lower limit : "))
upper=int(input("enter the upper limit :  "))
count = 0
state=True

b=rd.randint(lower,upper)
while state:
    a = int(input("enter a guess : "))
    count +=1
    if a == b:
        print("You Guessed it right")
        state=False
    elif a<b :
     print('High')
     count=count+1

    elif a>b :
     print('Low')
     count=count+1

print("Total number of guess : ",count)
"""
Matrix Addition
"""
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Enter number for matrix1[{i}][{j}]: "))
        row.append(a)
    matrix.append(row)

matrix2 = []
for i in range(m):
    row1 = []
    for j in range(n):
        a = int(input(f"Enter number for matrix2[{i}][{j}]: "))
        row1.append(a)
    matrix2.append(row1)

sum_matrix = []
for i in range(m):
    row2 = []
    for j in range(n):
        row2.append(matrix[i][j] + matrix2[i][j])
    sum_matrix.append(row2)

print("Sum matrix is:")
for i in range(m):
    for j in range(n):
        print(sum_matrix[i][j], end=" ")
    print()

"""
Frequency of a string
"""
st=input("enter the string :  ")
char={}
for i in st:
    if i in char:
        char[i]+=1
    else:
        char[i]=1
for i,f in char.items():
    print(i ,":", f)
"""
Sort on basis of Rank
"""
n=int(input("enter the lmit : "))
rank=[]
count=0
for i in range(n):
    a=int(input("enter the elements : "))
    rank.append(a)
b=rank[0]
for i in range(n):
    if rank[i]<b:
        count=count+1
        b=rank[i]

print(count)


