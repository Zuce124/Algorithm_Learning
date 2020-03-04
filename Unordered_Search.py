items = [6,20,8,19,56,23,87,41,49,53]
items_ord = [6,8,19,20,23,41,49,53,56,87]
def find_item_unord(item, itemlist):
    for i in range(len(itemlist)):
        if item == itemlist[i]:
            return i

    return None

def find_item_ord(item,itemlist):

    lenght = len(itemlist)-1

    lower = 0
    upper = lenght

    while lower <= upper:
        mid = (lower+upper)//2

        if itemlist[mid] == item:
            return mid

        if item > itemlist[mid]:
            lower = mid+1
        else:
            upper = mid-1

    if lower > upper:
        return None

items1 = [6,8,19,20,23,41,49,53,56,87]
items2 = [6,20,8,19,56,23,87,41,49,53]

def is_sorted(itemlist):
    #for i in range(len(itemlist)-1):
     #   if itemlist[i+1] < itemlist[i]:
      #      return False

    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    #return True

#print(find_item_unord(87, items))

#print(find_item_ord(23,items_ord))

print(is_sorted(items1))
print(is_sorted(items2))
