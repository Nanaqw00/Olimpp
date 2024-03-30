with open ('magical.txt') as wt:
    w=list(wt)
    l=[]
    for x in range(len(w)):
        w[x]=w[x][:-1]
        l.append(list(w[x].split(';')))
r=l[1:]
#d-словарик для упопрядочивания инфы
d={}
res={}
for el in r:
    if el[0] not in d:
        d[el[0]]=1
    else:
        d[el[0]]+=1
print(d)

