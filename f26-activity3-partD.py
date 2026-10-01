# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Stephan Kozak
# Date: September 30, 2026

# SCENARIO
# Calculate SIMPLE interest on an investment. This exercise does not use
# compound interest, powers, or square roots.
# Formula: interest = principal * rate * time
# Start with:
# Principal (starting investment): $1,000.00
# Annual interest rate: 5% (store this as 0.05)
# Time: 3 years

# TODO 1: Create variables for the principal, annual interest rate, and time.
principal = 1000.00
rate = 0.05
time = 3

# TODO 2: Calculate the interest earned using the formula above.
interest = principal * rate * time

# TODO 3: Calculate the final investment value (principal + interest).
final_value = principal + interest

# TODO 4: Print the starting investment, interest earned, and final value.
# Optional: Format money to two decimal places.
print(f"Starting investment: ${principal:,.2f}")
print(f"Interest earned: ${interest:,.2f}")
print(f"Final value: ${final_value:,.2f}")

# CHECK YOUR WORK
# Interest earned: $150.00
# Final value: $1,150.00
