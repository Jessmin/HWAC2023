import sys
from math import sqrt
def is_prime(x):
    if x ==2:
        return True
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
        return True

def dfs(m,lr,vis):#DFS
    for j in range(len(lr)):
        if vis[j]==1:
            continue
        if is_prime(m+lr[j][0]):
            vis[j]=1
            if lr[j][1] ==0 or dfs(lr[j][1],lr,vis): #匹配成功
                lr[j][1] =m
                print(f'{m},{lr[j][0]}match' )
                return True
            #已经有匹配了，
                print(f'{lr[j][0]} has!')
    return False
# n = int(input())
input_str = "20923 22855 2817 1447 29277 19736 20227 22422 24712 27054 27050 18272 5477 27174 13880 15730 7982 11464 27483 19563 5998 16163"
n = 22
l = list(map(int,input_str.split(' ')))

ll = []
lr = []
for item in l:
    if item%2==0:
        lr.append([item,0])
    else:
        ll.append(item)
print(ll)
print(lr)
count = 0
for item in ll:
    vis = [0]*len(lr)
    if dfs(item,lr,vis):
        count+=1
print(count)
print(lr)