person_details = {
    "name": "Narendra Modi",
    "age": 67,
    "salary": 2_00_000,
    "role": "CM of Gujarat",
    "role": "PM of India",  # latest will be stored

}
print(person_details)


print("\nEnumerate keys:")
for each in enumerate(person_details.keys()):
    print(each)

# Enumerate over values
print("\nEnumerate values:")
for each in enumerate(person_details.values()):
    print(each)

# Enumerate over items
print("\nEnumerate over items:")
for key, value in enumerate(person_details.items()):
    print(key, value)
