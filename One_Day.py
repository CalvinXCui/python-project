""" 
    Python中的所有的关键字  全部为小写  共30个
        and	exec	not
        assert	finally	or
        break	for	pass
        class	from	print
        continue	global	raise
        def	if	return
        del	import	try
        elif	in	while
        else	is	with
        except	lambda	yield
"""
print("你好啊")
print ('hello');print ('runoob')
#判断
if True:
    print ("True")
    print("Answer")
else:
  print ("False")
  print("Answer")

#
print("aaasadasfaf1233")
#定义变量
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)#打印变量
'''
   多行注释  采用三个单引号 或者三个双引号
'''

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
"""
    在Python当中一共有5中数据类型:
        Numbers（数字）
        String（字符串）
        List（列表）
        Tuple（元组）
        Dictionary（字典）
"""
print(counter),print(miles),print(name)
d = f = g = 1
print("d+f+g={}".format(d+f+g))
a= "a1b2c3d4f5"
#截取字符串  下标为两种  一种是从左到右依次为：0，1，2，3，4.....    一种是从右到左以此为：-1，-2，-3，-4.....
b,c=a[1:6],a[-7:-2]
print("a的值为:"+a),print("b的值为:"+b),print("c的值为:"+c),print("将c的值输出两次为:"+c*2)
print("a的第一个字母为:"+a[0]),print("a的第四个字符以后的为:"+a[3:]),print("截取a的第二个字符到第八个字符中的步长的字符串:"+a[1:7:4])

str = '0123456789'
print ("截取第一位到第三位的字符"+str[0:3]) #截取第一位到第三位的字符
print ("截取字符串的全部字符"+str[:]) #截取字符串的全部字符
print ("截取第七个字符到结尾"+str[6:]) #截取第七个字符到结尾
print ("截取从头开始到倒数第三个字符之前"+str[:-3]) #截取从头开始到倒数第三个字符之前
print ("截取第三个字符"+str[2]) #截取第三个字符
print ("截取倒数第一个字符"+str[-1]) #截取倒数第一个字符
print ("创造一个与原字符串顺序相反的字符串"+str[::-1]) #创造一个与原字符串顺序相反的字符串
print ("截取倒数第三位与倒数第一位之前的字符"+str[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
print ("截取倒数第三位到结尾"+str[-3:]) #截取倒数第三位到结尾
print ("逆序截取，具体啥意思没搞明白"+str[:-5:-3]) #逆序截取，具体啥意思没搞明白？

##############集合练习
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list)# 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

#############元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
print(tuple)

#############字典   其实在我看来特就是java中的map集合
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict['one'] = "This is one"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])# 输出键为'one' 的值
print(dict[2])# 输出键为 2 的值
print(tinydict)# 输出完整的字典
print(tinydict.keys())# 输出所有键
print(tinydict.values())# 输出所有值

