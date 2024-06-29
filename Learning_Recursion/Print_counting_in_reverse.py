
n=int(input())
def print_counting(n):
    if n==0: 
        return 
    print(n)
    print_counting(n-1)
print_counting(n)