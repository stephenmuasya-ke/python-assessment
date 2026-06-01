# pizza_order_cost.py

# Pizza Order Cost Calculator
# This program calculates the total cost of a pizza order
# based on pizza size, toppings, and the  delivery distance.

# Get pizza size from user
pizza_size = input("Enter pizza size (small or large): ").lower()

# Get number of toppings
toppings = int(input("Enter number of toppings: "))

# Get delivery distance
miles = int(input("Enter delivery distance in miles: "))

# Determine pizza base price
if pizza_size == "small":
    base_cost = 8
elif pizza_size == "large":
    base_cost = 12
else:
    print("Invalid pizza size entered.")
    exit()

# Calculate toppings cost
topping_cost = toppings * 1

# Calculate delivery fee
if miles == 0:
    delivery_fee = 0
elif miles <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (miles - 5)

# Calculate total cost
total_cost = base_cost + topping_cost + delivery_fee

# Display order summary
print("\n----- ORDER SUMMARY -----")
print(f"Pizza Size: {pizza_size.capitalize()}")
print(f"Base Cost: ${base_cost:.2f}")
print(f"Toppings Cost: ${topping_cost:.2f}")
print(f"Delivery Fee: ${delivery_fee:.2f}")
print(f"Total Order Cost: ${total_cost:.2f}")