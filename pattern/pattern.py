for i in range(5,0,-1):
    print("student",i)
    
    for j in range(5,i-1,-1):
        # if j <= i:
        print("check subject",j)
print()    
####################################################
for n in range(1,10):
 for i in range(1,11):
  print(n*i)
 print(" ") 
 ###############################################
for i in range(1,5):
  for j in range(1,i+1):
   print("#",end=" ")
  print() 
##################################################
for i in range(1,5):
    for j in range(5-i):
        print("#",end=" ")
    print()    
#########################################################
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("#",end=" ")    
    print(" ")    
#################################################3
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("#",end=" ")    
    print(" ")  
    n=4  
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(n+1-i):
        print("#",end=" ")
    print()        
#####################################################
for i in range(4):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print(" ")   
####################################################
temp =65
for i in range(4):
    for j in range(i+1):
     print(chr(temp),end=" ")
     temp+=1
    print()
##########################################
for i in range(5,0,-1):
    print("student ",i)
    for j in range(5,i-1,-1):
        print("subject ",j)
    print()    
##################################################
for i in range(5,11):
    for j in range(1,11):
        print(i*j)
    print()    
######################################################
for n in range(1,17+1):
    count=0
    for i in range(1,n+1):
        if n%i==0:
         count+=1
    if count ==2:
        print("prime",n)
    else:
        print("not prime",n)        
#######################################################
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")         
    print()    
######################################
n=5
for i in range(0,n):
    for j in range(0,n):
        if j<=i:
            print("*",end=" ")
    print()  
##############################################    
n=5
for i in range(0,n):
    for j in range(0,n):
        if i<=j:
            print("*",end=" ")
    print()  
#########################################    
n=5
for i in range(0,5):
    for j in range(4,0,-1):
        if j<=i:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()          
###################################################
n=5
for i in range(4,0,-1):
    for j in range(4,0,-1):
        if j<=i:
            print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()   
########################################         
n=5
for i in range(0,n):
    for j in range(0,n):
       if j<=i:
           print("*",end=" ")
    print()  
########################################  
n=5
for i in range(n,0,-1):
    for j in range(0,n):
        if j<=i:
            print("*",end=" ") 
        else:
            print( )
    print()        

