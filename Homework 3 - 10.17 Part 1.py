#Pranav Tetali
#ID 1541822
#Homework 3 10.17

class ItemToPurchase:
    # EX #1
    def __init__(self):
        # variables
        # given values
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

        #items
    def print_item_cost(self):
        #It should display the item name, quantity and price in that order
        print(self.item_name + " " + str(self.item_quantity) + " @ $"
              + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity ))

if __name__ == "__main__":
    # Ex #2
    # This is the main function
    # It should print the item1 depending on item given
    print("Item 1")
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    # it should prompt and read the item1 details from the user
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print("\nItem 2")
    # it should prompt the user and read the item2 details from the user
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print("\nTOTAL COST")
    # Ex #3
    item1.print_item_cost()
    item2.print_item_cost()
    # it should add up the cost of items
    total = (item1.item_price*item1.item_quantity)+(item2.item_price * item2.item_quantity)
    # it should display the total cost at the bottom
    print("\nTotal: $" + str(total))
