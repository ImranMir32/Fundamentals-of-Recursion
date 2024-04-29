import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(sum, n, limit) :
    if limit < n :
        print(sum)
        return 
    
    sum += n
    recustion_fuction(sum , n + 1, limit)
    

limit = int(input())
print("The sum of numbers from 1 to", limit, ":")

recustion_fuction(0, 1, limit)