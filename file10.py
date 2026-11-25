n = int(input("Enter a two-digit number: "))

tens = n // 10
ones = n % 10
total = tens + ones

print("Tens digit :", tens)
print("Ones digit :", ones)
print("Sum of digits =", total)