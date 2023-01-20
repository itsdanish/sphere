def bounce():
    first = 10
    index = 0.6
    bounces = 4
    h = first * index
    middle = 2 * h
    last = first * index**bounces
    d = first + (bounces - 1)*(middle) + last
    print(d)
        
bounce()
