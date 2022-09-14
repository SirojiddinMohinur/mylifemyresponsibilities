a=[1,2,3,1,34,565,452,2,6,9,10]
b=[10,2,9,1,0,3,35,2,6,34,10,36]
c=[]
s=0
for i in a: # a jadval elementlarini i o`zgaruvchiga tenglashtirdik
    if i in b : # a jadval elementlarini b jadvaldan qidirdik
        if i not in c: c.append(i) # c jadvalga a va b dagi bir xillarini qo`shib chiqdik
        s+=1
print(c)