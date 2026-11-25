units = int(input("Enter units consumed: "))

if units <= 200:
    if units <= 100:
        bill = units * 3
    else:
        bill = 100 * 3 + (units - 100) * 5
else:
    if units <= 300:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10

print("Electricity bill = Rs.", bill)