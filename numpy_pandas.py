import numpy as np
import array
import random
import pandas as pd
import calendar


'''
    numpy 和 pandas的学习
'''
class numpy_pandas:
################# NUMPY类型 ################################
    def __init__(self):
         '''
            np.zeros_like(a) 复制一份和 a 一样但是值为 0 矩阵
            np.ones_like(a) 复制一份和 a 一样但是值为 1 矩阵
            np.full_like(a,value,dtype) 复制一份和 a 一样但是值为 value 并且类型为 dtype的 矩阵
         '''

    #打印某一年的日历
    def get_year_date(year):
        print("以下是{year}年的日历".format(year=year))
        textcal = calendar.TextCalendar()
        aa = textcal.pryear(year)
        print(aa)

    get_year_date(2500)

    #将列表转换为数组
    def table_to_list(table):
        a_list = list(table)
        b = np.array(a_list)
        print(b)
        return b

    #生成 a*b并且值全部为 0 以及类型为 dtype 矩阵
    def create_zeros_matrix(a,b,dtype):
        a = np.zeros((a,b) , dtype=dtype)
        print(a)

    #生成 a*b并且值全部为 1 以及类型为 dtype 矩阵
    def create_ones_matrix(a,b,dtype):
        b = np.ones((a,b),dtype)
        print(b)

    ##生成 a*b并且值全部为 value 矩阵
    def create_value_matrix(a,b,value):
        a = np.full((a,b),value)
        print(a)

    #生成a*b并且值为 小于 1 的随机数 的矩阵
    def random_matrix(a,b):
        b = np.random.random(a,b)
        print(b)

    ##生成a*b并且值为 0-10的随机整数 的矩阵
    def random_int_matrix(a,b):
        c = np.random.randint(0,10 ,(a,b))
        print(c)

    #获取 a-b中间的所有的 偶数值  左闭右开
    def get_even_num(a,b):
        a = list(range(a,b,2))
        print(a)

    #获取 a-b中间的所有的 偶数值  左闭右开
    def get_arange_num(a,b):
        a = np.arange(a,b,2)
        print(a)

    #将a至b的分成平均的 c  等分   a,b可以为浮点型   c必须为int 类型
    def get_num_lin(a,b,c):
        a = np.linspace(a,b,c)
        print(a)

    #生成行数对应的位置 为1  其他全为 0 的a 次 矩阵
    def get_eye_nums(a):
        a = np.eye(a)
        print(a)

    #访问arr(arr为多维数组) 数组中第 a 行 ， 第 b列的元素
    def get_element(arr,a,b):
       a = arr[a,b]
       b = arr[a][b]
       print(a)
       print(b)
    '''
        访问数组时：
        arr[a,b] 等价于 arr[a][b]
        数组切片
        arr[:a][:b] 不等价于  arr[:a,:b]
    '''
    '''
        统计类型
    '''
    #数组求和
    def arr_sum(arr):
        a = sum(arr)
        print(a)

    #数组变形   将arr数组变成 a 行 b 列的一个新的数组
    def arr_reshape(arr,a,b):
        a = arr.reshape(a,b)
        print(a)
    '''
        排序函数
            np.sort(arr)
        拼接函数
            按行去连接
                np.concatenate([b,b,b],axis=0)
            按列去连接
                np.concatenate([b,b,b],axis=1)
    '''
################### PANDAS类型  #######################################
    #读取 csv 文件
    def get_csv(csv_path):
        df = pd.read_csv(csv_path)
        return df

    # read_csv("C:/Users/HASEE/Desktop/python/test.csv")

    #获取csv的前 n 条数据 n为整数
    def get_csv_head(csv_path ,n):
        df = pd.read_csv(csv_path)
        print(df.head(n))
        return df.head(n)

    #get_csv_head("C:/Users/HASEE/Desktop/python/test.csv",4)

    #获取DataFrame 的列名  以及索引
    def get_df_columns(csv_path):
        df = pd.read_csv(csv_path)
        colums = df.columns
        index = df.index
        dric = {
            "colums" : colums,
            "index" :index
        }
        print(dric)
        return dric

    #get_df_columns("C:/Users/HASEE/Desktop/python/test.csv")

    #获取csv 第 n+1行数据  n为整数
    def get_line_data(csv_path,n):
        df = pd.read_csv(csv_path)
        a = df.loc[n]
        print(a)
        return a

    #get_line_data("C:/Users/HASEE/Desktop/python/test.csv",2)

    #筛选 数学 大于  num 的数据   返回一个新的df
    '''
        复杂筛选
        df[df.数学 > num & df.语文 > num &df.物理 > num]
    '''
    def sel_df_data(csv_path,colums_data,num):
        df = pd.read_csv(csv_path)
        df = df[df.数学 > num]
        print(df)
        return df

    #sel_df_data("C:/Users/HASEE/Desktop/python/test.csv","数学",95)


    #对df根据 colums_arr 进行排序  然后获取前n+1行  colums_arr是一个 []  如['数学'，'语文']
    def df_sort(csv_path,colums_arr,n):
        df = pd.read_csv(csv_path)
        df = df.sort_values(colums_arr).head(n)
        print(df)
        return df

    #df_sort("C:/Users/HASEE/Desktop/python/test.csv",["数学","语文"],5)


    #获取di n+1 行数据
    def line_df(csv_path, n):
        df = pd.read_csv(csv_path)
        df = df.loc[n]
        print(df)
        return df

    #line_df("C:/Users/HASEE/Desktop/python/test.csv",5)

    '''
        改变索引
            pd.DataFrame(df,index=['one','two','three'])
        注意：当改完索引之后  再通过索引访问时，应该使用新的索引   df.loc['one']     但是此时仍然通过 df.iloc[0] 访问 
        df.ix[0]  合并了   df.loc['one'] 和 df.iloc[0] 的功能   当索引值为数字时  结果为 df.loc[] 的值    不然则为  df.iloc[]  的值
        此处不再加以演示
    '''

    #根据 某列统计数据
    def get_counts(csv_path):
        df = pd.read_csv(csv_path)
        df = df.数学.value_counts()
        print(df)
        return df

    #get_counts("C:/Users/HASEE/Desktop/python/test.csv")

    #提取 colums_arr 的 前 n 行数据   colums_arr  可为数组
    def get_colums_data(csv_path,colums_arr,n):
        df = pd.read_csv(csv_path)
        df = df[colums_arr].head(n)
        print(df)
        return df

    #get_colums_data("C:/Users/HASEE/Desktop/python/test.csv",["姓名","数学","语文"],5)

    #根据  数学  分类
    def classify(score):
        if score ==100:
            return "天才"
        elif score>=90:
            return "优秀"
        elif score>=70:
            return "良好"
        elif score>=60:
            return "及格"
        else:
            return "不及格"

    df =get_csv("C:/Users/HASEE/Desktop/python/test.csv")
    #df["数学分类"] = df.数学.map(classify)
    #print(df)

    #在原基础上加上 值
    def add_df(number):
        return number + 10

    #等价于

    add_df = lambda number : number + 10

    #df.applymap(lambda x : str(x) + '-')

    #根据多列生成新的一个列的操作   用apply
    df["数学+英语+语文的总分"] = df.apply(lambda x:x.数学+x.语文+x.英语,axis = 1)

    #最后几行
    print(df.tail(3))
    #前几行
    print(df.head(3))
