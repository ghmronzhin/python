str = input("Please enter a string: ")
i = len(str) - 1
new_string = ""
while i >= 0:
    new_string += str[i]
    i-=1
print(new_string)
