def bubble_sort(n):

    lenght = len(n)

    while lenght != 1:
        for i in range(lenght-1):
            if n[i+1] < n[i]:
                n[i+1],n[i] = n[i],n[i+1]
        lenght -= 1

    return(n)


def merge_sort(n):
    if len(n) > 1:
        mid = len(n)//2
        left = n[:mid]
        right = n[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0 #left
        j = 0 #right
        k = 0 #merged

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
               n[k] = left[i]
               i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1


        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1


def quick_sort(n, first, last):
    if first<last:
        pivotIdx = partion(n, first, last)

        quick_sort(n, first, pivotIdx-1)
        quick_sort(n, pivotIdx+1, last)

def partion(n, first, last):
    pivotvalue = n[first]
    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and n[lower] <= pivotvalue:
            lower += 1

        while n[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        if upper < lower:
            done = True
        else:
            n[lower], n[upper] = n[upper], n[lower]

    n[first], n[upper] = n[upper], n[first]
    print(n)
    return upper




n = [2,3,6,4,2,3,563,7789,654,34,5,6]
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
#print(bubble_sort(n))

#merge_sort(n)

print(items)
quick_sort(items, 0, len(items)-1)
print(items)
