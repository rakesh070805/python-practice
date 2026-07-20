#syntax dictionary_name={"key1":value1,"key2":value2}

student={"name":"rakesh","age":20,"course":"python"}
print(student)

#access value
print(student["name"])
print(student["age"])

# Add a new key-value pair
student["city"] = "Madurai"
print("After adding city:", student)

# Update a value
student["age"] = 22
print("After updating age:", student)

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())

# Display all key-value pairs
print("Items:", student.items())

# Remove a key
student.pop("course")
print("After removing course:", student)