###########运算符
'''
1、算术运算符
    加减乘除一样  就不多说了 
       看看其他的
          **	幂 - 返回x的y次幂
          //	取整除 - 返回商的整数部分（向下取整）
          注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
2、比较运算符
    比较运算符和其他语言基本一致  在这里就不再多说
         ==	等于 - 比较对象是否相等
         !=	不等于 - 比较两个对象是否不相等
         <>	不等于 - 比较两个对象是否不相等 这个运算符类似 !=
         >	大于 - 返回x是否大于y
         <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价
         >=	大于等于	- 返回x是否大于等于y
         <=	小于等于 -	返回x是否小于等于y
3、赋值运算符
    赋值运算符也和其它语言的基本一致
         =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
         +=	加法赋值运算符	c += a 等效于 c = c + a
         -=	减法赋值运算符	c -= a 等效于 c = c - a
         *=	乘法赋值运算符	c *= a 等效于 c = c * a
         /=	除法赋值运算符	c /= a 等效于 c = c / a
         %=	取模赋值运算符	c %= a 等效于 c = c % a
         **=	幂赋值运算符	c **= a 等效于 c = c ** a
         //=	取整除赋值运算符	c //= a 等效于 c = c // a
4、按位运算符 （感觉不怎么用，最起码java中很少用  所以这里不做过多介绍）
        &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
        |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
        ^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
        ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011，在一个有符号二进制数的补码形式。
        <<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
        >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
5、逻辑运算符
        and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
        or	x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
        not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
6、成员运算符
        in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
        not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
7、身份运算符
        is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
        is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
    
'''
print(2**3)# 幂 - 返回x的y次幂   结果应该是8
print(9//2)# 取整除 - 返回商的整数部分（向下取整） 结果应该是4

aa = 10
bb = 20
list = [1, 2, 3, 4, 5];
if (aa in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (bb not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
aa = 2
if (aa in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")
#身份运算符
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")
if (a is not b):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print( "3 - a 和 b 没有相同的标识")
if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
"""
    运算符优先级
        **	指数 (最高优先级)
        ~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
        * / % //	乘，除，取模和取整除
        + -	加法减法
        >> <<	右移，左移运算符
        &	位 'AND'
        ^ |	位运算符
        <= < > >=	比较运算符
        <> == !=	等于运算符
        = %= /= //= -= += *= **=	赋值运算符
        is is not	身份运算符
        in not in	成员运算符
        not and or	逻辑运算符
"""
"""
     条件语句
        if 判断条件1:
            执行语句1……
        elif 判断条件2:
            执行语句2……
        elif 判断条件3:
            执行语句3……
        else:
            执行语句4……
"""
"""
    循环语句
       Python提供了for循环和while循环（在Python中没有do..while循环）:
            while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
            for 循环	重复执行语句
            嵌套循环	你可以在while循环体中嵌套for循环
    循环控制语句
        break 语句	在语句块执行过程中终止循环，并且跳出整个循环
        continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
        pass 语句	pass是空语句，是为了保持程序结构的完整性。
"""
nums = [12,37,5,42,65]
even=[]
odd=[]
while len(nums) > 0 :
    num = nums.pop()
    if(num % 2 == 0) :
        even.append(num)
    else:
        odd.append(num)
print(even),print(odd)

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')

for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)

for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)

####列表(List)
  ###访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
 ###更新列表
list = []  ## 空列表
list.append('Google')  ## 使用 append() 添加元素
list.append('Runoob')
print(list)
 ###删除列表元素
list3 = ['physics', 'chemistry', 1997, 2000]
del list3[2]
print(list3)
'''
    列表脚本操作符
        len([1, 2, 3])	3	长度
        [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
        ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
        3 in [1, 2, 3]	True	元素是否存在于列表中
        for x in [1, 2, 3]: print x,	1 2 3	迭代
        List[1:] 从第二个元素开始截取列表 返回一个新的集合
        
        1	cmp(list1, list2)       比较两个列表的元素
        2	len(list)               列表元素个数
        3	max(list)               返回列表元素最大值
        4	min(list)               返回列表元素最小值
        5	list(seq)               将元组转换为列表
        1	list.append(obj)        在列表末尾添加新的对象
        2	list.count(obj)         统计某个元素在列表中出现的次数
        3	list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        4	list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
        5	list.insert(index, obj) 将对象插入列表
        6	list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        7	list.remove(obj)        移除列表中某个值的第一个匹配项
        8	list.reverse()          反向列表中元素
        9	list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序
        
   元组
       访问元组
            tup1 = ('physics', 'chemistry', 1997, 2000)
            tup2 = (1, 2, 3, 4, 5, 6, 7 )
             
            print "tup1[0]: ", tup1[0]
            print "tup2[1:5]: ", tup2[1:5]
       修改元组
            元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
                tup1 = (12, 34.56)
                tup2 = ('abc', 'xyz')
                 
                # 以下修改元组元素操作是非法的。
                # tup1[0] = 100
                 
                # 创建一个新的元组
                tup3 = tup1 + tup2
       删除元组
           元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
           tup = ('physics', 'chemistry', 1997, 2000)
           del tup
       元组索引，截取
            L = ('spam', 'Spam', 'SPAM!')
            L[2]	'SPAM!'	读取第三个元素
            L[-2]	'Spam'	反向读取，读取倒数第二个元素
            L[1:]	('Spam', 'SPAM!')	截取元素
       任意无符号的对象，以逗号隔开，默认为元组，如下实例：
            print 'abc', -4.24e93, 18+6.6j, 'xyz'
            x, y = 1, 2
            print "Value of x , y : ", x,y
          以上实例运行结果：
             abc -4.24e+93 (18+6.6j) xyz
             Value of x , y : 1 2
       元组内置函数      
           1	cmp(tuple1, tuple2)     比较两个元组元素。
           2	len(tuple)              计算元组元素个数。
           3	max(tuple)              返回元组中元素最大值。
           4	min(tuple)              返回元组中元素最小值。
           5	tuple(seq)              将列表转换为元组。
'''
'''
    字典(Dictionary)  和java中的map差不多   所以  我就在这里不多说   只说几个个别方法
         删除字典  
            能删单一的元素也能清空字典，清空只需一项操作
            dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
            del dict['Name']  # 删除键是'Name'的条目
            dict.clear()      # 清空词典所有条目
            del dict          # 删除词典
    字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
       两个重要的点需要记住：
            1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
            2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
    字典内置函数&方法
            1	cmp(dict1, dict2)       比较两个字典元素。
            2	len(dict)               计算字典元素个数，即键的总数。
            3	str(dict)               输出字典可打印的字符串表示。
            4	type(variable)          返回输入的变量类型，如果变量是字典就返回字典类型。
            1	dict.clear()            删除字典内所有元素
            2	dict.copy()             返回一个字典的浅复制
            3	dict.fromkeys(seq[, val])创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
            4	dict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
            5	dict.has_key(key)           如果键在字典dict里返回true，否则返回false
            6	dict.items()                以列表返回可遍历的(键, 值) 元组数组
            7	dict.keys()                 以列表返回一个字典所有的键
            8	dict.setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
            9	dict.update(dict2)                  把字典dict2的键/值对更新到dict里
            10	dict.values()                       以列表返回字典中的所有值
            11	pop(key[,default])                  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
            12	popitem()                           随机返回并删除字典中的一对键和值。
'''
ss = input("请输入值")
print("您输入值为:{}".format(ss))