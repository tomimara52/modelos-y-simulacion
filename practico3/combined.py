#!/usr/bin/python3
import sys
from math import lcm
import matplotlib.pyplot as plt

"""
Computes two generators and the generator of their sum
"""
def combined(seed, a1, c1, M1, a2, c2, M2, M, add=1):
    z = seed + add * seed
    gen = [z]
    k = 1
    x = seed
    y = seed
    gen_x = [seed]
    gen_y = [seed]

    plot_x = []
    plot_y = []

    # this assumes that the two input methods have maximum period possible
    period1 = M1 if c1 != 0 else M1 - 1
    period2 = M2 if c2 != 0 else M2 - 1
    period = lcm(period1, period2)

    while True:
        x = (a1*x + c1) % M1
        y = (a2*y + c2) % M2

        # if the pair (x, y) was seen previously then the z generator is going to start repeating
        repeated = [i for i, (x_e, y_e) in enumerate(zip(gen_x, gen_y)) if x_e == x and y_e == y]

        if len(repeated) > 0:
            break

        gen_x.append(x)
        gen_y.append(y)

        z = (x + add * y) % M
        
        gen.append(z)
        k += 1
    

    print("Period (maybe):", period)
    print("Period posta:", k)
    print("Sequence:", gen)

    return gen, gen_x, gen_y

try:
    gen_z, gen_x, gen_y = combined(int(sys.argv[1]), 
                             int(sys.argv[2]), 
                             int(sys.argv[3]), 
                             int(sys.argv[4]), 
                             int(sys.argv[5]), 
                             int(sys.argv[6]),
                             int(sys.argv[7]),
                             int(sys.argv[8]),
                             int(sys.argv[9]) if len(sys.argv) >= 10 else 1,
                             )
    
    plot_z = plt.subplot2grid((2,2), (1,0), colspan=2)
    plot_z.scatter(gen_z[:len(gen_z)-1], gen_z[1:], s=5)
    plot_z.set_title('z')
    plot_z.set_xlabel('z_i')
    plot_z.set_ylabel('z_(i+1)')
    plot_z.set_aspect('equal', adjustable='box')


    plot_x = plt.subplot2grid((2,2), (0,0))
    plot_x.scatter(gen_x[:len(gen_x)-1], gen_x[1:], s=5)
    plot_x.set_title('x')
    plot_x.set_xlabel('x_i')
    plot_x.set_ylabel('x_(i+1)')
    plot_x.set_aspect('equal', adjustable='box')


    plot_y = plt.subplot2grid((2,2), (0,1))
    plot_y.scatter(gen_y[:len(gen_y)-1], gen_y[1:], s=5)
    plot_y.set_title('y')
    plot_y.set_xlabel('y_i')
    plot_y.set_ylabel('y_(i+1)')
    plot_y.set_aspect('equal', adjustable='box')

    plt.show()


except Exception as e:
    print(e)
    print("Usage: combined.py <seed> <a1> <c1> <M1> <a2> <c2> <M2> <M>")
