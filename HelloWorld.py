# Showing Various ways to write Print Statement in Python

# Using Single Quotes:
print('Hello World!')

# Using Double Quotes:
print("Hello World!")

# Using Triple Single Quotes (Single Quotes Inside):
print('''Hello World!''')

# Using Triple Double Quotes (Double Quotes Inside):
print("""This is a double-quoted string with "double quotes" inside.""")

# Mixing Single and Double Quotes:
print('Mixing single and "double" quotes')

# Escaping Quotes:
# You can also escape quotes inside a string using a backslash:
print("Escaping single quote: I\'m happy.")
print('Escaping double quote: She said, "Hello."')

# Printing Special Characters:
# You can print special characters using escape sequences, such as newline (\n), tab (\t), and others:
print("This is a newline.\nThis is a tab:\tTabbed text.")

# Using Variables in Print Statements:
# You can include variables in your print statements by using the f-string feature in Python 3.6 and later:
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Concatenating Strings:
# You can concatenate strings using the + operator:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name: " + full_name)

# Printing Multiple Arguments:
# The print function can take multiple arguments, which it will print with a space by default:
greeting = "Hello"
target = "world"
print(greeting, target)



