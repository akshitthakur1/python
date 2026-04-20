#print all prime numbers in an interval
a = int(input("enter the  number;"))
for i in range(1,a):
    for j in range(2,i):
        if i%j==0:
            print(i)
            break


