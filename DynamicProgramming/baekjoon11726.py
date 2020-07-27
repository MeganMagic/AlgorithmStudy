N = int(input())

#init
opt = [0, 1, 2]
if N <= 2 : print(opt[N])

#optimal[n] = optimal[n-1] + optimal[n-2]
else :
    for n in range(3, N+1) : opt.append( opt[n-1] + opt[n-2] )
    print(opt[-1]%10007)
