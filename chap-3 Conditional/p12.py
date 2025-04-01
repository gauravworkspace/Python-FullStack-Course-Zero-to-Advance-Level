# Python program to calculate electricity bill based on usage

# Billing Criteria:
# First 100 units: ₹5 per unit
# Next 200 units (101-300): ₹7 per unit
# Above 300 units: ₹10 per unit

num_units = int(input("Enter the number of units consumed: "))
bill = 0  # Initialize bill amount

if num_units <= 100:
    bill = num_units * 5  # First 100 units at ₹5 per unit
elif num_units <= 300:
    bill = (100 * 5) + (num_units - 100) * 7  # Next 200 units at ₹7 per unit
else:
    bill = (100 * 5) + (200 * 7) + (num_units - 300) * 10  # Above 300 units at ₹10 per unit

# Display the final bill amount
print(f"Electricity bill is ₹{bill}")
