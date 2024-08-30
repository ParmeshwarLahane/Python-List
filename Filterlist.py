# Write a program that contains filter(), map(), and reduce() in it. Python application that contains one list of numbers. The list contains the numbers accepted by the user.
# Filter should filter out all such numbers that are greater than or equal to 70 and less than or equal to 90.
# The map function will increase each number by 10. 
# Reduce will return the product of all that numbers.

from functools import reduce

Special_List = []
Increased_List = []
Originul_list1 = []

list_length = int(input("Enter length of list : "))

#---------------------------------------------------------------------------------------
print("\nEnter list element ")
for i in range(list_length):
    
    Element = int(input())
    Originul_list1.append(Element)
    
# Printing Original list :
print("\nInput list = ",Originul_list1)

#---------------------------------------------------------------------------------------
def max(n):
    return n >= 70 and n <= 90
    # return 70 <= n <= 90

A = list(filter(max, Originul_list1))

# Maxmum number from Originul list :
Special_List.extend(A)
print("\nFiter list = ",Special_List)

#---------------------------------------------------------------------------------------
def Increase(n):
    return n + 10

B = list(map(Increase,Special_List))

# From 70 to 90, this range element list is increased by 10: 
Increased_List.extend(B)
print("\nMap list = ",Increased_List)

#---------------------------------------------------------------------------------------
def prod(n,m):
    return n * m

# Multiplying all elements of increased 10 in the final list:
Final_Result = reduce(prod,Increased_List)
print("\nReduce list = ", Final_Result)

