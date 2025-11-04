def safe(b, r, c, n):
    for i in range(c):
        if b[r][i] or (r-i>=0 and b[r-i][c-i]) or (r+i<n and b[r+i][c-i]):
            return False
    return True

def solve(b, c, n):
    if c == n:
        for r in b: print(*r)
        print(); return True
    for i in range(n):
        if safe(b, i, c, n):
            b[i][c] = 1
            if solve(b, c+1, n): return True
            b[i][c] = 0
    return False

n = int(input("Enter number of Queens: "))
b = [[0]*n for _ in range(n)]
solve(b, 0, n)
