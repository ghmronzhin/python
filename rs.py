str = input("Please enter a string to reverse: ")
i = len(str) - 1
new_str = ""
while (i >= 0):
    new_str+=str[i]
    i-=1
print(new_str)
