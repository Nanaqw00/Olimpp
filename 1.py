from csv import *
'''with open('magical44.csv', encoding='utf-8') as of:
   r=list(reader(of,delimiter=','))[1:]
   r=[list(map(str,x)) for x in reader(of,delimiter=',')]
   print(r)
#list(reader(of,delimiter=','))[1:]'with open('magical.txt') as wt:
    a=list(wt)

    print(a)
    r = [list(map(str, x)) for x in wt]
print(r)
'''
with open ('magical.txt') as wt:
    w=list(wt)
    l=[]
    for x in range(len(w)):
        w[x]=w[x][:-1]
        l.append(list(w[x].split(';')))
r=l[1:]

count=0
#-count-переменная обозначает травку для сбора
d={}
for el in r:
    if el[1]=='-1':
        if  el[2] not in d:
            d[el[2]]=1
            count+=1
        else:
            d[el[2]] += 1
            count+=1

        if  el[3] not in d:
            d[el[3]]=1
            count+=1
        else:
            d[el[3]] += 1
            count+=1

        if  el[4] not in d:
            d[el[4]]=1
            count+=1
        else:
            d[el[4]] += 1
            count+=1
print(d)
print(count)

with open('magicaPotions.csv','w', encoding='utf-8',newline='') as wt:
    w=writer(wt,delimiter=',')
    w.writerow(['magic_herbs','count_herbs'])
    w.writerows(d)
