# BeeCrowd: Approximate Number of Primes
import math
if __name__ == '__main__':
    n=int(input())
    P=n/math.log(n)
    M=1.25506*P
    print("{:.1f}".format(P), "{:.1f}".format(M))