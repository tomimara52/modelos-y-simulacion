#!/usr/bin/python3

def von_neumann(seed):
    k = 1
    gen = [seed]
    x = seed
    while True:
        x = ((x*x) // 100) % 10000
        
        if x in gen:
            break
        
        gen.append(x)
        k += 1
    
    print("Period:", k)
    print("Sequence:", gen)

von_neumann(int(input("Type the seed: ")))
