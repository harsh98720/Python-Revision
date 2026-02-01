n = int(input("Enter a Number :"))

if n <= 1 :
    print("Not prime")

else :
    for i in range(2, n) :
        if n % i == 0:
            print("Not a prime")
            break

    else :
        print("Prime")