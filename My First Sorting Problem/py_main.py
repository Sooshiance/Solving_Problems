n = int(input("Enter the number of test case : "))

l = []


for i in range(n):
    t = []

    a, b = input("Enter Two values : ").split()

    a = int(a)
    b = int(b)

    if a > b:
        t.append(b)
        t.append(a)
    else:
        t.append(a)
        t.append(b)
    
    l.append(t)


x = enumerate(l)


for i, j in x:
    print(j[0], " ", j[1])
