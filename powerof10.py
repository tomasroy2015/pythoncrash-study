n = int(input("Enter input number="))
if(n<=0):
    print("Invalid input")
else:
    while n%10 == 0:
        n = n/10
        print(n)
                
    if(n == 1):
        print("Its a power of 10")
    else:
        print("Not power of 10")
