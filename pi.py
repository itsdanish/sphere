
        
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
    
get_pi()