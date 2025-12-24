new_list=[]
print(type(new_list))
#################################
new_list=[1,2,3]
print(new_list)
################################
new_list=['aman',123,'a',82]
print(new_list[3])
########################################
li=[1,2,3,4,5,6]
print(li[1:6:2])
############################
li=[1,2,3,4,5,6,]
print(li[-6::2])
#####################################
li=[1,2,3,4,5,6,]
print(li[::-1])
###############################
li=[10,20,30,40,50]
print(li)
li[2] =80
print(li[2])
print(li)
#######################################
li = [1,2,3,4,5]
for i in li:
    print(i)
##################################
for i in range(len(li)):
    print(li[i])
#####################################
li1 = [1,2,3,4]
for i in range(len(li1)):
    li1[i] = li1[i]**2
print(li1)
######################################
l1 = [1,2,3,4]
for i in range(len(l1)):
    l1[i] = l1[i] + 2
print(l1)
######################################
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
for i in range(len(l1)):
    l1[i] = l1[i] + l2[i]
print(l1)
#########################################
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
for i in range(len(l1)):
    l1[i] = l1[i] + l2[-(i+1)]
print(l1)
#####################################
l1 = [1,2,5,3,4,3]
max_ele = 0
sec = 0
for i in range(len(l1)):
#####################################    
    if max_ele < l1[i]:
        sec = max_ele
        max_ele = l1[i]
print("largest :- ",max_ele)
print("second :- ",sec)
#################################
min_ele = max_ele
for i in range(len(l1)):
    if l1[i] < min_ele:
        min_ele = l1[i]
print("smallest :- ",min_ele)
########################################
li=[10,3,4,8]
first_largest=0
second_largest=0
for num in li:
    if num>first_largest:
        second_largest=first_largest
        first_largest=num
    elif num >second_largest:
        second_largest =num
print(first_largest)
print(second_largest)
#########################################
l1=[1,2,3,4,5]
left=0
right=len(l1)-1
while left < right:
    l1[left],l1[right] = l1[right],l1[left]
    right -=1
    left +=1
print(l1) 
#####################################
# append method is used to add the element at least of the list
li=[1,2]
li.append(3)
print(li)
######################################################
#  first list -> squre of the elements -> odd idx
#  second list -> cube of all the elements -> even idx
li=[1,2,3,4,5,6,7,8,9,]
first_list=[]
second_list=[]
for i in range(len(li)):
    if i%2==0:
        first_list.append(li[i] ** 2)
    else:
        second_list.append(li[i] **3)
print(first_list)            
print(second_list)
####################################################
# find the lenght of the list without using the len function
li=[1,2,3,4,5,6]
count=0
for i in li:
    count+=1
print(count)    
############################################
# print common element 
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
         print(l1[i])   
#########################################
# palindrome of the given element
l1=[1,2,2,1]
is_palindrome=True
for i in range(len(l1)):
    if l1[i] !=l1[-(i+1)]:

#############################################
# find polindrome in the given string value
li=['aman','naman','ram']  
for word in li:
    if word ==word[::-1]   :
        print(word)   

# append,extend,insert,pop

# .append()->method is used to add only one element at the last of the list
######################################################################
li=[1,2,3,4,5,6,7,8,9,10]
even_num=[]
odd_num=[]
for num in li:
    if num%2==0:
        even_num.append(num)
    else:
        odd_num.append(num)  
print(even_num)         
print(odd_num) 
####################################################3
# .extend -> extend method is used to extend the list by adding the multiple element at a time

# .index()-> insart method is used to insert the element at a particullar index
li=[1,2,3,4,5,6]
print(li)
li.insert(1,100)
print(li)
# .pop()  -> pop method is used to remove the element from the list by giving the particullar index and return that value
# by defult index is last index of the last -1
# it means it remove the kast elemnt form the list and return it
sum=0
li=[1,2,3,4]
while len(li) !=0:
    element=li.pop()
    sum += element
print(li)
print(sum)    
###########################################
# sorted() -> the sorted method is use to sort tge list it return the sorted list,
li=[1,2,1,5,6]
is_sorted=True
for i in range(len(li)-1):
    if li[i]>li[i+1]:
        is_sorted=False
if is_sorted:
    print("sorted")
else:
    print("not sorted")   
######################################3
li=[1,2,3,4]
k=3
for i in li:
    if k == li[i]:
        print([i])
        break
    else:
        print("not exits")
###################################################
n=int(input('enter the no of element sum -:'))
li=[]
while n != 0:
    n=int(input('enter num :'))
    li.append(n)
    n-=1
print(sum(li))
######################################################
# map(int,a)-> to change value in intiger 
li=list(map(int,input("enter a list of number :").split()))
print(li)
sum=0
for i in range(len(li)):
    sum += li[i]
print(sum)    
########################################
li=[1,2,3,4,5,6,7]
print(li[0],li[-1])
############################################
li=[1,2,3,4,5,6,7]
sum=0
for i in range(len(li)):
    sum+=li[i]
print(sum)    
#################################################
li=[1,2,3,4] 
target=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
       if li[i]+li[j]==target:
        print(i,j)
        break    
############################################
li=['this ','is','a','sentence']
max =li[0]
for i in li:
    if len(max)<len(i):
        max =len(i)
        print(max,i)
##############################################
li=[1,2,3,4]
prod=1
for num in li:
    prod *= num
for i in range(len(li)):
    li[i]= prod //li[i]    
print(li)          
##################################################
li=[1,2,3,4,5,6,7,8,9,10]
even_num=[]
odd_num=[]
for i in li:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)    
print(even_num)     
print(odd_num)   
######################################
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            print(l1[i])            
##############################################
# sorted  list
li=[1,2,3,5] # 11
# [1,2,3,4,5]=45 -> 15-11=4
sum=0
for i in range(1,5+1):
    sum+=i
li_sum=0    
for num in li:
    li_sum+=num
missing=sum-li_sum
print(missing)    

#########################################
# remove duplicate number from the list
[1,2,2,3,4]
li=[1,2,2,3,4]
unique_li=[]
for num in li:
 if num not in unique_li:
###################################

#######################################################
# sum of all the element
sum=0
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in li:
    for j in i:
     sum+=j
print(sum)      
#########################################
# flat the 2D list into 1D list
flatten_li=[]
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    flatten_li.extend(li[i])
print(flatten_li)   
#################################################
# reverse each row of the matrix or 2d list
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    li[i] =li[i][::-1]
print(li)    
################################################
li=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in li:
    for j in i:
        if j%2==0:
         print(j)
         sum+=j
print("the sum  of the even number",sum)        
#############################################################
# change the row of list into coloum 
li=[[1,2,3],[4,5,6],[7,8,9]]
transpose_mat=[]
for i in range(len(li)):
    row=[]
    for j in range(len(li[i])):
        row.append(li[j][i])
    transpose_mat.append(row) 
print(transpose_mat)




            






 


































