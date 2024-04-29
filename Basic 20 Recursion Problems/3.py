import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(fisrt, second, limit) :
    if limit == 0 :
        return 
    
    temp = second + fisrt
    fisrt = second
    second = temp
    print(fisrt, end=" ")

    recustion_fuction(fisrt, second, limit - 1)
    

limit = int(input())
print("The Series are :")

recustion_fuction(0, 1, limit)