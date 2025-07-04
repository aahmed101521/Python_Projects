# Define two sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(f"set1: {set1}")
print(f"set2: {set2}")
print("-" * 20)

# Union 
union_set = set1 | set2 
print(union_set)
print("-" * 20)

# Intersection  
intersect_set = set1 & set2 
print(intersect_set)
print("-" * 20)

# Difference 
difference_set = set1 - set2 
print(difference_set)
print("-" * 20)