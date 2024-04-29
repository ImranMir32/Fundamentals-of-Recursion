import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(mx, start, array) :
    if start == len(array) :
        print(mx)
        return
    
    mx = max(mx, array[start])
    recustion_fuction(mx, start + 1, array)


print("Largest element of an array is : ")
array = list(map(int, input().split()))
recustion_fuction(0, 0, array)