# (M) Medium level problem
# O(log(n)) time complexity 
# (R)review in spaced intervels 


N = 8   # number of remaining numbers
fwd = True   # flag for forward/backward elimination
m = 2    # elimination step/interval
s = 0   # elimination base

while N > 1:
    if fwd or N % 2 == 1: 
        s += m // 2
        print("S = ",s)
    m *= 2
    print("M = ", m)
    N = N // 2
    print("N = ", N)
    print("N%2 = ",  N%2)
    fwd = not fwd   # reverse the pass direction
print(s+1)