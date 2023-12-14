#每次要均分，如果不能均分，取出或者放回，直到手上就1个
num = 15

cnts = []

def fenpei(num,cnt):
    if num == 1:
        cnts.append(cnt)
        return
    else:
        if num%2 ==1:
            fenpei(num+1,cnt+1)
            fenpei(num-1,cnt+1)
        else:
            fenpei(num//2,cnt+1)
    
fenpei(15,0)
print(cnts)
print(min(cnts))