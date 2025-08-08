from shoppinglist import ShoppingList,Product

product1 = Product("Broccoli", 1)
print(product1)
product1.change_quantity(3)
print(product1)

product2 = Product("Cauliflower", 2)
product3 = Product("Carrot", 1)

list1 = ShoppingList("Groceries")

print(list1)

list1.add(product1)
list1.add(product2)
list1.add(product3)
list1.show()