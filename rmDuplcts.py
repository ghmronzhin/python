lst = [4, 1, 4, 4, 4, 5, 6, 7, 5, 7, 12]
lst.sort()
print(lst)
ndlst = []
for number in lst:
    if number not in ndlst:
        ndlst.append(number)
print(ndlst)
