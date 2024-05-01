import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(v, dec):
    if dec == 0:
        return
    
    recursion_function(v, dec // 2)
    v.append(str(dec % 2)) 
    

dec = int(input())
print("The Binary value of decimal no.", dec, " is :")
v = []
recursion_function(v, dec)

print(''.join(v))
