import time

class solution:
    def sqrt(self, x):
        min = 0
        max = x/2

        if x == 1:
            return 1
        while True:
            
            
            search = (min + max)/2
            # print("Search", search)

            if int(min) == int(max) or search**2 == x:
                break
            elif search**2>x:
                max = search
            elif search**2<x:
                min = search
            # print(int(min), int(max))
        return search

s = solution()
print(s.sqrt(74))