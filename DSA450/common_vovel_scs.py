string = "aeiou"
text2 = 'aeiou'

dic = {}
dic = dic.fromkeys(text2, 0)
print(dic)
le = 0
max_len = 0
for i in range(len(string)):
    if i == 0:
        le = 1
        dic[string[i]] = 1
    elif string[i] >= string[i - 1]:
        le += 1
        dic[string[i]] = 1
    else:
        if dic['a'] != 0 and dic['e'] != 0 and dic['i'] != 0 and dic['o'] != 0 and dic['u'] != 0:
            max_len = max(max_len, le)
        le = 1
        dic = dic.fromkeys(text2, 0)
        dic[string[i]] = 1
if dic['a'] != 0 and dic['e'] != 0 and dic['i'] != 0 and dic['o'] != 0 and dic['u'] != 0:
    max_len = max(max_len, le)
print(max_len)