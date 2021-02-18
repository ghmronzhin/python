lst = [1, 2, 3, 4, 5, 6, 7]
i = len(lst) - 1
rv = []
print("list: {}".format(lst))
while i >= 0:
    rv.append(lst[i])
    i-=1
print("Reversed list: {}".format(rv))
