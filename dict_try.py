# Create dictionary
person_info = {
    "name": "Abrar Ahmed",
    "team": "Arsenal",
    "location": "Trier"
}

# Print dictionary
print(person_info)
print("-" * 20)


# Access and print value associated with team
team = person_info["team"]
print(team)
print("-" * 20)

# Change Location
person_info["location"] = "Hasselt"
print(person_info)
print("-" * 20)

# Add new key-pair value
person_info["food"] = "biryani"
print(person_info)
print("-" * 20)

# loop for keys
for i in person_info.keys():
    print(i)
print("-" * 20)    


# loop for values
for j in person_info.values():
    print(j)
print("-" * 20) 

# loop for values
for i,j in person_info.items():
    print(i,j)
print("-" * 20) 