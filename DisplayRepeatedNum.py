# Write a program which accept N number from user and store it into list. 
# Accept one another number from user and return frequency of that number from list

# This function checks the count of repeated numbers in list1 then return list length and list2. it takes two arguments, ChkNum and list1.
def count(ChkNum,list1):
    list2 = []
    for i in list1:
        if ChkNum == i:
            list2.append(i)
            
    return f"repeated {len(list2)} time, \n\nCheck it : {list2}"

# This function creates list according to length number, so it takes one argument and returns the list.
def create(listlen):
    list1 = []
    for i in range(listlen):
        Element = int(input("\nEnter element : "))
        list1.append(Element)
    
    return list1

# This is display or print function 
def main():   
    
    listlen = int(input("\nEnter length of list : "))
    list1 = create(listlen)
    
    ChkNum = int(input("\nCheck friquncy of number : "))
    
    print(f"\nlist1 : {list1}") 
    Ans = count(ChkNum,list1)
    print(f"\n{ChkNum} {Ans}")    
    
if __name__=="__main__":
    main()