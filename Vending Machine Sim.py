cart = []
products = {"M&M":100, "Starburst":150, "RedBull":300}
print("Welcome to Vendino 9000. \n")
print("1. M&M \n 2. Starburst \n 3. RedBull")
inp = input("Pick an option from the ones above (enter 0 to stop): ")
if inp == "1":
    cart.append(products["M&M"])
elif inp == "2":
    cart.append(products["Starburst"])
else:
    cart.append(products["RedBull"])
while inp != "0":
    inp = input("Add more? ")
    if inp == "1":
        cart.append(products["M&M"])
    elif inp == "2":
        cart.append(products["Starburst"])
    else:
        cart.append(products["RedBull"])

    if inp == "0":
        break

#show items in cart
print("Shopping cart: \n")
prodVal = list(products.values())
for a in cart:
    print(prodVal.index[cart[a]])
        
total = 0
for i in cart:
    total += cart[i]

balance = input("Enter the amount your card has: ")
while balance < total:
    print("Not enough balance to purchase. Use a different card.")
    balance = input("Enter new card here:")

balance -= total;
print("Purchase successful. Remaining balance: ", balance)
