import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(n, limit) :
    if limit < n :
        return 

    print(n, end=" ")
    if n % 10 == 0 :
       print()

    recustion_fuction(n + 1, limit)
    


print("The natural numbers are :")

limit = int(input())
recustion_fuction(1, limit)