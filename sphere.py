#sphere.py
#Author: Danish Rizvi
#01/18/23

def main():
    #This program converts radius to diameter, circumference
    #volume, and surface area of a sphere
    r = float(input("Enter radius: "))
    #calling sphere function with argument, radius
    sphere(r)


def sphere(r):
    pi = 3.14
    #diameter formula 2r
    d = 2 * r
    #circumference: 2(pi)r
    c = 2 * pi * r
    #volume: 4/3(pi)r^3
    v = 4/3 * pi * r**3
    #surface area: 4(pi)r^2
    sa = 4 * pi * r**2
    #putting calculated values in list
    output = [d, c, sa, v]
    #printing list
    print(output)

main()