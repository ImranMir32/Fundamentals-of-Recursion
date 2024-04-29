import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(A, B) :
    if B == 0 :
        print(A)
        return
    
    recustion_fuction(B, A % B)
    

A, B = map(int, input().split())
print("The GCD of ", A, "and", B," is:")

recustion_fuction(A, B)