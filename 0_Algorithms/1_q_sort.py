def q_sort(array: list):
    if len(array) < 2:
        return array
    pivot = array[len(array)//2]
    l_arr = []
    r_arr = []
    for each in array:
        if each < pivot:
            l_arr.append(each)
        elif each > pivot:
            r_arr.append(each)
    return q_sort(l_arr) + [pivot] + q_sort(r_arr)

print(q_sort([2,1,6,4,5,3]))