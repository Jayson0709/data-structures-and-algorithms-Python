# 给两个字符串 输出最长子序列的长度
import sys

input_thing = []
result = ""
while True:
    sn = sys.stdin.readline().strip()
    if sn == '':
        break
    sn = list(sn.split())
    input_thing.append(sn)
string1 = input_thing[0][0]
string2 = input_thing[1][0]
print("The first string is : ", string1)
print("The second string is : ", string2)


def longest_substring(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    maxstr = s1
    substr_maxlen = max(len(s1), len(s2))
    for sublen in range(substr_maxlen, -1, -1):
        for i in range(substr_maxlen - sublen + 1):
            if maxstr[i: i + sublen] in s2:
                return maxstr[i: i + sublen]


if __name__ == "__main__":
    result = longest_substring(string1, string2)
    print(result)
