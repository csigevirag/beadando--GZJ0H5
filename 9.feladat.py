from math import sqrt

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))

# def legnagyobbprimtenyezo(szam):
#     primtenyezo=0
#     for i in range(1,szam):
#         if prim(i) and szam % i == 0:
#             primtenyezo = i
#     return primtenyezo
#
# def prim(n):
#     for i in range(2,int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
# print(legnagyobbprimtenyezo(600851475143))