
#libaries:

import random



#Q)1
############################################################################################################
#Problem
"""
Write a Python program to converting an integer to a string in any base.
Sample Solution.

Example:
let take (255)10 with base decimal and we are  convert to (11111111)2 with base binary. 
"""

#code
def to_convert_base(Num, base):

    
    List_base="0123456789ABCDEF"
    
    if Num<base:
        
        return List_base[Num]
    
    else:

        return to_convert_base(Num//base,base) + List_base[Num%base]
    

#output:
print(to_convert_base(255,2))
print(to_convert_base(255,10))
print(to_convert_base(255,16))

r1=random.randrange(0,255),random.randrange(2,16)
print("The number is:",r1[0],"and the base is:",r1[1],"the result after convert-->",to_convert_base(r1[0],r1[1])) 

############################################################################################################

print("#"*30)

#Q)2
############################################################################################################
#Problem
"""
Write a Python program to solve the Fibonacci sequence using recursion.
Sample Solution:


Example:
let take 11 , and we are need get the Fibonacci for 11 with use Dp
[0]  0
[0, 1]  1
[0, 1, 1]  2
[0, 1, 1, 2]  3
[0, 1, 1, 2, 3]  4
[0, 1, 1, 2, 3, 5]  5
[0, 1, 1, 2, 3, 5, 8]  6
[0, 1, 1, 2, 3, 5, 8, 13] 7
[0, 1, 1, 2, 3, 5, 8, 13, 21] 8
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 9
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89] 11
"""
#code

F=[-1]*500

def to_get_Fibonacci(Num):

    
    
    if F[Num]<0:

        if(Num==0):
            F[Num] = 0

        elif (Num==1):
            F[Num]=1
        
        else:
            F[Num]= to_get_Fibonacci(Num-1) + to_get_Fibonacci(Num-2)
    
    return F[Num]
    

#output:
for i in range(12):

    print("The number of ",i,",The Fibonacci:",to_get_Fibonacci(i),",The DpList",F[:i+1])
############################################################################################################


print("#"*30)

#Q)3
############################################################################################################
#Problem
"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). // use recursion 
Sample Solution:

Example:
let take 15 , and we are need get sum series for 15.

"""

#code
def to_get_sumSer(Num):


    if Num<1:
        return 0 
    else:
        return Num + to_get_sumSer(Num-2)



#output:
print("The Number is ",6,"The sum of Series : ",to_get_sumSer(6)) # 6 4 2 0 , sum = 12
print("The Number is ",10,"The sum of Series: ",to_get_sumSer(10)) # 10 8 6 4 2 0 , sum = 30
print("The Number is ",15,"The sum of Series: ",to_get_sumSer(15)) # 15 13 11 9 7 5 3 1  , sum = 64

r= random.randrange(0,1000)
print("The Number is ",r,"The sum of Series: ",to_get_sumSer(r)) 
############################################################################################################



print("#"*30)

#Q)4
############################################################################################################
#Problem
"""
Write a Python program to calculate the value of 'a' to the power 'b'.
Example:
let take a=2 , b=4 , then z= a**b ==> 16
"""
#code
def to_get_pow(a,b):

    if b==1:
        return a
    
    elif b==0:

        return 1
    
    elif a==1:

        return 1
    
    else:
        return a*to_get_pow(a, b-1)



#output:
print("a= ",3,"b= ",4,"a= a**b= ",to_get_pow(3,4))
print("a= ",2,"b= ",4,"a= a**b= ",to_get_pow(2,4))

r= random.randrange(0,10),random.randrange(0,10)
print("a= ",r[0],"b= ",r[1],", z= a**b= ",to_get_pow(r[0],r[1]))
############################################################################################################





print("#"*30)

#Q)5
############################################################################################################
#Problem
"""
Write a Python program to find out its proper divisors
Example:
let take n= 12 , then [1, 2, 3, 4, 6] are divisors by 12
"""
#code
def to_get_DivBy(Num):

    LK=[]
    i=1
    while(i<Num):

        if Num%i==0:
            LK.append(i)
        
        i+=1
    
    return LK

        
    

#output:
print(to_get_DivBy(12))
r= random.randrange(0,100)
print("The divisors by",r,"Are:==>",to_get_DivBy(r))
############################################################################################################





print("#"*30)

#Q)6
############################################################################################################
#Problem
"""
Write a Python program to multiply two integers without using the * operator in python.
Sample Solution:-

Example:
let take a= 4 , b = 3 , then z= a*b==> 12
"""
#code
def to_get_Mul(a,b):

    if (b<0):

        return -to_get_Mul(a,-b)

    if (b==0):
        return 0
    
    elif (b==1):
        return a
    
    else:
        return a + to_get_Mul(a,b-1)
    

        
    

#output:
print(to_get_Mul(3,4))
print(to_get_Mul(3,-4))
print(to_get_Mul(-3,4))
print(to_get_Mul(-3,-4))

r= random.randrange(-100,100),random.randrange(-100,100)
print("a= ",r[0],"b= ",r[1],", z= a*b= ",to_get_Mul(r[0],r[1]))
############################################################################################################





print("#"*30)

#Q)7
############################################################################################################
#Problem
"""
Python program to display the given integer in reverse manner

Example:
let take a= 411 ,  then a reverse manner for 411 ==>114
"""

#code
def to_get_Rmanner(Num):

    SL=""

    while(Num!=0):
        Div = Num%10
        SL+=str(Div)

        Num//=10

    return SL

    
        
    

#output:

print(to_get_Rmanner(411))

r= random.randrange(0,100)
print("The Number:",r," reverse manner:==>",to_get_Rmanner(r))
############################################################################################################




print("#"*30)

#Q)8
############################################################################################################
#Problem
"""
Python program to find the sum of the digits of an integer using while loop

Example:
let take a= 564 ,  then a Sum digit of 564 ==> 5+6+4 = 15
"""

#code
def to_get_SumDigit(Num):


    sum=0
    while(Num!=0):
        Div = Num%10
        sum += Div

        Num//=10

    return sum

    
        
    

#output:

print(to_get_SumDigit(564))

r= random.randrange(0,100)
print("The Number:",r," reverse manner:==>",to_get_SumDigit(r))
############################################################################################################





print("#"*30)

#Q)9
############################################################################################################
#Problem
"""
Write a program in python as a function that determines the intersection of two sets without using any predefined functions.
Example:
let take S= {"HTML", "CSS", "JavaScript", "C++"} ,  S2={"JavaScript","Python", "Java","C++", "PHP"}

then S3 = {"C++", "JavaScript"}
"""

#code
def to_get_Cross(S1, S2):

    S3= set()
    
    m= max(len(S1),len(S3))

    if m==len(S1):
        SJ=S1
        SK=S2
    if m==len(S2):
        SJ=S2
        SK=S1

    for ele in SJ:

        if ele in SK:

            S3.add(ele)
    
    return S3




#output:
E = {"HTML", "CSS", "JavaScript", "C++"}
F = {"JavaScript","Python", "Java","C++", "PHP"}
print("The intersection of E and F is : " , to_get_Cross(E , F))

############################################################################################################




print("#"*30)

#Q)10
############################################################################################################
#Problem
"""
Write a python algorithm to remove duplicate elements from a list.
Solution
Example:
let take Array= [1,1,1,1,2,3,4,5,5,6,7] 

then ArrayDip = [1,2,3,4,5,6,7] 
"""

#code
def to_get_removeDuplicate(L):

    
    RL= []

    for ele in L:

        if ele not in RL:

            RL.append(ele)

        
    
    return RL
    
    


    
    




#output:
L = [11 , 3 , 11, 3 , 4 , 11 , 7 , 3 , 11]
print(to_get_removeDuplicate(L))

Lr= [random.randint(i,10)  for i in range(10)]
print(Lr)
print(to_get_removeDuplicate(Lr))
############################################################################################################



print("#"*30)

#Q)11
############################################################################################################
#Problem
"""

Write a python algorithm to remove duplicate elements from a list.
Solution
Example:
let take S= {2, 4, 5, 6} ,  S2={4, 6, 7, 8}


then S3 = {2, 4 , 5, 6, 7, 8}
"""

#code

def to_get_union(S1,S2):

    
    LS = { i for i in list(S1) + list(S2)}

    UList = {ele for ele in LS}

    return UList



#output:
set1 = {2, 4, 5, 6} 
set2 = {4, 6, 7, 8}
print(to_get_union(set1,set2))

Set1= {random.randint(i,10)  for i in range(10)}
Set2= {random.randint(i,10)  for i in range(10)}
print("Set1:",Set1,", Set2:",Set2,"Union:--->",to_get_union(Set1,Set2))
#############################################################################################################


