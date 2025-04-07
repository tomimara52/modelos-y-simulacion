#!/usr/bin/env python
import sys

def mixto(seed, a, c, M):
    k = 1
    gen = [seed]
    x = seed
    while True:
        x = (a*x + c) % M
        
        if x in gen:
            break
        
        gen.append(x)
        k += 1
    
    print("Period:", k)
    print("Sequence:", gen)

try:
    mixto(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
except:
    print("Usage: mix.py <seed> <a> <c> <M>")
