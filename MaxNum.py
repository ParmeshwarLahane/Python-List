# Write a program which accept N numbers from user and store it into list. Return Maximum number from that list.

def listMini(list1):
    MiniNum = list1[0]

    for num in list1:
        if num < MiniNum:
            MiniNum = num
    return MiniNum

def listMax(list1):
    Maxnum = list1[0]

    for num in list1:
        if num > Maxnum:
            Maxnum = num
    return Maxnum

def main():
    print("App is for find Max number from list : ")
    list1 = list()

    print("\nEnter length of list : ")
    lengthlist = int(input())

    print("\nEnter element : ")
    for i in range(lengthlist):
        Element = int(input())
        
        list1.append(Element)

    Max = listMax(list1)
    Mini = listMini(list1)

    print(f"List is : {list1}, \nMaximum number is : {Max}\nMinimum number is : {Mini}")

if __name__=="__main__":
    main()
