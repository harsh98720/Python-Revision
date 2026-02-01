# max, min, average without built-ins
def max_num(arr) :
    max_elem = arr[0]
    for i in arr:
        if i > max_elem :
            max_elem = i

    return max_elem

def min_num(arr) :
    min_elem = arr[0]
    for i in arr:
        if i < min_elem :
            min_elem = i

    return min_elem

def avg(arr):
    total = 0
    count = 0

    for i in arr:
        count+= 1
        total+= i

    return round(total/ count, 2)

arr = [1,2,3,4,5,6,7,16,5,-5,3,2,1]

# duplicate remove without set()

without_duplicate_arr = []

for elem in arr:
    if elem not in without_duplicate_arr:
        without_duplicate_arr.append(elem)

print(without_duplicate_arr)