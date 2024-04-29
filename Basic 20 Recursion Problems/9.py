import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(i, j, s) :
    if i > j :
        return
    
    # Swapping 
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

    recustion_fuction(i + 1, j - 1, s)

s = input()
s = list(s)
print("The reversed string is:")
recustion_fuction(0, len(s) - 1, s)

print(''.join(s))