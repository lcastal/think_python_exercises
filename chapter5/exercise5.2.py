def check_fermat(a,b,c,n):
    an_bn = a**n + b**n;
    cn = c**n;

    if(an_bn == cn):
        print ("Holy smokes, Fermat was wrong!")
    else:
        print ("No, that doesn't work")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
n = int(input("n: "))

check_fermat(a,b,c,n)
