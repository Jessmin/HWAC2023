import sys
num = 2

input = [
    [0,255],
    [200,60],
]

_min = sys.maxsize
for it in input:
    st,time = it
    if time<128:
        res = st+time
        if res<_min:
            _min = res
    else:
        time = bin(time)
        _exp = int(time[4:7],2)
        _mant = int(time[-4:],2)
        res = (_mant|0x10)<<(_exp+3)
        if res<_min:
            _min = res
print(_min)