c0=int(input("enter a non-egative & non-zero no:"))
steps=0
while c0>1 and c0!=0:
    if c0%2==0:
        c0=c0/2
        print(c0)
        steps+=1
        continue
    elif c0%2!=0:
        c0=3*c0+1
        print(c0)
        steps+=1
        continue
    else:
        c0=c0/2
        print(c0)
        steps+=1
        continue
print("Steps:",steps)
