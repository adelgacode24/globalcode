


# i=7
# while i < 20:
#     print(i)
#     i=i+1

# i=14
# while i < 20:
#     print(i)
#     i=i+2


# def events():
#     num1=int(input("Enter smaller bumber: "))
#     num2=int(input("Enter bigger  bumber: "))
#     if num1 %2!=0:
#         num1 +=1
#         while num1 < num2 :
#             print(num1)
#             num1=num1+2
           
    
# events()




def reverse_events():
    num1=int(input("Enter smaller number: "))
    num2=int(input("Enter bigger number: "))

    if num2%2 !=0:
        num2 -=1

    while num2 > num1:
        print(num2)
        num2 -=2

reverse_events()
