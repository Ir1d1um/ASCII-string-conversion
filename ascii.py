from unittest import result


print("########本脚本为ASCII编码解码，无其他用途########")
result_aci=list()  #空list，用于存编码后的ASCII列表
result_str=list()  #空list，用于存解码后的str

num = input("请输入(编码为1，解码为2): ")
if num == str(1):
    str = input("请输入需要编码的字符: ")
    for i in str:
        result_aci.append(ord(i))
    print(result_aci)
elif num == str(2):
    spl=input("请输入分隔符: ")
    ints = input("请输入需要解码的ascii: ").split(spl)#指定分割符
    ints = list(map(int ,ints))
    for i in ints:
        i = chr(int(i))
        result_str.append(i)
    result_str=''.join(result_str)
    print(result_str)
else:
    print("让你输1，2呢，你输入你妈呢？")