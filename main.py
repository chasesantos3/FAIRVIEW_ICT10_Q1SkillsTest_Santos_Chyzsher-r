print("Chicken Wings Ordering System")
print("\nMenu:")
print("1. Original Wings - ₱150")
print("2. Spicy Wings - ₱170")
print("3. Honey Garlic Wings - ₱180")

order_total = 0

order = input("\nEnter your chosen wings (1/2/3 or multiple separated by comma): ")

if "1" in order:
    order_total += 150
if "2" in order:
    order_total += 170
if "3" in order:
    order_total += 180

print("\nSauce Options:")
print("1. None - ₱0")
print("2. Buffalo - ₱20")
print("3. BBQ - ₱25")
print("4. Sweet Chili - ₱22")

sauce = input("Choose sauce (1-4): ")
if sauce == "2":
    order_total += 20
elif sauce == "3":
    order_total += 25
elif sauce == "4":
    order_total += 22

print("\nDrinks:")
print("1. Coke - ₱40")
print("2. Iced Tea - ₱50")
print("3. Lemonade - ₱55")

drink = input("Choose drink (1/2/3 or multiple separated by comma): ")

if "1" in drink:
    order_total += 40
if "2" in drink:
    order_total += 50
if "3" in drink:
    order_total += 55

print("\nCustomer Information:")
name = input("Name: ")
address = input("Address: ")
contact = input("Contact Number: ")

print("\nOrder Summary:")
print("Customer Name:", name)
print("Address:", address)
print("Contact Number:", contact)
print("Total Amount: ₱", order_total)
