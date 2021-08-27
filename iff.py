# a = input("enter a number to check")
# if int(a) > 0:
#     print("entered statement is positive")
#     if int(a)>10:
#         print("entered number is greater than 10")
#     elif int(a)<5 :
#         print("entere number is less than 5")
#     else:
#         print("entered number is between 5 and 10")
# else:
#     print("entered statement is negative")

menu={1:"pahti",2:"chicken",3:"curry v",4:"choee",5:"nood",6:"meen"}
a=input("do you want to see the menu(y/n)")
if a=='y':
    print(menu)
    choice=int(input("enter a choice"))
    if (choice>0)or(choice<=6):
        print("you selected "+menu[choice])
    else:
        print("invalid choice")
elif a=='n':
    print("thank you for visiting")
else:
    print("invalid request")
