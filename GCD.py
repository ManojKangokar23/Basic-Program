//Brute force approach. 
a = 48
b = 18

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)



//Reverse loop 
a = 48
b = 18

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print("GCD =", i)
        break