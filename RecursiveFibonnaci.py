# Recursive Fibbonaci

def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n - 1) + fibonnaci(n - 2)

# Time Complexity O(2^n)
# Space Complexity O(n)

print()
print('-------------------------------------------------------------------------')
print(fibonnaci(98))
print('-------------------------------------------------------------------------')

"""In this approach we recursively calling our defined function which makes slower to compute and larger amount of Memory Usage.
"""