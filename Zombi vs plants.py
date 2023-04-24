def isPalindrome(head) -> bool:
    lenhead = len(head)
    number2 = lenhead - 1
    step = 0
    middlepalinrome = round(lenhead / 2)
    palindrom = True
    for i in head:
        step += 1
        if i == head[number2]:
            number2 -= 1
            if middlepalinrome == step:
                break
        else:
            palindrom = False
            break
    return palindrom
print(isPalindrome([1,2]))