n = 4

def run(n):
    if n ==0:
        return '1'
    else:
        dst = run(n-1)
        current=dst[0]
        current_num=0
        output = ''
        for i in range(len(dst)):
            if dst[i] == current:
                current_num+=1
                if i == len(dst)-1:
                    output+=str(current_num)+dst[i]
            else:
                output+=str(current_num)+dst[i-1]
                current = dst[i]
                if i == len(dst)-1:
                    output+=str(1)+dst[i]
        return output
def run2(N):
    dp = ['' for i in range(N+1)]
    dp[0]  = '1'
    for idx in range(1,N+1):
        dst = dp[idx-1]
        current=dst[0]
        current_num=0
        output = ''
        for i in range(len(dst)):
            if dst[i] == current:
                current_num+=1
                if i == len(dst)-1:
                    output+=str(current_num)+dst[i]
            else:
                output+=str(current_num)+dst[i-1]
                current = dst[i]
                if i == len(dst)-1:
                    output+=str(1)+dst[i]
        dp[idx] = output
    return dp[N]
    
import time
st_time = time.time()
N = 10
print(run(N))
print((time.time()-st_time)* 1e6)
st_time = time.time()
print(run2(N))
print((time.time()-st_time)* 1e6)
     
    