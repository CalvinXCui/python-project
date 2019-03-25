import this
print("jvm的基本原理以及运行机制")
'''
    python异常
'''
try:
    fh = open("testfile", "w",encoding="utf-8")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
'''
语法：
    try:
        正常的操作
       ......................
    except(Exception1[, Exception2[,...ExceptionN]]]):
       发生以上多个异常中的一个，执行这块代码
       ......................
    else:
        如果没有异常执行这块代码
try...finally语法
    try:
    <语句>
    finally:
    <语句>    #退出try时总会执行
    raise
'''
'''
    os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：
    
         序号	                                                        方法及描述
         
1	os.access(path, mode)                           检验权限模式
2	os.chdir(path)                                  改变当前工作目录
3	os.chflags(path, flags)                         设置路径的标记为数字标记。
4	os.chmod(path, mode)                            更改权限
5	os.chown(path, uid, gid)                        更改文件所有者
6	os.chroot(path)                                 改变当前进程的根目录
7	os.close(fd)                                    关闭文件描述符 fd
8	os.closerange(fd_low, fd_high)                  关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9	os.dup(fd)                                      复制文件描述符 fd
10	os.dup2(fd, fd2)                                将一个文件描述符 fd 复制到另一个 fd2
11	os.fchdir(fd)                                   通过文件描述符改变当前工作目录
12	os.fchmod(fd, mode)                             改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13	os.fchown(fd, uid, gid)                         修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14	os.fdatasync(fd)                                强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15	os.fdopen(fd[, mode[, bufsize]])                通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16	os.fpathconf(fd, name)                          返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17	os.fstat(fd)                                    返回文件描述符fd的状态，像stat()。
18	os.fstatvfs(fd)                                 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
19	os.fsync(fd)                                    强制将文件描述符为fd的文件写入硬盘。
20	os.ftruncate(fd, length)                        裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21	os.getcwd()                                     返回当前工作目录
22	os.getcwdu()                                    返回一个当前工作目录的Unicode对象
23	os.isatty(fd)                                   如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24	os.lchflags(path, flags)                        设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25	os.lchmod(path, mode)                           修改连接文件权限
26	os.lchown(path, uid, gid)                       更改文件所有者，类似 chown，但是不追踪链接。
27	os.link(src, dst)                               创建硬链接，名为参数 dst，指向参数 src
28	os.listdir(path)                                返回path指定的文件夹包含的文件或文件夹的名字的列表。
29	os.lseek(fd, pos, how)                          设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30	os.lstat(path)                                  像stat(),但是没有软链接
31	os.major(device)                                从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32	os.makedev(major, minor)                        以major和minor设备号组成一个原始设备号
33	os.makedirs(path[, mode])                       递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34	os.minor(device)                                从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35	os.mkdir(path[, mode])                          以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36	os.mkfifo(path[, mode])                         创建命名管道，mode 为数字，默认为 0666 (八进制)
37	os.mknod(filename[, mode=0600, device])         创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
38	os.open(file, flags[, mode])                    打开一个文件，并且设置需要的打开选项，mode参数是可选的
39	os.openpty()                                    打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40	os.pathconf(path, name)                         返回相关文件的系统配置信息。
41	os.pipe()                                       创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42	os.popen(command[, mode[, bufsize]])            从一个 command 打开一个管道
43	os.read(fd, n)                                  从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44	os.readlink(path)                               返回软链接所指向的文件
45	os.remove(path)                                 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
46	os.removedirs(path)                             递归删除目录。
47	os.rename(src, dst)                             重命名文件或目录，从 src 到 dst
48	os.renames(old, new)                            递归地对目录进行更名，也可以对文件进行更名。
49	os.rmdir(path)                                  删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
50	os.stat(path)                                   获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
51	os.stat_float_times([newvalue])                 决定stat_result是否以float对象显示时间戳
52	os.statvfs(path)                                获取指定路径的文件系统统计信息
53	os.symlink(src, dst)                            创建一个软链接
54	os.tcgetpgrp(fd)                                返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
55	os.tcsetpgrp(fd, pg)                            设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
56	os.tempnam([dir[, prefix]])                     返回唯一的路径名用于创建临时文件。
57	os.tmpfile()                                    返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
58	os.tmpnam()                                     为创建一个临时文件返回一个唯一的路径
59	os.ttyname(fd)                                  返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
60	os.unlink(path)                                 删除文件路径
61	os.utime(path, times)                           返回指定的path文件的访问和修改的时间。
62	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])    输出在文件夹中的文件名通过在树中游走，向上或者向下。
63	os.write(fd, str)                                                    写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
64	os.path 模块                                                         获取文件的属性信息。
'''
"""
    内置函数
    
        abs( x )                                    返回数字的绝对值。
        divmod(a, b)                                把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        input()                                     接受一个标准输入数据，返回为 string 类型。
        open()                                      用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
        staticmethod                                返回函数的静态方法。
        all()                                       用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
        enumerate()                                 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        int()                                       用于将一个字符串或数字转换为整型。
        ord()                                       chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
        str()                                       将对象转化为适于人阅读的形式。
        any()                                       用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。元素除了是 0、空、FALSE 外都算 TRUE
"""
'''
    类
    语法：
    class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体
'''
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print(  "Name : ", self.name, ", Salary: ", self.salary)

    def get_employee(self,name,age,*args,**kwargs):
        print(name,age,*args,**kwargs)

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp2.get_employee("wong",20,300,"研发",[1,23,65,98,12])
print("Total Employee %d" % Employee.empCount)
'''
    数据库的操作
        mysql -u root -p u是用户名 p：需要密码登陆数据库
        show databases 查看数据库
        use databases_name 选择数据库
        show tables 查看数据库中的table 表
        desc tables  查看表格的结构
        select * from table_name 查看表中的数据  
'''
#对json的操作
import json;
'''
    方法	描述
        json.dumps()	将 Python 对象编码成 JSON 字符串
        json.loads()	将已编码的 JSON 字符串解码为 Python 对象
        json.dump()	    将Python内置类型序列化为json对象后写入文件
        json.load()	    读取文件中json形式的字符串元素转化为Python类型
'''
json_data = {
    "name":"张三13213123122",
    "age":25,
    "sex":"男"
}

# json串是一个字符串
res = json.dumps(json_data)# 把json串，变成python的数据类型，只能转换json串内容
product_dic = json.loads(res)
print(product_dic)

