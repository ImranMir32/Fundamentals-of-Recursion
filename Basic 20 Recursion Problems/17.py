import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recursion_function(base, power):
   if power == 0 :
      return 1
   
   return base * recursion_function(base, power - 1)

    
    
base = int(input())
power =  int(input())

print("The value of", base, "to the power of", power,"is : ")

print(recursion_function(base, power))