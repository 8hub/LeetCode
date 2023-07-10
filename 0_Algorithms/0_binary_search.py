def binary_search(to_find:int, numbers: list) -> int:
    # left pointer
    lp = 0
    # right pointer
    rp = len(numbers) - 1
    while(lp <= rp):
        mid = (lp + rp)//2
        guess = numbers[mid]
        if(guess == to_find):
            return mid
        elif(guess > to_find):
            rp = mid - 1
        else:
            lp = mid + 1
    return None
print(binary_search(6,[0,1,2,3,4,5,6,7]))
print(binary_search(7,[0,1,2,3,4,5,6,7]))
print(binary_search(10,[0,1,2,3,4,5,6,7]))
print(binary_search(0,[0,1,2,3,4,5,6,7]))
print(binary_search(1,[0,1,2,3,4,5,6,7]))
print(binary_search(420,[0,1,2,3,4,5,6,7]))
print(binary_search(-20,[0,1,2,3,4,5,6,7]))