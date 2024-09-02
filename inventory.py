# Initialize an empty list to hold the products
inventory = []

# Function to display the menu
def display_menu():
    print("\nInventory Management System")
    print("1. Add new product")
    print("2. Remove existing product")
    print("3. Update product quantity")
    print("4. Search for product by name")
    print("5. Display entire inventory")
    print("6. Record a sale")
    print("7. Quit")

# Function to add a new product
def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    threshold = int(input("Enter minimum quantity threshold: "))
    product = {
        'name': name, 
        'category': category, 
        'quantity': quantity, 
        'price': price, 
        'threshold': threshold, 
        'total_sold': 0, 
        'revenue': 0.0
    }
    inventory.append(product)
    print(f"Product {name} added to inventory.")

# Function to remove an existing product
def remove_product():
    name = input("Enter product name to remove: ")
    for product in inventory:
        if product['name'] == name:
            inventory.remove(product)
            print(f"Product {name} removed from inventory.")
            break
    else:
        print(f"Product {name} not found in inventory.")

# Function to update product quantity
def update_quantity():
    name = input("Enter product name to update: ")
    for product in inventory:
        if product['name'] == name:
            new_quantity = int(input("Enter new quantity: "))
            product['quantity'] = new_quantity
            if new_quantity < product['threshold']:
                print(f"Alert: Quantity of {name} is below the threshold of {product['threshold']}.")
            print(f"Product {name} quantity updated to {new_quantity}.")
            break
    else:
        print(f"Product {name} not found in inventory.")

# Function to search for a product by name
def search_product():
    name = input("Enter product name to search: ")
    for product in inventory:
        if product['name'] == name:
            print(f"Found product: {product}")
            break
    else:
        print(f"Product {name} not found in inventory.")

# Function to display the entire inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for product in inventory:
            print(f"Name: {product['name']}, Category: {product['category']}, Quantity: {product['quantity']}, Price: ${product['price']}, Total Sold: {product['total_sold']}, Revenue: ${product['revenue']}")

# Function to record a sale
def record_sale():
    name = input("Enter product name to record a sale: ")
    for product in inventory:
        if product['name'] == name:
            quantity_sold = int(input("Enter quantity sold: "))
            if quantity_sold <= product['quantity']:
                product['quantity'] -= quantity_sold
                revenue_generated = quantity_sold * product['price']
                product['total_sold'] += quantity_sold
                product['revenue'] += revenue_generated
                print(f"Sale recorded: {quantity_sold} units of {name} sold, generating ${revenue_generated} in revenue.")
                if product['quantity'] < product['threshold']:
                    print(f"Alert: Quantity of {name} is below the threshold of {product['threshold']}.")
            else:
                print("Insufficient quantity in stock.")
            break
    else:
        print(f"Product {name} not found in inventory.")

# Main loop to run the program
while True:
    display_menu()
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        update_quantity()
    elif choice == 4:
        search_product()
    elif choice == 5:
        display_inventory()
    elif choice == 6:
        record_sale()
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please choose again.")
