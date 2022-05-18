# import file for prgrm - permutation.py


def fact(a):
    b=1
    if a==1 or a==0:
        return b
    else :
        b=a*fact(a-1)
        return b
