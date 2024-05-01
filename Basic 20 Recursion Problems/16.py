import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(i, j, s):
    if i > j :
        return True

    if s[i] != s[j] :
        return False
    
    return recursion_function(i + 1, j - 1, s)

    
    
s = input()
if recursion_function(0, len(s)-1, s) :
   print("The entered word is a palindrome")
else :
    print("The entered word is not a palindrome")
