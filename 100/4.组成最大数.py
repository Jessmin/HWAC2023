from functools import cmp_to_key

# 自定义比较函数，确保拼接后的数是最大的
def custom_compare(x, y):
    return int(x + y) - int(y + x)

def largest_number(nums):
    # 将数字转换为字符串
    nums_str = list(map(str, nums))
    
    # 对字符串数组进行排序
    nums_str.sort(key=cmp_to_key(custom_compare), reverse=True)

    # 拼接排序后的字符串数组
    result = ''.join(nums_str)

    return result

# 示例：数字列表 [3, 30, 34, 5, 9]
numbers = [3, 30, 34, 5, 9,900]
result = largest_number(numbers)
print(result)
