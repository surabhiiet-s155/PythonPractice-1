def sum_n(n):
    if n == 1:  #Similar to factorial 1=1 1+2=3
        return 1
    return n + sum_n(n-1)  

num = int(input("Enter number: "))
print("Sum =", sum_n(num))
