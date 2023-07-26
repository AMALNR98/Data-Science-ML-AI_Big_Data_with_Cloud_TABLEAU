multiplier = int(input("Enter the multiplere : "))
limit = int(input ("Enter the limit : "))
i = 1
product = 0
while limit >= i:
    product = multiplier * i
    print(f"{i} x {multiplier} = {product} ")
    i += 1