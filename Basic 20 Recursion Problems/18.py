import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(start):
    if start == 1 :
        v.append(start)
        return 
    
    v.append(start)
    if start % 2 == 0:
        start //= 2
    else:
        start = 3 * start + 1

    recursion_function(start)


    
start = int(input())
v = []
print("The hailstone sequence starting at ", start, "is : ")

recursion_function(start)
print(*v)
print("The length of the sequence is", len(v))