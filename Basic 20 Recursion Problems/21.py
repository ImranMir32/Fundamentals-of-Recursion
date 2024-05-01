import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(f, l, value, s):
    if f > l :
        return False
    mid = (f + l) // 2

    if v[mid] == value :
        return True
    if v[mid] > value :
        l = mid - 1
    else :
        f = mid + 1

    return recursion_function(f, l, value,  v)


v = list(map(int , input().split()))
value = int(input())

if not recursion_function(0, len(v)-1, value, v) :
    print("This value doesn't exits in the array")
else :
    print("Value found in the array")