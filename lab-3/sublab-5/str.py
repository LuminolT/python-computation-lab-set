# 编写函数 rotateword ，接收一个字符串 strsrc 以及一个整数 n 作为参数，
# 返回新字符串 strdes ，其各个字母是 strsrc 中对应位置各个字母在字母表中“轮
# 转” n 字符后得到的编码。


import re


def rotateword(strsrc, n):
    strdes = ''
    for i in strsrc:
        if i.isalpha():
            if i.isupper():
                strdes += chr((ord(i)-ord('A')+n) %
                              26+ord('A'))  # ord()返回字符的ASCII码
            else:
                strdes += chr((ord(i)-ord('a')+n) % 26+ord('a'))
        else:
            strdes += i
    return strdes


print(f"凯撒加密：{rotateword('azcZ', 1)}")


# 使用re编写rotateword_re函数
def rotateword_re(strsrc, n):
    strdes = ''
    for i in strsrc:
        if re.match(r'[a-zA-Z]', i):  # re.match()从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
            if i.isupper():
                strdes += chr((ord(i)-ord('A')+n) %
                              26+ord('A'))
            else:
                strdes += chr((ord(i)-ord('a')+n) % 26+ord('a'))
        else:
            strdes += i
    return strdes


print(f"使用re的凯撒加密：{rotateword_re('azcZ', 1)}")


# 编写函数 avoids ，接收一个单词和一个含有禁止字母的字符串，判断
# 该单词是否含有禁止字母。

def avoids(word, forbidden):
    for i in word:
        if i in forbidden:
            return False
    return True

# 使用列表推导式编写avoids函数
# def avoids(word, forbidden):
#     return False if [i for i in word if i in forbidden] else True


print(f"avoid：{avoids('abc', '.')}")


# 使用re编写avoids_re函数


def avoids_re(word, forbidden):
    if re.search(r'[%s]' % forbidden, word):  # re.search()扫描整个字符串并返回第一个成功的匹配
        return False
    return True

# def avoids_re(word, forbidden):
#     if re.search(r'[forbidden]' , word):  # re.search()扫描整个字符串并返回第一个成功的匹配
#         return False
#     return True


print(f"使用re的avoid：{avoids_re('abc', '.')}")


'''若直接使用 [forbidden] ，虽然可以表示一个
字符集合的正则表达式模式，但是，当 forbidden 中包含特殊字符时会出现问题。
例如，如果 forbidden 的值是 '.'，那么使用 [forbidden] 表示的就是匹配任意字符的
正则表达式模式，而不是匹配 '.' 字符。

将 forbidden 插入到一个字符串格式化的占位符中，可以使得特殊
字符在使用前被正确地转义。'''


# 编写函数 useonly ，接收一个单词和一个含有允许字母的字符串，判断
# 该单词是否仅仅由允许字母组成。

def useonly(word, allowed):
    for i in word:
        if i not in allowed:
            return False
    return True


print(f"useonly：{useonly('abc', 'a')}")

# 使用列表推导式编写useonly函数
# def useonly(word, allowed):
#     return False if [i for i in word if i not in allowed] else True


# 使用re编写useonly_re函数


def useonly_re(word, allowed):
    if re.search(r'[^%s]' % allowed, word):  # []表示字符集合，[^]表示非字符集合
        return False
    return True


print(f"使用re的useonly：{useonly_re('abc', 'a')}")


# 编写函数 useall ，接收一个单词和一个含有需要字母的字符串，判断该
# 单词是否包含了所有需要字母至少一个，并输出words.txtwords.txt中使用了所有
# 元音字中使用了所有元音字母母aeiouaeiou的单词。的单词。

def useall(word, need):
    for i in need:
        if i not in word:
            return False
    return True


# 使用列表推导式编写useall

# def useall(word,need):
#     return False if [i for i in need if i not in word] else True


print(f"useall：{useall('abc', 'ab')}")


# 使用re编写useall_re函数


def useall_re(word, need):
    for i in need:
        if not re.search(i, word):
            return False
    return True


print(f"使用re的useall：{useall_re('abc', 'ab')}")


# ）编写函数 hasnoe ，判断一个英语单词是否包含字母 e ，并计算

def hasnoe(word):
    if 'e' in word:
        return False
    return True


print(f"hasnoe：{hasnoe('abc')}")

# 使用re编写hasnoe_re函数


def hasnoe_re(word):
    if re.search(r'e', word):
        return False
    return True


print(f"使用re的hasnoe：{hasnoe_re('abc')}")


# 使用hasnoe计算 words.txt中不含 e 的单词在整个字母表中的百分比。


def hasnoe_percent():
    with open('lab-3/sublab-5/words.txt') as fin:
        count = 0
        total = 0
        for line in fin:
            word = line.strip()
            total += 1
            if hasnoe(word):
                count += 1
        # 计算单词总数
        print(f"单词总数：{total}")
        print(f"不含e的单词总数：{count}")
        return count/total


# print(hasnoe_percent())
print(f"hasnoe_percent：{hasnoe_percent()}")


# ）编写函数 isabecedarian ，判断一个英语单词中的字母是否符合字母表序
# 并且输出 words.txt 中所有这样的单词。

def isabecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True


def isabecedarian_words():
    with open('lab-3/sublab-5/words.txt') as fin:
        result = []
        for line in fin:
            word = line.strip()
            if isabecedarian(word):
                # print(word)
                result.append(word)
        return result


print(f"words.txt中符合字母表序的单词：{isabecedarian_words()}")
print(f"words.txt中符合字母表序的单词总数：{len(isabecedarian_words())}")
