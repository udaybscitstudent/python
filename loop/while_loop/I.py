
n = int(input("Enter any number:"))
r=0
while n!=0:
    d = n%10
    r = r*10+d;
    n=n//10
while r!=0:
    d= r%10
    match d:
        case 0:
            print("Zero" ,end=" ")
        case 1:
            print("One" ,end=" ")
        case 2:
            print("Two" ,end=" ")
        case 3:
            print("Three" ,end=" ")
        case 4:
            print("Four" ,end=" ")
        case 5:
            print("Five" ,end=" ")
        case 6:
            print("Six" ,end=" ")
        case 7:
            print("Seven" ,end=" ")
        case 8:
            print("Eight" ,end=" ")
        case 9:
            print("Nine" ,end=" ")
    r = r//10

