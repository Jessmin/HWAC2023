input = [10,9,8,7,6,5,4,3,2,1]

max = 0
for i in range(0,len(input)):
    for j in range(i,len(input)):
        w = j-i
        h = min(input[i],input[j])
        area = w*h
        if area>max:
            max = area
            
print(max)