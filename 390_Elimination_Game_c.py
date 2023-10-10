n = 6
arr =[]
new_arr = []
ltr = True
delete = False
# arr = [1,2,3,4,5,6,7,8,9]
        #0 1 2 3 4 5 6 7 8
        ##[2,4,6,8]
        ###0 1 2 3
        ###[4,8]
for i in range(1, n+1):
    arr.append(i)
print(arr)

for i in range(len(arr)):
    if len(arr) ==1:
        print(arr[0])
        break

    else:
        for j in range(len(arr)):
            if delete:
                new_arr.append(arr[j])
                delete = not delete
            else: 
                delete = not delete

        delete = False
        arr = new_arr
        print("array l2r", arr)
        new_arr = []
        arr = arr[::-1]

        if len(arr) > 1:
            
            for j,k in enumerate(arr):
                if delete:
                    new_arr.append(arr[j])
                    delete = not delete
                else: 
                    delete = not delete
                        
            delete = False
            arr = new_arr
            print("array r2l", arr)
            
            arr = arr[::-1]
            new_arr = []
            
            

# arr = [1,2,3,4,5,6,7,8,9]

# print(arr[::-1])