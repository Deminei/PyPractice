# Combine stings and numbers by using th format() method
age = 55
txt = "My name is Bob, and I am {}"
print(txt.format(age))

# format takes unlimited arguments and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item #{} for ${} dollars."
print(myorder.format(quantity, itemno, price))

# Can use index numbers {0} to be sure arguments are placed in
# the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay ${2} dollars for {0} pieces of item #{1}."
print(myorder.format(quantity, itemno, price))

# Use the forward slash(escape character) to allow for double qoutes in a string
txt = "We are the so-called \"Pirates\" from the pacific."
print(txt)
