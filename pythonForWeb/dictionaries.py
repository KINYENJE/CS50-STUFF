houses = {"Harry": "Gryffindor", "Draco": "Slytherin"} # Create a dictionary with some data

print(f"This is the value for Harry -> {houses['Harry']} ") # Print out the value stored under the "Harry" key

houses["Hermione"] = "Gryffindor" # Add a new key-value pair
print(f"This is the value for Hermione -> {houses['Hermione']} ") # Print out the value stored under the "Hermione" key
# output: This is the value for Hermione -> Gryffindor 

print(houses) # Print out the entire dictionary
# output: {'Harry': 'Gryffindor', 'Draco': 'Slytherin', 'Hermione': 'Gryffindor'}

