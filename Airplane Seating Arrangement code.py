#import statements
import math;
import random;

#checking if it is a prime number
def Isprime(num):
  if num==1:
      return False
  for i in range (2, (int)(math.sqrt(num))+1):
      if(num%i==0):
        return False
  else :
      return True
     
#checking if it is a power of two

def IspowerOf2(n):
  res=math.log(n,2)
  whole=int(res)
  if(res==whole):
    return True
  else :
    return False

#driver program

n=int(input("Enter the number of Matrices : "));
dim=[] #stores number of rows and columns for N matrices in the form of (row,col) tuple
temp=() #stores row and column of ith matrix as (row,col)
Seat=[] #A 3-d array which stores the ultimate result
Prime=[] #list storing prime numbers
Power=[] #list storing Numbers that are  power of 2
Other=[] #list storing the other category numbers
W=[] # list storing the tuple(matrix num,row,col) corresponding to window seat
A=[] # list storing the tuple(matrix num,row,col) corresponding to aisle seat
C=[] # list storing the tuple(matrix num,row,col) corresponding to center seat

#reading the dimensions of n matrices
for i in range(n):
  print("Enter the number of rows in ",i+1," matrix : ",end=" ")
  row=int(input())
  print("Enter the number of columns in ",i+1," matrix : ",end=" ")
  col=int(input())
  temp=(row,col)
  dim.append(temp)
  temp=()

#initialising the Seat list

for i in range(n):
  mat=[]
  Row=dim[i][0]
  Col=dim[i][1]
  for j in range(Row):
    rows=[0]*Col
    mat.append(rows)
  Seat.append(mat)

#reading passenger id's

print("Enter the passenger's id : ",end=" ")
passenger=list(map(int,input().split(' '))) #list storing passenger id's

#separating paseenger id's into prime , power of 2,Other and appending in corresponding  lists

for i in passenger:
  if(Isprime(i)):
    Prime.append(i)
  elif(IspowerOf2(i)):
    Power.append(i)
  else:
    Other.append(i)

#calculating the tuples corresponding to window , aisle and center seats
#The tuple is of form :(Matrix number , Row index , Column index)
for i in range(n):
  #if it is the first matrix then :
  #First column -window
  #middle columns-center
  #last column - aisle
  if(i==0):
    Row=dim[i][0]
    Col=dim[i][1]
    for j in range(Row):
      for k in range(Col): 
        #checking if first column 
        if(k==0):
          temp=(i,j,k)
          W.append(temp)
        #checking if last column
        elif(k==Col-1):
          temp=(i,j,k)
          A.append(temp)
        #else part
        else :
          temp=(i,j,k)
          C.append(temp)

  #if it is the Last matrix then :
  #Last column -window
  #middle columns-center
  #First column - aisle

  elif(i==n-1):
    Row=dim[i][0]
    Col=dim[i][1]
    for j in range(Row):
      for k in range(Col): 
        #checking if first column
        if(k==0):
          temp=(i,j,k)
          A.append(temp)
        #checking if last column
        elif(k==Col-1):
          temp=(i,j,k)
          W.append(temp)
        else :
          temp=(i,j,k)
          C.append(temp)

  #if it is not an extreme matrix then :
  #First column -Aisle
  #middle columns-center
  #last column - aisle
  else :
    Row=dim[i][0]
    Col=dim[i][1]
    for j in range(Row):
      for k in range(Col):
        if(k==0 or k==Col-1):
          temp=(i,j,k)
          A.append(temp)
        else:
          temp=(i,j,k)
          C.append(temp)

#printing the wtuples corresponding to window , aisle , center seats
  
#print("Window : ",W)
#print("Aisle : ",A)
#print("Center : ",C)

#alloting seats

#alloting seats for Prime passenger id's
while(len(Prime)!=0):
    #alloting in Aisle seats
    if(len(A)!=0):
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(A)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      A.remove(temp)
    
    #alloting in Window seats

    elif(len(W)!=0):
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(W)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      W.remove(temp)  

    #alloting in Center seats
    else :
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(C)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      C.remove(temp)

#alloting seats for Power 0f 2 passenger id's

while(len(Power)!=0):
     #alloting in Aisle seats

    if(len(A)!=0):
      passenger_id=random.choice(Power)
      temp=random.choice(A)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Power.remove(passenger_id)
      A.remove(temp)
    
     #alloting in Window seats

    elif(len(W)!=0):
      passenger_id=random.choice(Power)
      temp=random.choice(W)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Power.remove(passenger_id)
      W.remove(temp)

     #alloting in Center seats

    else :
      passenger_id=random.choice(Power)
      temp=random.choice(C)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Power.remove(passenger_id)
      C.remove(temp)

#alloting seats for other passenger id's

