#Фияункция для расчёта ak=2b(k−1)+a(k−1);  bk=2a(k−1)+b(k−1)  a1=b1=1 

def raschet_rec(k):  #k - кол-во повторений
    ak=1
    bk=1
    if k == 1:
        ak1=2*(bk)+(ak)
        bk1=2*(ak)+(bk)
        return (ak1, bk1)
    else:
        buf=raschet_rec(k-1)
        ak=buf[0]
        bk=buf[1]
        ak1=2*(bk)+(ak)
        bk1=2*(ak)+(bk)
        return (ak1, bk1)


def raschet_iter(k):
    ak=1
    bk=1
    for i in range(k):
        ak1=2*(bk)+(ak)
        bk1=2*(ak)+(bk)
        ak=ak1
        bk=bk1
    return (ak, bk)


print(raschet_rec(3))
print(raschet_iter(3))
