with open ('magical.txt') as wt:
    w=list(wt)
    l=[]
    for x in range(len(w)):
        w[x]=w[x][:-1]
        l.append(list(w[x].split(';')))
r=l[1:]
print(r)
inp=input()
while inp!='стоп':
    for x in r:
        if x[2]==inp or x[3]==inp or x[4]==inp:
            mn=1000
            name = ''
            for j in r:
                if inp== j[2] or inp== j[3] or inp== j[4]:
                    if int(j[1])<mn and int(j[1])!=0:
                        mn = int(j[1])
                        name = j[0]
            print(name)
            break
    else:
        print('Такую траву мы не используем')
    inp=input()


