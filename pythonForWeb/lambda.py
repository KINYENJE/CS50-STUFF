people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]

def f(person):
  return person["name"]

people.sort(key=f)

print(people) # output: [{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]



# or we can use lambda function to sort the list of dictionaries
people.sort(key=lambda person: person["house"]) # sort the list of dictionaries based on the value of the key "house"

print(people) # output: [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}]
