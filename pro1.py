name = input("Enter your name: ")
age = input("Enter your age: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}")

print("Information saved successfully!")