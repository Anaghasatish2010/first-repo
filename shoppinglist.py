# 7th
class Product:
 def __init__(self, title, quantity):
  self.title = title
  self.quantity = quantity
 def __str__(self):
  return f"Product:\n\tTitle: {self.title}\n\tQuantity: {self.quantity}"
 def change_quantity(self, newQuantity):
        self.quantity = newQuantity
class ShoppingList:
    
    def __init__(self, title):
        self.title = title
        self.items = []
    
    def __str__(self):
        return f"Shopping List:\n\tTitle: {self.title}\n\tNumber of Items:  {len(self.items)}"
   
    def add(self, itemToAdd):
        if isinstance(itemToAdd, Product):
            self.items.append(itemToAdd)
            print("New Item has been added to List")
        else:
            print("Item is not a product")
    
    def show(self):
        print("\n****Shopping List****")
        print(f"Number of items {len(self.items)}")
        for item in self.items:
            print(item.title, item.quantity)