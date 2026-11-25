n = int(input("Enter an integer: "))
n = abs(n)

count = 0
if n == 0:
    count = 1
while n > 0:
    count += 1
    n //= 10

print("Number of digits =", count)