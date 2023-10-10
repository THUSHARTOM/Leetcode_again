
# This is a medium level problem which I coulnt solve. The nested loop takes too much space.
# The optimized solution is given below

# n = 100000000
# arr =[]
# new_arr = []
# ltr = True
# delete = False
# # arr = [1,2,3,4,5,6,7,8,9]
#         #0 1 2 3 4 5 6 7 8
#         ##[2,4,6,8]
#         ###0 1 2 3
#         ###[4,8]
# arr = list(range(1,n+1))
# # print(arr)

# for i in range(len(arr)):
#     if len(arr) ==1:
#         print(arr[0])
#         break

#     elif len(arr) > 1:
#         for j,k in enumerate(arr):
#             if j%2!=0:
#                 new_arr.append(arr[j])
                    
#         arr = new_arr[::-1]
#         # print("array", arr)
#         new_arr = []
            

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

