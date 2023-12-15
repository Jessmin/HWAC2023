input = [7,5,9,4,2,6,8,3,5,4,3,9]
# input = [1,2,3,7,1,5,9,3,2,1]



output = []
def find_route(arr,cached):
    for i in range(len(arr)-2,-1,-1):
        if arr[i]+i ==len(arr)-1:
            cached.append(i)
            if 0<=i<=len(input)//2:
                cached.append(i)
                output.append(cached)
                return cached
            elif i<0:
                return cached
            # loop
            arr = arr[:i]
            find_route(arr,cached)
            #回溯
            cached = cached[0:-1]
        else:
            print(f"{i} :{arr[i]} pass")
cached = []
find_route(input,cached)
print(output)