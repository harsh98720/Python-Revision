n = 200

for i in range(1, n+1) :
    root = int(i ** 0.5)
    if root * root == i :
        print(i)