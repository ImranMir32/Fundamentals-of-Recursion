import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(i, s):
    if i == len(s) or (s[i] > 'A' and s[i] < 'Z') :
        if i == len(s) :
            return -1 
        else :
            return s[i]
        
    return recursion_function(i + 1, s)
  
s = input()
letter = recursion_function(0, s)
if letter == -1 :
    print("There is no capital letter")
else :
    print("The first capital letter appears in the string testString is",letter )                                                                         
