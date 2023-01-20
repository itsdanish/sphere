def sphere():
    pi = 3.14
    #r = float(input('enter sphere radius: '))
    r = 2
    d = 2 * r
    c = 2 * pi * r
    v = 4/3 * pi * r**3
    sa = 4 * pi * r**2
    output = [d, c, sa, v]
    print(output)
    print('diameter: ', d)
    print('circumference: ', c)
    print('surface area: ', sa)
    print('volume: ', v)


def bounce():
    first = 10
    index = 0.6
    bounces = 4
    h = first * index
    middle = 2 * h
    last = first * index**bounces
    d = first + (bounces - 1)*(middle) + last
    print(d)
        
def get_pi():
    its_0 = 10000
    its = its_0 * 2
    pi_0 = 0
    neg = -1
    for i in range(1,its+1,2):
        neg = neg * -1
        pi_0 = pi_0 + neg * 1/i
    pi = pi_0 * 4
    print(pi)
    
def print():
    month = 1
    princ = 1000
    down = .1 * princ
    monthly_paym = .05 * (princ - down)
    balance = princ - down
    interest = balance * (.12/12)
    p_remain = balance - (monthly_paym - interest)
    print("remain: ", p_remain)
    print("| Month | Curr. Balance")
    

print()