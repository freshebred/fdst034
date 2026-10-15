import math
i1n = input("Enter name of item 1: ")
i1p = float(input("Enter price for item 1: "))
i1q = int(input("Enter quantity for item 1: "))
sum1 = i1p * i1q

i2n = input("Enter name of item 2: ")
i2p = float(input("Enter price for item 2: "))
i2q = int(input("Enter quantity for item 2: "))
sum2 = i2p * i2q


print("--- Your shopping cart ---")
print(f"{int(i1q)} x {i1n} = ${sum1}")
print(f"{int(i2q)} x {i2n} = ${sum2}")
print(f"Total: ${sum1+sum2}")