def uniquePaths(n, m):
    if n == 1 or m == 1:
        return 1
    
    return uniquePaths(n - 1, m) + uniquePaths(n, m - 1)

print(uniquePaths(7, 7))