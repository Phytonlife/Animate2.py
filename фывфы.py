def string_shifr(string):
    lens=len(string)
    number=-1
    obj=string[number]
    while not obj.isdigit():
        number-=1
        obj = string[number]

    lastpart=string[number::]

    return lastpart
print(string_shifr("2[a2[b]]"))


