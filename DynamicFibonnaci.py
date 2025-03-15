# Fibonnaci Dynamicly Programmed

def fibonnaci(n):
    if n < 2:
        return n
    
    dp = [0, 1]

    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return i-1, dp[1]

# Time Complexity O(n)
# Space Complexity O(1)

Nth_Fibonacci, Fibbonaci_Value = fibonnaci(98)
print()
print('-------------------------------------------------------------------------')
print(f"The value of {Nth_Fibonacci}-th Fibonnaci Number is: {Fibbonaci_Value}")
print('-------------------------------------------------------------------------')

"""Intuition Behind the Code: 
Instead of maintaining a full array of all Fibonacci numbers up to n, 
this approach uses just two variables (represented by the two elements in dp) to store the last two Fibonacci numbers. 
This optimization reduces the memory usage to a constant amount, making the code more efficient. 
It's a neat iterative way to calculate Fibonacci numbers without using recursion or a large array."""

