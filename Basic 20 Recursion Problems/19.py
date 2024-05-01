import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(i, orginal_string):
    if i == len(orginal_string) :
        return
    
    copy_string.append(orginal_string[i])
    recursion_function(i + 1, orginal_string)
    

orginal_string = input()
copy_string = []

recursion_function(0, orginal_string)

print("The first string is :", orginal_string)                                                                         
print("The copied string is : ", end="")
print(''.join(copy_string))