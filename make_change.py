

from math import*
pay = float(input('How much did you pay?'))
cost = float(input('How much did it cost?'))
def f(x,y):
    return(x - y)
print(f'You received ${f(pay,cost):.2f} in change. That is...')
v = f(pay,cost)

def q(x):
    return(x//.25)

def d(x):
    return((x-q(x)*.25)//.10)

def n(x):
    return((x-q(x)*.25-d(x)*.10)//.05)

def p(x):
    return(round(((x*100) % 5),0))

#lightwork
    
if(1>=q(v)>0):
    print(f'{int(q(v))} quarter')
if(q(v) > 1):
    print(f'{int(q(v))} quarters')
if(1>=d(v)>0):
    print(f'{int(d(v))} dime')
if(d(v) > 1):
    print(f'{int(d(v))} dimes')
if(n(v)>0):
    print(f'{int(n(v))} nickel')
if(1>=q(v) > 1):
    print(f'{int(n(v))} nickels')
if(1 >= p(v)>0):
    print(f'{int(p(v))} penny')
if(p(v) > 1):
    print(f'{int(p(v))} pennies')


    