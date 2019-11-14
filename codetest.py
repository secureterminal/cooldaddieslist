def my_quote_plus(search):
    print(type(search))
    b = my_split(search)
    c = ""
    d = 1

    for e in b:
        d = d + 1
        c = c + e
        if d <= len(b):
            c = c + "+"

    return c


def my_split(my_word):
    final = []
    part_string = ""
    for a in my_word:
        
        if a == "":
            final.append(part_string)
            part_string = ""
        else:
            part_string = part_string + a

    return final


print(my_split("This is a user generated data"))
print(my_quote_plus("This is a user generated data"))