while(len(Other)!=0):
    #alloting in Aisle seats
    if(len(A)!=0):

      passenger_id=random.choice(Other)
      temp=random.choice(A)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Other.remove(passenger_id)
      A.remove(temp)

     #alloting in Window seats

    elif(len(W)!=0):
      passenger_id=random.choice(Other)
      temp=random.choice(W)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Other.remove(passenger_id)
      W.remove(temp)  

     #alloting in Center seats

    else :
      passenger_id=random.choice(Other)
      temp=random.choice(C)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Other.remove(passenger_id)
      C.remove(temp)

#printing the seat arrangement

for i in range(n):
  Row=dim[i][0]
  for j in range(Row):
    print(Seat[i][j]) 
  print(' ')


"""
Test Case 1:

Enter the number of Matrices : 4 
Enter the number of rows in  1  matrix :  2
Enter the number of columns in  1  matrix :  3
Enter the number of rows in  2  matrix :  3
Enter the number of columns in  2  matrix :  4
Enter the number of rows in  3  matrix :  3
Enter the number of columns in  3  matrix :  2
Enter the number of rows in  4  matrix :  4
Enter the number of columns in  4  matrix :  3
Enter the passenger's id :  29 59 14 11 3 13 15 18 12 16 6 17 7 47 61 5 21 2 41 9 10 8 19 1 3 4
[12, 0, 7]
[10, 21, 2]
 
[5, 0, 0, 17]
[41, 0, 0, 3]
[11, 0, 0, 19]
 
[15, 4]
[13, 16]
[8, 61]
 
[29, 0, 18]
[1, 0, 14]
[59, 0, 9]
[47, 0, 6]

Test Case 2:

Enter the number of Matrices : 4
Enter the number of rows in  1  matrix :  3
Enter the number of columns in  1  matrix :  2
Enter the number of rows in  2  matrix :  4
Enter the number of columns in  2  matrix :  3
Enter the number of rows in  3  matrix :  2
Enter the number of columns in  3  matrix :  3
Enter the number of rows in  4  matrix :  3
Enter the number of columns in  4  matrix :  4
Enter the passenger's id :  29 59 14 11 3 13 15 18 12 16 17 6 7 47 61 5 21 2 41 9 10 8 19 1 4
[6, 41]
[21, 4]
[14, 61]
 
[29, 0, 19]
[3, 0, 1]
[8, 0, 9]
[11, 0, 17]
 
[7, 0, 2]
[59, 0, 13]
 
[5, 12, 0, 15]
[16, 0, 0, 10]
[47, 0, 0, 18]
 
Test Case 3:

Enter the number of Matrices : 3
Enter the number of rows in  1  matrix :  2
Enter the number of columns in  1  matrix :  3
Enter the number of rows in  2  matrix :  3
Enter the number of columns in  2  matrix :  4
Enter the number of rows in  3  matrix :  3
Enter the number of columns in  3  matrix :  2
Enter the passenger's id :  29 59 14 17 16 12 15 7 3 5 19 21 33 44 19
[44, 0, 3]
[21, 0, 19]
 
[7, 0, 0, 19]
[33, 0, 0, 29]
[59, 0, 0, 17]
 
[5, 14]
[12, 15]
[16, 0]
 
Test Case 4: 

Enter the number of Matrices : 5
Enter the number of rows in  1  matrix :  2
Enter the number of columns in  1  matrix :  3
Enter the number of rows in  2  matrix :  4
Enter the number of columns in  2  matrix :  3
Enter the number of rows in  3  matrix :  2
Enter the number of columns in  3  matrix :  4
Enter the number of rows in  4  matrix :  2
Enter the number of columns in  4  matrix :  2
Enter the number of rows in  5  matrix :  4
Enter the number of columns in  5  matrix :  3
Enter the passenger's id :  2 67 54 3 11 17 18 29 39 51 64 17 35 7 11 9 8 16 41 14 15 19 20 22 37 59 77 55 13 78 47
[39, 0, 19]
[77, 0, 51]
 
[2, 0, 59]
[41, 0, 16]
[78, 0, 8]
[37, 0, 9]
 
[54, 15, 0, 67]
[11, 0, 0, 11]
 
[13, 3]
[55, 64]
 
[29, 0, 22]
[7, 0, 20]
[47, 0, 18]
[17, 0, 14]
 

Test Case 5:

Enter the number of Matrices : 2
Enter the number of rows in  1  matrix :  3
Enter the number of columns in  1  matrix :  3
Enter the number of rows in  2  matrix :  2
Enter the number of columns in  2  matrix :  2
Enter the passenger's id :  11 17 15 17 8 6 9 2 59 60
[15, 0, 8]
[9, 0, 17]
[60, 0, 59]
 
[2, 6]
[11, 0]
"""
