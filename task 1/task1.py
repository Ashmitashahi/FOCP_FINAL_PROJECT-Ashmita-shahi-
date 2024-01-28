print("BPP Pizza Price Calculator")
print("==========================")

# Constants
PIZZA_PRICE = 12.00
DELIVERY_COST = 2.50
TUESDAY_DISCOUNT = 0.50
APP_DISCOUNT = 0.25

# positive integer input with error handling
def get_int_input(prompt):
    """Get a positive integer input from the user with error handling."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer!")
            else:
                return value
        except ValueError:
            print("Please enter a number!")

# yes/no input with error handling
def get_yes_no_input(prompt):
    """Get a yes/no input from the user with error handling."""
    while True:
        response = input(prompt).lower()
        if response == 'y' or response == 'n':
            return response
        else:
            print('Please answer "Y" or "N".')


# Inputs
num_pizzas = get_int_input("How many pizzas ordered? ")
delivery_required = get_yes_no_input("Is delivery required? ").lower() == 'y'
is_tuesday = get_yes_no_input("Is it Tuesday? ").lower() == 'y'
used_app = get_yes_no_input("Did the customer use the app? ").lower() == 'y'

# Pizza cost
pizza_cost = num_pizzas * PIZZA_PRICE

# Tuesday discount
if is_tuesday:
    pizza_cost *= (1 - TUESDAY_DISCOUNT)

# Delivery cost
delivery_cost = 0.0
if delivery_required and num_pizzas < 5:
    delivery_cost = DELIVERY_COST

# App discount
total_discount = 0.0
if used_app:
    total_discount = APP_DISCOUNT

# Total price
total_price = (pizza_cost + delivery_cost) * (1 - total_discount)

# Result
print(f"Total Price: £{total_price:.2f}")