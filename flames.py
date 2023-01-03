def myreverse(c,d):
    t=[]
    for i in range(d-1,len(c)):
        t.append(c[i])
    for i in range(d-1):
        t.append(c[i])
    return(t)
    
l=input("enter the name1:")
m=input("enter the name2:")
l1=list(l)
l2=list(m)
i=0
while i<len(l1):
    j=0
    while j<len(l2):
        if l1[i]==l2[j]:
            l1.remove(l1[i])
            l2.remove(l2[j])
            i=i-1
            j=j-1
            break
        j+=1
    i+=1
print(l1,l2)
a=len(l1)+len(l2)
c=["f","l","a","m","e","s"]
d=a%6
print(d,a)
k=6
while True:
    if len(c)==1:
        break
    if d==0:
        c.remove(c[len(c)-1])
        print(c)
        k=k-1
        d=a%k
    else:
        print(d,c)
        c.remove(c[d-1])
        c=myreverse(c,d)
        print(c)
        k=k-1
        d=a%k
print(c)    
    
