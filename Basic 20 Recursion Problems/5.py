import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(cnt, n) :
    if n == 0 :
        print(cnt)
        return
    
    recustion_fuction(cnt + 1, n // 10)
    

n = int(input())
print("The number of digits in the number is  :")

recustion_fuction(0, n)