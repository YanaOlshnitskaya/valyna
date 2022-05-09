a=float(input("Введите число"))
b=float(input("Введите число"))
c=float(input("Введите число"))
D=(+(b*b)-4*a*c)
if D!=0 and D>0:
    x1=((-b*b)+(sgrt(D)))/(2*a)
    x2=((b*b)+(sgrt(D)))/(2*a)
    print(x1,x2)
if D==0:
    x=(-b/2*a*2)
    print(x)
if D<0:
    x="нет корней"
    print(x)