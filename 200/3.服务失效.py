input_str = 'a1-a2,a5-a6,a2-a3'
wrong_str ='a5,a2'


input_list = input_str.split(',')
a=[]
b=[]
for item in input_list:
    p1,p2 = item.split('-')
    a.append(p1)
    b.append(p2)
for wrong in wrong_str.split(','):
    if wrong in b:
        idx = b.index(wrong)
        a[idx]=-1
        b[idx]=-1
    if wrong in a:
        idx = a.index(wrong)
        a[idx] = -1
a.extend(b)
output = []
for res in a:
    if res!=-1 and res not in output:
        output.append(res)
print(output)