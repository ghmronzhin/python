nstring = input("enter a number string separated by spaces: ")
nlist = nstring.split(' ')
while len(nlist) > 2:
    num = nlist.pop(3)
    print("value of num: ", num)
    print(nlist)
