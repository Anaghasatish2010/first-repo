from shoppinglist import ShoppingList, Product
print("~~Shopping Cart~~")
userInput = input("Enter the title of your shopping list:")
userShoppingList = ShoppingList(userInput)
done = False
while(not done):
    print("1. Add new Product")
    print("2. Show item list")
    print("3, Change product quantity")
    print("4. Exit application")
    userChoice = int(input("Choose an option:"))
    if userChoice == 1:
        productTitle = input("Enter product name:")
        productQuantity = int(input(f"Please enter quantity of {productTitle}: "))
        newProduct = Product(productTitle, productQuantity)
        userShoppingList.add(newProduct)

    elif userChoice == 2:
        if len(userShoppingList.items) == 0:
            print("Shopping List has no stuff in it!")
        else:
            userShoppingList.show()

    elif userChoice == 3:
        nameOfProduct = input("Enter name of Product whose quantity needs to be changed: ")
        for item in userShoppingList.items:
            if nameOfProduct == item.title:
                newQuantity = int(input(f"Enter {item.title}'s new quantity: "))
                
                item.change_quantity(newQuantity)
                print(f"{item.title}'s quantity has been updated to {item.quantity}")
                break
        else:
            print(f"{nameOfProduct} does not exist in Shopping List")

    elif userChoice == 4:
        print("Exitting Program")
        done = True
    else:
        print("Invalid choice, select from the options!")