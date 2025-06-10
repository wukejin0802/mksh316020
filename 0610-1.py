def fab(n):
    if n ==0: return 0
    if n ==1: return 1
    return fab(n-1) + fab(n-2)
for i in range(20):
    print(fab(i)," ",end="")