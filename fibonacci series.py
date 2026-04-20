a = int(input("Enter how many Fibonacci terms: ").replace("\ufeff", "").strip())
b = 0
m = 1

for i in range(a):
    print(b, end=" ")
    d = b + m
    b = m
    m = d

