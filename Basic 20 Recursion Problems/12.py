import sys
import math
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(root, n):
    if root == 1 or n % root == 0 :
        if root == 1 :
            print("prime number")
        else :
            print("not prime number")
        return
       
    recursion_function(root - 1, n)

n = int(input())
print("The number", n, "is a",end=" ")
root = int(math.sqrt(n))
recursion_function(root, n)

