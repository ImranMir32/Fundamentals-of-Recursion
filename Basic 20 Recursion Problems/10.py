import sys
sys.stdout = open('Basic 20 Recursion Problems/output.txt', 'w')
sys.stdin = open('Basic 20 Recursion Problems/input.txt', 'r')

def recustion_fuction(limit) :
    if limit == 1 :
        return 1
    
    return limit * recustion_fuction(limit - 1)

# Another way
# def recustion_fuction(result, limit) :
#     if limit == 0 :
#         print(result)
#         return 
    
#     result *= limit
#     recustion_fuction(result, limit - 1)
    
limit = int(input())
print("The Factorial of", limit, " is :")
print(recustion_fuction(limit))
# recustion_fuction(1, limit)