x1=int(input("1"))
y1=int(input('2'))
x2=int(input("3"))
y2=int(input("4"))
if x2==x1+2 and y2==y1+1 or x2==x1+2 and y2==y1-1 or x2==x1-2 and y2==y1-1 or x2==x1-2 and y2==y1+1 or x2==x1+1 and y2==y1+2 or x2==x1-1 and y2==y1+2:
    print("yes")
else:
    print("no")