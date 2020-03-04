#items = ["apple", "pear", "orange", "banana", "apple",
#         "orange", "apple", "pear", "banana", "orange",
#         "apple", "kiwi", "pear", "apple", "orange"]

#filter = dict()

#for item in items:
#    filter[item] = 0

#result = set(filter.keys())
#print(result)

#counter= dict()

#for item in items:
#    if (item in counter.keys()):
#        counter[item] += 1
#    else:
#        counter[item] = 1

#print(counter)

items = [6,20,8,19,56,23,87,41,49,53]

def find_max(items):
    if len(items) == 1:
        return items[0]

    op1 = items[0]
    op2 = find_max(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2


print(find_max(items))