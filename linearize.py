def linearize_rec(mas):     #mas - массив для линериализации
    otv = []
    for key_1 in mas:
        if  isinstance(key_1, list):
            buf=linearize_rec(key_1)
            for key_2 in buf:
                otv.append(key_2)
        else:
            otv.append(key_1)
    return otv

def linearize_iter(mas):
    otv=[]
    while mas:
        cur=mas.pop(0)
        if isinstance(cur, list):
            mas.extend(cur)
        else:
            otv.append(cur)
    return otv

print(linearize_rec([1, 2, [3, 4, [5, [6, []]]]]))
print(linearize_iter([1, 2, [3, 4, [5, [6, []]]]]))
