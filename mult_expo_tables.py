
#====== Welcome Section ======#
# Display welcome message and get user input
print("Welcome to my Multiplication/Exponent Table")

#====== Input Section ======#
# Get user name and number with validation
while True:
    user_name = input("Hello, what is your name?: ")
    if user_name.strip():  # Check if message is not empty after removing whitespace
        break
    print("Name cannot be empty. Please try again.")

user_name = user_name.title()

while True:
    try:
        input_number = float(input(f"What number would you like to work with {user_name}?: "))
        break
    except ValueError:
        print("Please enter a valid number")

#====== Multiplication Table Section ======#
# Calculate and display multiplication table for numbers 1-9
# Round results to 4 decimal places
i=1
print(f"Multiplication Table For {input_number}\n")
for i in range (1,10):
    print(f"{i} * {input_number} = {round(input_number * i, 4)}")
        
#====== Exponent Table Section ======#
# Calculate and display exponent table for powers 1-9
# Round results to 4 decimal places
e=1
print(f"\nExponent Table For {input_number}\n")
for e in range (1,10):
    print(f"{input_number} ** {e} = {round(input_number ** e, 4)}")

#====== Message Display Section ======#
# Create and display messages using different string methods
message = f"{user_name}, Math is cool!"
# - Original message
print(message)
# - Lowercase message
print(f"\t{message.lower()}")
# - Title case message
print(f"\t\t{message.title()}")
# - Uppercase message
print(f"\t\t\t{message.upper()}")

print(f"\n\t\t\t\t Thank you for testing my app {user_name.title()}.")