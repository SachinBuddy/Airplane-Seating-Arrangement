import math;
import random;

#checking if it is a prime number
def Isprime( n,factor):
  if n==2:
    return True
  elif(factor>(n/2)):
    return True
  elif(n%factor==0):
    return False
  else :
    return Isprime(n,factor+1)

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
dim=[] #stores number of rows and columns for N matrices in the form og (row,col) tuple
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
  if(Isprime(i,2)):
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
  
print("Window : ",W)
print("Aisle : ",A)
print("Center : ",C)

#alloting seats

#alloting seats for Prime passenger id's
while(len(Prime)!=0):
    #alloting in aisle seats
    if(len(A)!=0):
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(A)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      A.remove(temp)
    
    #alloting in window seats

    elif(len(W)!=0):
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(W)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      W.remove(temp)  

    #alloting in center seats
    else :
      #choosing id's and seats randomly
      passenger_id=random.choice(Prime)
      temp=random.choice(C)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Prime.remove(passenger_id)
      C.remove(temp)

#alloting seats for Power 0f 2 passenger id's

while(len(Power)!=0):
     #alloting in aisle seats

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

     #alloting in center seats

    else :
      passenger_id=random.choice(Power)
      temp=random.choice(C)
      Seat[temp[0]][temp[1]][temp[2]]=passenger_id
      Power.remove(passenger_id)
      C.remove(temp)

#alloting seats for other passenger id's

while(len(Other)!=0):
    #alloting in aisle seats
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

     #alloting in center seats

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
  print('\t')
