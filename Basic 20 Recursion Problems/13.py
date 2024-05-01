import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(A, B):
    if B == 0:
        return A
    return recursion_function(B, A % B) 

def LCM(A, B):
    return int((A * B) // recursion_function(A, B))

A, B = map(int, input().split())
print("The LCM of", A, "and", B, "is :", end=" ")
print(LCM(A, B)) 
