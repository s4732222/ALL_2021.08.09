import math

def Uv_value(uv,Uz):
    uv=1
    Uz=1
    global a,b,c,d,e,f
    if uv>int(0.8)&Uz<int(2):
        a=1
        print('1')
    elif uv>int(0.8)&int(2)<=Uz<=int(5):
        b=2
        print('2')

    else:
        print('Error')
    
    return uv,Uz

