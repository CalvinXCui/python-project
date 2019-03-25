'''python 第二天'''
# -*- coding: UTF-8 -*-
import  time
import calendar
import math
import os
import locale

'''时间'''
ticks = time.time();#时间戳
print(ticks)
localtime = time.localtime(time.time());#本地时间的元组
print(localtime)
localtime2 = time.asctime( time.localtime(time.time()))#获取格式化的时间
print(localtime2)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
print(time.mktime(time.strptime(localtime2, "%a %b %d %H:%M:%S %Y")))
"""日历"""
cal = calendar.month(2500, 1)
print("以下输出2019年1月份的日历:")
print(cal)

print(calendar.isleap(2019))#判断是否是闰年
print(calendar.leapdays(1994,2019))#返回在Y1，Y2两年之间的闰年总数
"""函数"""
def firstfunction(ss):
    return ss;
'''
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
      不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
      可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
      
      不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
      可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
'''

# 调用changeme函数
mylist = [10, 20, 30];
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return

print("初始值: ", mylist)
changeme(mylist);
print("函数外取值: ", mylist)
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print("Name: ", name);
   print("Age ", age);
   return;
#调用printinfo函数
printinfo( age=50, name="miki" );#只要关键字确定了  顺序就可以随便了
#可写函数说明
def printinfo1( name, age = 35 ):#35为age的默认值   如果当age没有传入  就默认为35
   "打印任何传入的字符串"
   print("Name: ", name);
   print("Age ", age);
   return;
