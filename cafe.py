#Creates a list for the menu
menu = ["coffee", "tea", "cake", "sandwich", "spaghetti", "pizza slice"]

#Creates a dictionary storing the number of items in stock for each item
stock = {"coffee": 10,
         "tea": 12,
         "cake": 5,
         "sandwich": 7,
         "pizza slice": 3}

#Creates a dictionary for the cost of each item
price = {"coffee": 3,
         "tea": 2.50,
         "cake": 3.50,
         "sandwich": 4,
         "pizza slice": 5}

#Creates the variable to store the total stock in
total_stock = 0

#For each item in the menu list, check if it is in the stock and price dictionaries
#If it is found, use the item as the key to access the value in both dictionaries
#Multiply the values together to find each item's current stock value, then print it and add to the total
for i in menu:
    if i in stock and price:
        item_value = stock[i] * price[i]
        print(f"Current {i}'s value is £{item_value}")
        total_stock += item_value
#If an item on the menu isn't found in the dictionaries, print a message to tell the user it wasn't found (spaghetti is my example for this!)
    else:
        print(f"{i.upper()} was not found in stock.")

#Prints out the total stock value of all items in the shop.
print(f"Total stock value is worth £{total_stock}")