def ipv4_to_int(ip):
    # 将IPv4地址分割成四个数字
    octets = list(map(int, ip.split('.')))

    # 将每个数字转换为二进制并拼接成32位的二进制数
    binary_str = ''.join(format(octet, '08b') for octet in octets)
    print(binary_str)
    # 将二进制字符串转换为整数
    integer_value = int(binary_str, 2)

    return integer_value

# 示例
ipv4_address = "192.168.1.1"
integer_value = ipv4_to_int(ipv4_address)
print(f"The IPv4 address {ipv4_address} as a 32-bit integer is: {integer_value}")
