#含有7或者7的倍数
input = [0,0,0,2,1]
nums = sum(input)
val = nums*7
output = [0 for i in range(len(input))]

idx =0
cnts=0
for i in range(val):
    if cnts==nums:
        break
    if (i+1)%7==0 or ((i+1)-7)%10==0:
        output[idx] +=1
        cnts+=1
    idx+=1
    if idx>len(output)-1:
        idx = idx-len(output)
print(output)