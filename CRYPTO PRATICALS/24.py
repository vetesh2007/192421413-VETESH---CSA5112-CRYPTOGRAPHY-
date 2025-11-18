# filename: 24_rsa_find_private_key.py
"""
Given e and n, factor n by trial division (works if p,q small) and compute private key d.
Input: prompted.
"""
import math

def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1: raise Exception("No inverse")
    return x % m

def trial_factor(n):
    for i in range(2, int(math.isqrt(n))+1):
        if n % i == 0:
            return i, n//i
    return 1,n

if __name__=='__main__':
    e = int(input("e = ").strip())
    n = int(input("n = ").strip())
    p,q = trial_factor(n)
    if p==1:
        print("Failed to factor n by trial division")
    else:
        phi = (p-1)*(q-1)
        d = modinv(e, phi)
        print("p=",p,"q=",q,"d=",d)
