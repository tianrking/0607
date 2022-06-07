
## 1-4

### 什么是Python GIL? Python GIL带来的影响是什么？

    GIL的全称是Global Interpreter Lock(全局解释器锁)，来源是python设计之初的考虑，为了数据安全所做的决定。在一个python进程中，GIL只有一个。拿不到GIL的线程，就不允许进入CPU执行。 据报道说在python3.12后会去掉GIL。
    
### 多任务适用于哪些场景? 
    
    程序出现了重复度高的情况时，比如爬虫、频繁的io读取、计算等操作，为提高效率会选择采用多线程或是多进程

### 在Python语法中，类(class)中的init的作用是什么?在什么时候会执行它?

```Python3
class init_test(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
temp = init_test(1,2) ## temp.value1 为 1 temp.value2 为2 
```
在初始化时候可以利用 init 传入参数，但必须包含一个名为 self 的参数，且必须作为第一个参数，可以当成类的默认构造方法

### 4. 常见的HTTP请求方法有哪些? 各自适用于什么场景?

    1、GET方法
    GET方法用于使用给定的URI从给定服务器中检索信息，即从指定资源中请求数据。使用GET方法的请求应该只是检索数据，并且不应对数据产生其他影响。
    GET请求是可以缓存的，我们可以从浏览器历史记录中查找到GET请求， GET请求有长度限制，仅用于请求数据（不修改）。

    2、POST方法
    POST方法用于将数据发送到服务器以创建或更新资源，它要求服务器确认请求中包含的内容，POST请求不会被缓存，且对数据长度没有限制；我们无法从浏览器历史记录中查找到POST请求。

    3、HEAD方法
    HEAD方法与GET方法相同，但没有响应体，仅传输状态行和标题部分。

    4、PUT方法
    PUT方法用于将数据发送到服务器以创建或更新资源，它可以用上传的内容替换目标资源中的所有当前内容。它会将包含的元素放在所提供的URI下，如果URI指示的是当前资源，则会被改变。如果URI未指示当前资源，则服务器可以使用该URI创建资源。

    5、DELETE方法
    DELETE方法用来删除指定的资源，它会删除URI给出的目标资源的所有当前内容。

## 5-7

### 什么是Python装饰器? 有什么作用? 请实现一个任意功能的装饰器。
在一些函数需要增加新的类似的功能的时候可以利用装饰器来快速实现,本质上就是将函数传入另一个函数 实现功能的增强
比如
def f1():
    print('1')

def f2():
    print('2')

def add_author(func):
    func()
    print("w0x7ce")
f1输出1 f2 输出 2 当我想实现f1 f2  同时打印出作者 可以这样
add_author(f1)
add_author(f2)
换成装饰器就是这样
@add_author
def f1():
    print('1')

@add_author
def f2():
    print('2')
会输出
1
w0x7ce
2
w0x7ce
### 深拷贝和浅拷贝有什么区别? 各有哪些实现方法（请各写一个代码示例）?
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

浅拷贝 
>>> a = {1: [1,2,3]} 
>>> b = a.copy() 
>>> a, b 
({1: [1, 2, 3]}, {1: [1, 2, 3]}) 
>>> a[1].append(4) 
>>> a, b 
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})

深拷贝
>>>import copy 
>>> c = copy.deepcopy(a) 
>>> a, c 
({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]}) 
>>> a[1].append(5)
>>> a, c 
({1: [1, 2, 3, 4, 5]}, {1: [1, 2, 3, 4]})

### fun(*args,**kwargs)中的*args,**kwargs是什么? 请实现一个带有*args或者**kwargs的函数。

args可以当成一个可变参数的数组 
def show_value(*args):
    for value in args:
        print(value)

>>> show_value([1,2])
[1,2]
>>> show_value([1,2,3])
[1,2,3]
Kwargs可以当成一个可变的字典
def show_kwargs(**kwargs):
    print(kwargs)

>>show_kwargs(a=1,b=2)
{'a': 1, 'b': 2}
>>show_kwargs(a=1,b=2,c=3


## 8-9