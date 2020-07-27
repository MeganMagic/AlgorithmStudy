caseNum = int(input())

for i in range(caseNum) :
    N = int(input())
    
    #init
    opt = [0, 1, 2, 4]
    if N <= 3 : 
        print( opt[N] )
        continue
        
    #optimal[n] = optimal[n-1] + optimal[n-2] + optimal[n-3]
    else :
        for n in range(4, N+1) : opt.append( opt[n-1] + opt[n-2] + opt[n-3] )
        print(opt[-1])
