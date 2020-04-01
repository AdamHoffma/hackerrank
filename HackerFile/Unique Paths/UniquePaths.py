import timeit

# code_to_test = """
# def uniquePaths(n, m):    
    
#     if n == 1 or m == 1:
#         return 1        
    
#     return uniquePaths(n - 1, m) + uniquePaths(n, m - 1)
# print(uniquePaths(15, 15))
#     """

# elapsed_time = timeit.timeit(code_to_test, number=1)/1
# print(elapsed_time)


def paths(m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j-1]
            print(cur[j])
    return cur[-1]

print(paths(7, 3))



