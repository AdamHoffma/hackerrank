import timeit

code_to_test = """
def uniquePaths(n, m):    
    
    if n == 1 or m == 1:
        return 1        
    
    return uniquePaths(n - 1, m) + uniquePaths(n, m - 1)
print(uniquePaths(7, 7))
    """

elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)
#print(uniquePaths(7, 7))