printinfo1(name="xiaocui");
printinfo1(age=60,name="calvin");
printinfo1("CalvinXCui",55);
'''动态的参数个数'''
# 可写函数说明
def printinfo2( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;
printinfo2(20);
printinfo2(60,80,90,"dsada")
"""
    匿名函数python 使用 lambda 来创建匿名函数
        语法：lambda [arg1 [,arg2,.....argn]]:expression
"""
# 可写函数说明
sum = lambda arg1, arg2: arg1 *arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
'''返回值return'''


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total;
# 调用sum函数
total = sum(10, 20);
#dir() dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
#返回的列表容纳了在一个模块里定义的所有模块，变量和函数
content = dir(math)
print(content);
print(globals());
print(locals());
'''
    Python 文件I/O
        不同模式打开文件的完全列表：
        模式	描述
        t	文本模式 (默认)。
        x	写模式，新建一个文件，如果该文件已存在则会报错。
        b	二进制模式。
        +	打开一个文件进行更新(可读可写)。
        U	通用换行模式（不推荐）。
        r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
        r+	打开一个文件用于读写。文件指针将会放在文件的开头。
        rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
        w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
        w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
        a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
        a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''
#input("Python 是一个非常棒的语言，不是吗？")
"""
file object = open(file_name [, access_mode][, buffering])
各个参数的细节如下：
file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
                          
                           模式	        r	r+	w	w+	a	a+
                           读	        +	+		+		+
                           写		    +	+	+	+	+
                           创建			+	+	+	+
                           覆盖			+	+		
                           指针在开始	+	+	+	+		
                           指针在结尾					+	+
"""
fo = open("foo.txt", mode="w",encoding="utf-8")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
fo.write("我是新写入的文件\n")
fo.write( "www.runoob.com!\nVery good site!\n")
fo.close()
'''
read()方法
read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字
'''
foo = open("foo.txt", mode="r+",encoding="utf-8")
print("读取的文件的内容为"+foo.read())
foo.close()
'''
    文件定位
    tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。
    seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
    如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置
'''
# 打开一个文件
fo = open("foo.txt", mode="r+",encoding="utf-8")
str = fo.read()
print("读取的字符串是 : ", str)
# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
'''
    重命名和删除文件
    Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
    要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。
    rename()方法：
    rename()方法需要两个参数，当前的文件名和新文件名。
    语法：
    os.rename(current_file_name, new_file_name)
    remove()方法
    你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
    语法：
    os.remove(file_name)
'''
# 重命名文件test1.txt到test2.txt。
#os.rename("foo.txt", "fooo.txt")
"""
    Python里的目录：
    所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。
    mkdir()方法
    可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
    语法
    os.mkdir("newdir")
"""
# 创建目录test
#os.mkdir("newdir")
'''
    chdir()方法
    可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
    语法：
    os.chdir("newdir")
'''
os.chdir("newdir")
'''
    getcwd()方法：
    getcwd()方法显示当前的工作目录。
    语法：
    os.getcwd()
'''
print(os.getcwd())
'''
    rmdir()方法
    rmdir()方法删除目录，目录名称以参数传递。
    在删除这个目录之前，它的所有内容应该先被清除。
    语法：
    os.rmdir('dirname')
'''
#os.rmdir( "newdir")
'''
    Python File(文件) 方法
    open() 方法
    Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
    注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
    open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
    open(file, mode='r')
    完整的语法格式为：
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    参数说明:
    file: 必需，文件路径（相对或者绝对路径）。
    mode: 可选，文件打开模式
    buffering: 设置缓冲
    encoding: 一般使用utf8
    errors: 报错级别
    newline: 区分换行符
    closefd: 传入的file参数类型
    opener:
    mode 参数有：
    模式	描述
    t	文本模式 (默认)。
    x	写模式，新建一个文件，如果该文件已存在则会报错。
    b	二进制模式。
    +	打开一个文件进行更新(可读可写)。
    U	通用换行模式（不推荐）。
    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
    默认为文本模式，如果要以二进制模式打开，加上 b
'''
'''
    Python 异常处理
    python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。
    异常处理: 本站Python教程会具体介绍。
    断言(Assertions):本站Python教程会具体介绍。
    python标准异常
    异常名称	描述
    BaseException	所有异常的基类
    SystemExit	解释器请求退出
    KeyboardInterrupt	用户中断执行(通常是输入^C)
    Exception	常规错误的基类
    StopIteration	迭代器没有更多的值
    GeneratorExit	生成器(generator)发生异常来通知退出
    StandardError	所有的内建标准异常的基类
    ArithmeticError	所有数值计算错误的基类
    FloatingPointError	浮点计算错误
    OverflowError	数值运算超出最大限制
    ZeroDivisionError	除(或取模)零 (所有数据类型)
    AssertionError	断言语句失败
    AttributeError	对象没有这个属性
    EOFError	没有内建输入,到达EOF 标记
    EnvironmentError	操作系统错误的基类
    IOError	输入/输出操作失败
    OSError	操作系统错误
    WindowsError	系统调用失败
    ImportError	导入模块/对象失败
    LookupError	无效数据查询的基类
    IndexError	序列中没有此索引(index)
    KeyError	映射中没有这个键
    MemoryError	内存溢出错误(对于Python 解释器不是致命的)
    NameError	未声明/初始化对象 (没有属性)
    UnboundLocalError	访问未初始化的本地变量
    ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
    RuntimeError	一般的运行时错误
    NotImplementedError	尚未实现的方法
    SyntaxError	Python 语法错误
    IndentationError	缩进错误
    TabError	Tab 和空格混用
    SystemError	一般的解释器系统错误
    TypeError	对类型无效的操作
    ValueError	传入无效的参数
    UnicodeError	Unicode 相关的错误
    UnicodeDecodeError	Unicode 解码时的错误
    UnicodeEncodeError	Unicode 编码时错误
    UnicodeTranslateError	Unicode 转换时错误
    Warning	警告的基类
    DeprecationWarning	关于被弃用的特征的警告
    FutureWarning	关于构造将来语义会有改变的警告
    OverflowWarning	旧的关于自动提升为长整型(long)的警告
    PendingDeprecationWarning	关于特性将会被废弃的警告
    RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
    SyntaxWarning	可疑的语法的警告
    UserWarning	用户代码生成的警告
    
    try:
    <语句>        #运行别的代码
    except <名字>：
    <语句>        #如果在try部份引发了'name'异常
    except <名字>，<数据>:
    <语句>        #如果引发了'name'异常，获得附加的数据
    else:
    <语句>        #如果没有异常发生
'''
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

