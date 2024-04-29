import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(start, end, array) :
    if start == end :
        return
    
    print(array[start], end=" ")
    recustion_fuction(start + 1, end, array)


print("The elements in the array are : ")
array = list(map(int, input().split()))
recustion_fuction(0, len(array), array)