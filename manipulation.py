my_string = "Hello, World!"
print(len(my_string))  # Output: 13

my_string = "hello, world!"
print(my_string.upper())  # Output: "HELLO, WORLD!"
my_string = "   Hello, World!   "
print(my_string.strip())  # Output: "Hello, World!"

my_string = "apple,banana,cherry"
print(my_string.split(","))  # Output: ["apple", "banana", "cherry"]

my_list = ["apple", "banana", "cherry"]
print(",".join(my_list))  # Output: "apple,banana,cherry"



my_string = "Hello, World!"
print(my_string.replace("World", "Universe"))  # Output: "Hello, Universe!"


my_string = "Hello, World!"
print(my_string.find("World"))  # Output: 7

my_string = "Hello, World! World!"
print(my_string.count("World"))  # Output: 2



my_string = "Hello, World!"
print(my_string.startswith("Hello"))  # Output: True