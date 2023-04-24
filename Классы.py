import string
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
def defis(func):
    def wrapper(x):
        stop =True
        lst=[]
        for i in list(func(x)):
            if i =="-":
                if stop:
                    stop=False
                    lst.append(i)
            else:
                stop =True
                lst.append(i)
        return "".join(lst)
    return wrapper
@defis
def latin(x):
    return "".join(["-" if i not in t and string.ascii_lowercase+string.ascii_uppercase else t[i] for i in x.lower()  ])
s = input()
print(latin(s))