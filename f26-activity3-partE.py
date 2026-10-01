# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Stephan Kozak
# Date: 

# SCENARIO
# A group of friends is planning a road trip and wants to estimate the
# driving time and fuel cost. Use these starting values:
# Distance: 650 km
# Average speed: 100 km/h
# Fuel efficiency: 8 L per 100 km
# Fuel price: $1.55 per litre
# Passengers: 3
# Assume constant average speed and fuel efficiency. Ignore stops,
# traffic, taxes, and other vehicle costs.

# TODO 1: Create five variables to store the trip information above.
# Give each variable a meaningful name.
distance_km = 650
average_speed_kmh = 100
fuel_efficiency_l_per_100km = 8
fuel_price_per_litre = 1.55
passengers = 3

# TODO 2: Calculate estimated driving time in HOURS.
# Hint: distance / average speed
driving_time_hours = distance_km / average_speed_kmh

# TODO 3: Calculate the total fuel needed in LITRES.
# Hint: fuel efficiency describes litres used for every 100 km.
fuel_needed_litres = distance_km / 100 * fuel_efficiency_l_per_100km

# TODO 4: Calculate the total fuel cost.
total_fuel_cost = fuel_needed_litres * fuel_price_per_litre

# TODO 5: Use an if/else statement to check that passengers is greater
# than zero before calculating the fuel cost per passenger.
# If passengers is zero or less, print a helpful message instead.
if passengers > 0:
    cost_per_passenger = total_fuel_cost / passengers
else:
    cost_per_passenger = None
    print("Fuel cost per passenger cannot be calculated because passengers must be greater than zero.")
  
# TODO 6: Print a readable trip summary showing:
#   - Estimated driving time (hours)
#   - Total fuel needed (litres)
#   - Total fuel cost (CAD)
#   - Fuel cost per passenger (CAD), when it can be calculated
print("Trip Summary")
print(f"Driving time: {driving_time_hours} hours")
print(f"Fuel needed: {fuel_needed_litres} litres")
print(f"Total fuel cost: ${total_fuel_cost:.2f} CAD")
if cost_per_passenger is not None:
    print(f"Fuel cost per passenger: ${cost_per_passenger:.2f} CAD")
  
# CHECK YOUR WORK
# With the starting values above, expect:
# Driving time: 6.5 hours
# Fuel needed: 52 litres
# Total fuel cost: $80.60
# Fuel cost per passenger: about $26.87
# Test again with zero passengers. Your program should not divide by zero.
