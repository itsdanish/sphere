
def store():
    month = 1
    princ = 1000
    down = .1 * princ
    monthly_paym = .05 * (princ - down)
    balance = princ - down
    interest = balance * (.12/12)
    p_remain = balance - (monthly_paym - interest)
    print("remain: ", p_remain)
    print("| Month | Curr. Balance | ")
    

store()