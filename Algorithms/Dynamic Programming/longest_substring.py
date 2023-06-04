# 给两个字符串 输出最长子序列的长度
# Given two strings, output the longest substring's length
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
    max_str = s1
    substr_max_len = max(len(s1), len(s2))
    for sub_len in range(substr_max_len, -1, -1):
        for i in range(substr_max_len - sub_len + 1):
            if max_str[i: i + sub_len] in s2:
                return max_str[i: i + sub_len]


if __name__ == "__main__":
    result = longest_substring(string1, string2)
    print(result)
