import copy
input = [
    [1,1,0],
    [0,0,0],
    [1,0,0]
]
#3x3
cnts = 0
while(1):
    input_copy = copy.deepcopy(input)
    # done
    if sum(sum(x) for x in input_copy)==9:
        print(cnts)
        break
    for i in range(3):
        for j in range(3):
            if input[i][j] == 1:
                if i+1<3:
                    if input_copy[i+1][j] == 0:
                        input_copy[i+1][j] =1
                if j+1<3:
                    if input_copy[i][j+1] == 0:
                        input_copy[i][j+1] =1
    cnts+=1
    if input_copy == input:
        print(input)
        print(input_copy)
        print('wrong')
        break
    input = input_copy