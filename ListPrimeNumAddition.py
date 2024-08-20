# Write a program which accepts N number from user and stores it in a list.
# Return addition of all prime number from that list.
# Main python file accept N number from user and passes each number to ChkPrime() function, 
# which is part of our user-defined module named as xyz.
# Name of the function in main Python file should be ListPrime()

def ChkPrime(num):     # ChkPrime function is to check whether the number is prime or not.
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,int(num**0.5) + 1,2):
        if num % i == 0:
            return False
    return True

def Primelist(number):     # The purpose of Primelist is to accept prime numbers and store them in a list.
    list1 = []
    for num in number:
        if ChkPrime(num):
            list1.append(num)
    return list1

def AddPrime(list1):       # The AddPrime function gets numbers one by one from the prime number list and adds it to the Addition variable.
    Addition = 0
    for i in list1:
        Addition += i
    return Addition

def Createlist(listlen):     # The “createlist” function gets the length of the list from the user and then accept the elements from the user according to the length as well. then store that element in "number list"
    number = []
    for i in range(listlen):
        Element = int(input("Enter Element : "))
        number.append(Element)
    return number

def main():        # This main function accepts the input from the user and sends it to the respective function and then accepts the processed data and displays the output on the screen
    listlen = int(input("Enter the your list length : "))
    number = Createlist(listlen)
    
    list1  = Primelist(number)
    
    Addition = AddPrime(list1)
    
    print(f"Main list : {number},\nPrime number list : {list1},\nAddition of Prime number {Addition}")
    
if __name__=="__main__":    # Program starter
    main()       # main function calling