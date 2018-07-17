import re

print("---------匹配单个字符与数字-----------")

'''

   .            匹配除换行符以外的任意字符
 [0123456789]   []是字符集合, 表示匹配方括号中所包含的任意一个字符
 [turo]         匹配't', 'u', 'r', 'o' 中任意一个字符
 [a-z]          匹配任意小写字母
 [A-Z]          匹配任意大写字母
 [0-9]          匹配任意数字, 类似[0123456789]
 [0-9a-zA-Z]    匹配任意的数字和字母
 [0-9a-zA-Z_]   匹配任意的数字、字母和下划线
 [^turo]        匹配除了't', 'u', 'r', 'o' 以外的所有字符,
                    中括号里的 ^ 称为脱字符, 表示不匹配集合中的字符
 [^0-9]         匹配所有的非数字字符
    \d          匹配数字, 效果同[0-9]
    \D          匹配非数字字符, 效果如同[^0-9]
    \w          匹配数字, 字母和下划线, 效果同[0-9a-zA-Z_]
                    (用来判断标识符)
    \W          匹配非数字字母和下划线, 效果同[^0-9a-zA-Z_]
    \s          匹配任意的空白符(空格, 换行, 回车, 换页, 制表)
                    效果同[ \f\n\r\t] (其中开始的空格就是空格符)
    \S          匹配任意的非空白符, 效果同[^ \f\n\r\t]
'''

# print(re.search(".", "turo is a good man"))
# print(re.search("[0123456789]", "turo is a goo5d man"))
# print(re.search("[turo]", "turo is a goo5d man"))
# print(re.search("[^turo]", "turo is a goo5d man"))
# print(re.findall("\d", "_turo is a goo5d man"))


print("---------------锚字符(边界字符)---------------")


'''
 ^      行首匹配, 和在[]里的 ^ 不是一个意思
 $      行尾匹配

 \A     匹配字符串开始, 它和 ^ 的区别是, \A只匹配整个字符串的开头,
            即时在re.M模式下, 它也不会匹配它行的行首
 \Z     匹配字符串结束, 和 $ 的区别, \Z 只匹配整个字符串的结束,
            即时在re.M模式下, 也不会匹配它行的行尾

 \b     匹配一个单词的边界, 也就是指单词和空格间的位置
            'er\b'可以匹配never, 不能匹配nerve
 \B     匹配非单词边界
'''

# print(re.search("turo$", "turo is a good man turo"))
# print(re.search("^turo$", "turo"))

# print(re.search("^turo is a good man turo$", "turo is a good man turo"))
# print(re.search("\Aturo", "turo is a good man turo"))

# print(re.findall("\Aturo", "turo is a good man turo\nturo is a good man", re.M))
# print(re.findall("^turo", "turo is a good man turo\nturo is a good man", re.M))

# print(re.findall("man\Z", "turo is a good man\nturo is a good man", re.M))
# print(re.findall("man$", "turo is a good man\nturo is a good man", re.M))

# print(re.search(r"er\b", "never"))
# print(re.search(r"er\b", "nerve"))
# print(re.search(r"er\B", "never"))
# print(re.search(r"er\B", "nerve"))

print("--------------匹配多个字符-----------------")

'''
说明: 下方的x、 y、 z 均为假设的普通字符, n、m 非负整数， 不是正则表达式的元字符

(xyz)   匹配小括号内的xyz(作为一个整体去匹配)
x?      匹配0个或1个x
x*      匹配0个或任意多个x(.* 表示匹配0个或者任意多个字符(换行符除外))
x+      匹配至少一个x
x{n}    匹配确定的n个x(n是一个非负整数)
x{n,}   匹配至少n个x
x{n,m}  匹配至少n个最多m个x。 注意:n<=m
x|y     | 表示或, 匹配的是 x 或 y
'''
# print(re.findall(r"(turo)", "turo is a good man"))
# print(re.findall(r"a?", "aaa"))#非贪婪匹配(尽可能少的匹配)
# print(re.findall(r"a*", "aaabaa"))#贪婪匹配(尽可能多的匹配)
# print(re.findall(r"(.*)", "aaabaa"))
# print(re.findall(r"a+", "aaaaa"))#贪婪匹配(尽可能多的匹配)
# print(re.findall(r"a{3}", "aaaabaabaaa"))
# print(re.findall(r"a{3,}", "aaaabaabaaa"))
# print(re.findall(r"a{3,6}", "aaaabaabaaaaaaaa"))
# print(re.findall(r"((T|t)uro)", "turo-Turo"))



#需求: 提取 turo ........ man.
str = "turo is a good man! turo is a nice man! turo is a very handsome man"
# print(re.findall(r"(^turo.*man$)", str))
# print(re.findall(r"(^turo(.*?)man$)", str))未解决
# print(re.findall(r"(turo.*?man)", str))


print("--------------特殊--------------")
'''
*?  +?  x?   最小匹配, 通常都是尽可能多的匹配, 可以使用这种方式解决贪婪匹配

(?:x)        类似(xyz), 但不表示一个组
'''
#注释: /* part1 */    /* part2 */
# print(re.findall(r"//*.*/*/", r"/* part1 */    /* part2 */"))
# print(re.findall(r"//*.*?/*/", r"/* part1 */    /* part2 */"))
