import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(n, limit):
    if limit < n :
        return
    
    print(n,end=" ")
    recursion_function(n + 2, limit)
    
limit = int(input())

print("All even numbers from 1 to", limit,"are :")
recursion_function(2, limit)
print()


print("All even numbers from 1 to", limit,"are :")
recursion_function(1, limit)
