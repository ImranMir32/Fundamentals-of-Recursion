import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(digit_sum, n) :
    if n == 0 :
        print(digit_sum)
        return
    
    digit_sum += (n % 10)
    recustion_fuction(digit_sum, n // 10)
    

n = int(input())
print("The number of digits in the number is  :")

recustion_fuction(0, n)