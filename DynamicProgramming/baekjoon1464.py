# 백준 1464번
X = int(input())

#init : X=1 -> opt=0
opt = [0, 0]

#비교하기
#1. opt[x-1]+1
#2. opt[x/2]+1 (if x%2 == 0)
#3. opt[x/3]+1 (if x%3 == 0)
for x in range(2, X+1) :
    candidate = opt[x-1] + 1
    
    if x%2 == 0 :
        temp = opt[int(x/2)] + 1
        if temp < candidate : candidate = temp
        
    if x%3 == 0 :
        temp = opt[int(x/3)] + 1
        if temp < candidate : candidate = temp
        
    opt.append(candidate)
    
print(opt[-1])
