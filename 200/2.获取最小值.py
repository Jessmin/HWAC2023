input_str = '2615371'
nums = 4


def find_smallest(input_str,cnts):
    if cnts==nums+1:
        print(input_str)
        return
    results = []
    for i in range(len(input_str)):
        temp = input_str[0:i]+input_str[i+1:len(input_str)]
        results.append(int(temp))
    find_smallest(str(min(results)),cnts+1)
    
find_smallest(input_str,1)