# hello-world
3.21学习心得
今天是自学营的第一天。学习内容是GitHub的基本操作，参考资料就是Git官方文档（英文版）。有了前几天的预习，对于今天的学习内容并不太感到吃力，不过看完所有的参考资料再加上完成作业，也前后花了三个多小时。很庆幸自己这几年一直在坚持学习英语，今天才真正体会到笑来老师所说的“英语就是一双翅膀”，现在自己的英语水平能顺利阅读官方文档，这对学习效率是极大的提升。一切都刚刚开始，对未来的学习过程充满期待。
3.22学习心得
今天的学习内容主要有三项：
1、阅读Python环境变量的设置，这块因为涉及很多后期的应用，虽然英文能读懂，但是并不理解其中的很多含义，算是Forward Reference，等下再读一次，不理解的部分先放下。
2、通过谷歌搜索编写“Hello World”程序，编程倒没什么，一开始不知道怎么运行，最后还是谷歌搜索搞定F5键操作。也算是成功运行第一个自己编写的程序，蛮有成就感的。
3、用Jupyter Lab阅读《自学是门手艺》，这一步之前几天通过预习搞定了。

3.23学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是了解python数值、字符串以及基本运算。参考文件讲的新概念太大，暂时不能全部消化。作业内容是编单步计算器的程序，一开始完全没有头绪。在网上找到一段程序，先阅读消化，之后又自己编了两次，运行成功。通过今天的作业，初步接触了函数和条件分支的基本操作。
感觉参考文档的难度还是很大，有必要先把《自学是门手艺》先尽快通读完毕，会有利于后期的学习。

3.24学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是流程控制。作业要求用for和while分别打出九九乘法表，并且用while打出奇数行的九九乘法表。在阅读了《自学是门手艺》中关于流程控制的部分之后，重点分析了两种循环的特征，我在没有参考网上结果的情况下，独立完成了这三项作业，很有成就感。今天最大的收获就是通过实际编写代码体会到block这个概念的重要性，代码前面缩进几列涉及到一个block的界限，非常重要。也正是在多次调整语句前缩进距离之后，我今天的程序才运行得出正确的结果。

3.25学习心得
姓名：张凯山
学习时间：8小时
班级编号：19100205
今天的作业难度明显比前几天上了一个量级，第一题花了我几乎5个小时，当时真有深深的挫败感，后来是参考1期学员的作业再加谷歌搜索才理出了思路，然后一步步完成。第二题直接谷歌到答案，涉及到connection函数的应用，暂时还没搞明白原理。做第三题时又被数值list转换成字符串的函数问题卡住了很久，之前第一题里学到的join函数在这里不能直接应用，后来又是谷歌到了一个间接迂回的方法。目前是解决问题了，但是不知道还有没有更简便的方法（比如直接调用某个函数？）万维钢老师说刻意练习最好的环境是85%熟悉+15%意外，可这几天自学营的感觉是每天刚开始的时候熟悉的成分连15%都不到，越来越痛苦。但是克服困难完成作业之后的成就和喜悦也是越来越强烈。在训练营开始之前，我对自己能每天完成作业赢取学费奖励非常有信心，但到了今天，我的信心有些动摇了。已经挺过了五天，还剩九天，如果难度上升的斜率是如此陡峭，不知道自己能撑到第几天？不过无论最终结果如何，通过这几天的磨练我已经感受到了学习编程的乐趣，以后一定会坚持下去，耐心打磨这项有用的技能。

3.26学习心得
姓名：张凯山
学习时间：6小时
班级编号：19100205
今天的作业第一题基本就是昨天的延伸，所以比较容易就解出来了。但第二题看似和第一题一样，实际却有很大差别，想了很久，最后参考了一期学长徐悦的答案，他的解法很巧妙，几行代码就搞定了。虽然今天的作业并不都是靠自己独立思考完成的，但是能看懂学长的答案，通过这个过程也熟悉了很多基本概念，收获还是很大。
今日收获：
1、掌握了定义函数的流程。
2、深化了对数据结构和字典等基本概念的理解。
3、对于中文字符串，每个字是一个元素，可以用for i in text的方法来遍历，其中i是一个汉字。
4、可以用if u'\u4e00' <= i <= u'\u9fff'的条件来筛选汉字。
5、c =｛｝，c[i]=text.count(i),就是把i的计数作为字典c的第i个元素对中的第二个元素，第一个元素就是i。c.items()作用是列举字典c中的所有元素对。
6、countcn = sorted(countcn.items(), key=lambda item: item[1], reverse=True)的意义：sorted()函数用于对iterable进行排序，countcn.items()是排序对象，key=lambda item: item[1]，由方括号中的数字指定排序的是元素对中的第第一个元素，本题中就是汉字。item可以为任意字符，reverse=True表示由高到低。

3.27学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天的学习任务是将昨天编写的两个函数整合成一个模块，并形成文件，再从另外一个文件中进行调用，相对而言比较简单。我的私思路是先统计中文词频，然后将中文字和标点都删掉，再统计英文词频，然后将两个结果（字典）合并，最后进行排序。，最终成功实现了这个结果。
今日心得：
1、原来用
for i in text：
    if i < n:
        del i
这种循环条件删除字符串中的元素是无效的，但运行并不会报错，暂时还不明白这个del是什么作用。后来是用replace命令实现的删除。
2、在合并两个字典时试了几项操作都无效，比如
dictMerged1=dict(dict1.items()+dict2.items())
dictMerged2=dict(dict1, **dict2)
好像是版本问题，这两个方法在3.x版都无效。最后是用连续两个update实现的。
d1={1:[1,11,111],3:[3,33,333]}
d2={3:[3,33,333],4:[4,44,444]}
d ={}
d.update(d1)
d.update(d2)
d.update(d1)前面不能加 d=，经测试，如果两个字典中有相同的索引，会被覆盖，无论冒号后的第二个元素是否相同。
3.调用文件和函数时一定要注意文件路径！

3.27学习心得
姓名：张凯山
学习时间：3小时
班级编号：19100205
今天学习任务是要求添加函数的参数类型检查并捕获异常，看了教程之后有了个大概的印象，但并没有全部了解。作业是参照徐悦学长完成的，用到了if not isinstance(text,str):这样的表达。教练说建议用try catch实现，但因为时间不够，没来得及研究透。后续再细化吧。
今日心得：
1、try前面不能缩进！（教程中的例子前面还有个while，所以要缩进）
2、 if not isinstance(text,str):条件判断text是否为字符串，是否为其他数据类型，还要搜索查询。


3.29学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天学习的内容是标准库的引用和文件的读取。在之前第一次做词频统计的时候，就通过谷歌找到了connections.Counter函数，当时不太明白是怎么回事，今天知道这是标准库中的一个函数。文件读取之前也在《手艺》一书里读过，今天算是复习。过程中遇到了UTF-8编码的问题，总是报错，在教练的提醒下，看同学发的Issue解决问题。
今日心得：
1、with open('tang300.json','r',encoding='UTF-8') as f:
    text = f.read()
这其中f.read()输出的是一个字符串，encoding='UTF-8'可以避免编码报错问题。
2、今天编了判断闰年平年的函数，明白了if和“if then”是不一样的！
3、遇见程序报错，将错误代码复制到谷歌中搜索解决方法。

3.30学习心得
姓名：张凯山
学习时间：4小时
班级编号：19100205
今天的学习内容是安装和调用第三方库，安装方法通过谷歌很顺利就搞定了，调用方法也很简单。但是完成作业还是花了不少时间，主要是想通过.remove()函数实现列表元素的删除，但总是报错，最后想了其他的办法才完成。还有就是对汉字字符串的长度理解也出现了偏差。不过最后总算完成了作业，已经第10天了，大家继续加油！
今日心得：
1、安装pip：到网址https://pypi.org/project/pip/#downloads，找到Download files，下载pip-19.0.3.tar.gz，解压缩后，通过Juypyter Lab的terminal，用 cd 命令进入到刚才解压缩的文件中，输入python setup.py install命令。
2、通过pip安装第三方库：通过Juypyter Lab的terminal，进入pip所在目录，用python setup.py install命令。
3、一直想偏了，觉得汉字要经过编码，根据不同的编码方式，一个汉字的长度至少是2个字节，所以想2个汉字应该长度至少为4，实际上程序在统计汉字词语长度的时候，是将一个汉字长度计算为1的！
4、另外我最初的设想是用遍历判断每个词语的长度，如果小于2 就把该元素删除，用的是 list.remove(i)命令，但是报错'generator' object has no attribute 'remove'，暂时没搞明白原因，后来是用新建立一个空列表，把符合条件的元素用.append()命令添加进去解决的。

3.31学习心得
姓名：张凯山
学习时间：3小时
班级编号：19100205
今天的学习任务是使用之前的函数模块，再加上yagmail、requests和pyquery第三方库，提取网页内容并进行词频统计，同时将结果发送至指定邮箱。因为有两个库的用法在教材里已经直接给出了，所以今天作业的难度不大，比较顺利就完成了。不过仅仅是了解了这几个库的最基本的使用，要想深入了解，还需要后期更仔细地阅读相关说明文档。
今日心得：
1、输入的邮箱密码并非普通密码，而是一串经过编码的字母，要在邮箱网页获取。
2、用str_1 = str(dic)函数实现从字典到字符串的转换，不过这样得出的字符串，输出后看起来仍然是字典的样子，但用type()函数查看，显示的是字符串格式。

4.1学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天的学习任务是通过wxpy库实现对微信消息中的网址采集，并进行词频分析后将结果返回给发送消息的好友。一开始自己通过摸索，能针对特定某个好友实现该功能。但后来看作业要求是对全体好友，最后通过参考徐悦学长的作业完成了。收获不小，但也发现现阶段自己的最大问题：对标准库和第三方库的各项功能还不够全面深入，虽然能完成作业，但有的地方还是知其然不知其所以然。后期学习需要继续夯实基本概念。
今日心得：
1、搜索单个好友应该用 my_friend = ensure_one(bot.search(u'好友昵称')) 这个函数
2、作业要求是对全体好友自动回复，我最初自己实现的功能只能针对特定好友。后来看了徐悦学长的方法，他使用了一个函数装饰器@bot.register(my_friend,SHARING),并定义了一个auto_reply(msg)函数。经分析，装饰器的作用是监听来自my_friend的消息，如果类型为SHARING（分享内容），即把消息内容赋值给msg变量。只是我不理解的是，函数返回的结果将直接自动回复给发送消息的好友（my_friend），这应该就是auto_reply这个函数的作用，但为什么这明明是个自己定义的函数，却能自带自动回复的功能？经过搜索，网上有介绍该库自动回复的方法，貌似auto_reply(msg)只要括号里的参数是msg，就自带将函数return的结果自动回复的功能，无论函数名称为什么。这应该是这个库的自带功能。
3、经与教练沟通，确认wxpy库有个自带功能，如果定义的函数return结果为str类型，将自动回复。

4.2学习心得
姓名：张凯山
学习时间：5小时
班级编号：19100205
今天作业是以图形化输出昨天的作业。一开始被counter函数的输出格式搞得有点糊涂，其实这个输出是二维list，而非字典。后来又卡在了如何将输出图片发送给好友上，提出issue后有高手指点，又参照了徐悦学长的作业，最终解决了。最后的问题是输出图片中的中文字都呈现方框，查了说是字体缺失。同班李浩天同学指出了方法,解决问题。
今日心得：
1、dic = collections.Counter(text_list1).most_common(100)这个函数的输出格式是二维列表（也就是说每一个元素也是一个包含两个元素的子列表），而非字典！如果要转换成字典，用dic=dict(list)函数。
2、根据wxpy库的特点，return只能将字符串自动发送到微信好友，今天作业要求是返回图片，所以要用到
    matplotlib.pyplot.savefig('words_frequency.png')
    msg.reply_image('words_frequency.png')
 先把结果保存为图片格式，再将图片发送。
 3、plt.rcParams['font.sans-serif'] = ['SimHei'] ，这一步是为了添加字体，否则汉字会显示为方框

 4.13 学习心得
 1、值的三种形式：布尔值，数值，字符串。
 2、函数的关键字参数必须包含=，也就是必须指定一个具体值，无论是默认指定还是我们特别指定。
 3、Python用的编码是Unicode，跟ASCII没什么关系。
 4、input()函数接收的输入和传递的结果都只能是字符串。
 5、字符串是一种容器，每个元素即是一个字符。
 4.14 学习心得
 1、列表删除操作：del 和 pop 操作的对象是索引，remove 操作的是元素本身,表达形式为：
    del a_list[i]   p = a_list.pop(i)   a_list.remove('example')
 2、集合中不能有重复元素，而且是无序的。包括可变和不可变两种。创建集合要用 p = set(),
    如果用 p = {}，这样创建出来的是字典。
 3、数据结构就是容器。
 4、冻结集合（Frozen Set），Frozen Set 之于 Set，正如 Tuple 之于 List，前者是不可变容器（Immutable），后者是可变容器（Mutable），无非是为了节省内存使用而设计的类别。
 5、dic 为字典：
 list(dic) 得到一个以dic中所有key（索引）为元素的一个列表。set(dic)、tuple(dic)分别得到以key为元素的集合与元组。
 dic.itenms() 得到一个二维列表，每个元素为字典的映射对 (key,value)，也就是说这个列表中每个元素都是一个包含两个元素的子列表。
 sorted(dic) 得到一个以dic中所有key（索引）为元素的一个列表，并按顺序排列。

 4.15 学习心得
 1、
def be_careful(a, b):
    a = 2
    b[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b

运行结果是(1, ['What?!', 2, 3])

def be_careful(a, b):
    a = 2
    b_copy = b.copy()
    b_copy[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b

运行结果是：(1, [1, 2, 3])

可变容器（例如，列表）经过函数运算后，会把函数运算结果更新到列表中，如上述第一个函数；
通过.copy()函数，可以备份列表，使其不受函数运算的影响，如上述第二个函数。
对列表运行其他Method也是如此，会改变原来的列表。
而不可变容器，例如元组，字符串，则不会被函数运算结果改变，如果要得到函数运算结果，应该将结果赋值给一个新变量。这一特性也就体现了“可变”和“不可变”的意思。

2、遍历函数中的Arbitrary Positional Arguments时，如果参数是字典，则只遍历其中的key部分。
3、 Arbitrary Keyword Argument 似乎必须是字典格式？或者类似字典的映射结构？因为关键字参数必须具有key=value的结构。

4.21 学习心得
1、
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

str = 'error wonderer severeness'

pttn = r'er+'
re.findall(pttn, str)

pttn = r'[er]+'
re.findall(pttn, str)

pttn = r'(er)+'
re.findall(pttn, str)
运行结果：
['err', 'er', 'er', 'er']
['err', 'r', 'erer', 'e', 'ere', 'e']
['er', 'er', 'er']

pttn = r'[er]+' 的意义分析：
从字符串的开头开始寻找，第一个字符是e或r就匹配，然后继续向后找，如果是e或r也匹配，如果不是e或r就中断，然后把之前匹配的片段合并输出。之后继续用同样的规则向后找，找到匹配的片段再输出，直至整个字符串结束。

4.23 学习心得
1、官方文档中对嵌套(nest,nested)list的介绍
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b

x[0][1]表示两重索引，x[0]是['a', 'b', 'c']，x[0][1]就是['a', 'b', 'c']中的第二个item。
2、
>>> a = 1
>>> b = 2
>>> a, b = b, a + b
第三行是先计算等号右边，形成一个元组(2,3),然后把这个元组的值分别赋给左边的a和b，使a=2，b=3。
a, b = b, a 相当于就是把 a 和 b 对调一下。
官方文档实现斐波那契数列的方法：
a, b = 0, 1
while a < 100:
        print(a)
        a,b = b,a+b
自己想出的使用中间变量的方法，但不如上述方法简洁：
a, b = 0, 1
while a < 100:
        print(a)
        c=a+b
        a=b
        b=c
3、True 和 False 分别等于数值 1 和 0。数值进行布尔运算，得出的结果也是数值（0 或后一个本来值）：
0 and 2     # => 0
-5 or 0     # => -5
5 and 2     # => 2

4.24 学习心得
1、字典的key必须为不可变类型，而value可以使任意类型。不可变类型包括：整数、浮点、字符串和元组。
2、list(dict.keys())这个method可以将字典dict的key提取出来形成一个list。
   list(dict.values())这个method可以将字典dict的value提取出来形成一个list。
3、字典的in命令对象是key而非value，例如：1 in dict 。
4、集合(set)的元素必须为不可变类型。4.29 学习心得
1、函数参数的传递顺序，运行以下代码的各项结果，可以体会：
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments，关键字参数赋值顺序没有要求
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

如果传递参数的过程中有=，则将特定参数值赋给特定参数；
如果没有=，则按顺序给各项参数赋值。
以下传递参数的方式无效：
parrot()                     # 必须为位置参数赋值，关键字参数可以不赋值，因为其有默认值
parrot(voltage=5.0, 'dead')  # 位置参数不得放在关键字参数之后赋值
parrot(110, voltage=220)     # 对同一个位置参数重复赋值
parrot(actor='John Cleese')  # 对未知的关键字参数赋值
2、*arguments（随意的位置参数）接受的是元组,**keywords（随意的关键字参数）接受的是字典。体会以下代码及运行结果：
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch") # 关注随意的未知参数和随意的关键字参数赋值方式，尽管它们并没有显示为元组                                和字典的形式。另注意关键字的顺序。

运行结果：

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch

3、*引导的随意的位置参数，实际上相当于把一个元组解开了，参见以下代码：
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
4、**引导的随意的关键字参数，实际上相当于把一个字典解开了，参见以下代码：
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
5、用匿名函数处理嵌套list排序的方法，作业中统计词频时用到过：
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) # 这句中的lambda函数针对的是每个子列表中的第二个元素排序，如果改成                                                 key=lambda pair: pair[0]，就是针对第一个元素排序。
print(pairs)

5.3 学习心得
1、list comprehension：方括号中可用多个 for 和 if，for 在 if 之前，中间不用逗号。
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
形成一个嵌套列表，等效于以下代码。
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
2、用两个 for 循环嵌套，将一个二维嵌套列表拆解成一个一维列表。
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
等效于：
vec = [[1,2,3], [4,5,6], [7,8,9]]
l = []
for elme in vec:
    for num in elme:
        l.append(num)
print(l)
3、字典的 key 必须是不可变类型，例如：字符串、数字和元组。
4、如果 d 是个字典，list(d) 可以导出一个列表，元素为 d 的所有 key。
5、字典生成器：
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
5.4 学习心得
1、嵌套list的又一个应用：
>>> lists = [ [] for i in range(3)]  #形成元素分别为三个空list的一个嵌套list
[ [], [], [] ]
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
lists[0].append(3)的意思：lists[0]表示大 list 中的第一个元素，也就是一个空list：[]，
lists[0].append(3)也就是在这个空 list 的所有元素的末尾中加上一个 3,因此得到一个新 list：[3]。

5.9 学习心得
1、
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> list(d)
['one', 'two', 'three', 'four']
>>> list(d.values())
[1, 2, 3, 4]
>>> d["one"] = 42
>>> d
{'one': 42, 'two': 2, 'three': 3, 'four': 4}
>>> del d["two"]
>>> d["two"] = None
>>> d
{'one': 42, 'three': 3, 'four': 4, 'two': None}

将字典的 key 和 value 分别提取成为 list。将某个元素删除后再赋值，其位置位于字典末尾。
2、
d = {"one": 1, "two": 2, "three": 3, "four": 4}
k = d.keys()
v = d.values()
i = d.items()
输出结果为：
k：dict_keys(['one', 'two', 'three', 'four']) 
v：dict_values([1, 2, 3, 4])
i：dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
k、v 和 i 的 type 都是 class。
list(k)、list(v) 和 list(i) 能将结果形成 list，其中 list(i) 是二维嵌套 list。
3、l 为 list，l.sort() 会将 l 的元素按字母顺序进行排序，并且会改变 l。print(l.sort()) 结果为 None，print(l) 结果才是排序后的 list。

5.10 学习心得
1、序列后[：：2]和[：：-1]的作用：
>>> 'ABCDEFG'[::2]
'ACEG'
第一个冒号前后表示筛选的起止点，留空表示序列的整个范围，最后一个 2 表示筛选的步长。因此：
>>> 'ABCDEFG'[::3]
'ADG'
[：：-1] 就是将原序列翻转：
>>> 'ABCDEFG'[::-1]
GFEDCBA

5.12 学习心得
如果 d1 和 d2 分别是一段文字的中英文排序结果（字典），那么 d = d1 + d2，d 中的元素会自动按中英文混合词频排列。
5.15
目前摸索出唯一能正常运行的 try/except 形式，注意缩进：
try:
    if type(text) != str:
        raise ValueError
except ValueError:
    print('输入类型错误')
根据官方文档中的介绍，中间两句 if……raise 似乎是不必要的，但是删除后运行会报语法错误。
5.17 学习心得
1、c = Counter(['eggs', 'eggs','ham'])
   print(c['eggs'])
结果为 2，相当于是显示字典 C 中 key 为 'eggs' 时的 value 值。
2、Counter 支持 subtract 的减法操作：
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
5.19 学习心得
1、以文件的行为目标对整个文件进行迭代：
with open(workfile) as f：
    for line in f:
    print(line, end='')
结果：
This is the first line of the file.
Second line of the file
5.20 学习心得
通过认真分析《手艺》中的 Golem class，对 OPP 的概念有了更深入的了解。
示例 class 的 method 里的
Golem.population += 1 以及 Golem.population -= 1，如果换成：
self.population += 1 以及 self.population -= 1 结果会不一样。
书中解释原文为：
“self.population 总是去读取 Golem 类中 population 的初始值，即使后面通过 setattr(Golem, 'population', 10) 更改 population 的值后，self.population 的值仍为 0，但 Golem.population 值则为 10。”
经修改测试，归纳总结如下：
1、定义 Golem 这个 class 之后，通过 g = Golem ()，就可以创建一个名为 g 的 object，从使用的角度讲，也就是这个 class Golem 的一个 instance。
2、创建 g 之后，如果 Golem 的定义中有对 self.population 的赋值，那么该赋值不受 Golem.population 值变化的影响。
3、如果将书中代码 Golem.population += 1 以及 Golem.population -= 1 换成：
self.population += 1 以及 self.population -= 1，即使有 setattr(Golem, 'population', 10) 修改 Golem.population 的值，但 g.population 仍然为 1。相当于 setattr(Golem, 'population', 10) 修改的是 Golem 这个 class 中的 population 值，而 g.population 是 g 这个 instance 中的属性，不受 Golem 这个 class 中属性值变化的影响。
4、假如 Golem 这个 class 中没有对 self.population 这个属性的赋值，那么在外部调用 g.population 就只能从 Golem 中寻找 population 的值，即 Golem.population。 
5、定义 method 时，__ int __ methond 中出现了 self.__active = False，其中 __active 这个变量之前并没有定义，但是也可以用。我随便加了另外一个未定义的变量 self.b 或则 self.__b，运行没问题，但外部调用 g.b 和 g.__b 报错。另外从外部调用 g.__active 会报错，因为 __active 是私有变量。从目前测试结果看，在 class 的外部，只能调用 class 主目录中的属性（即 hasattr(Golem, attr) 结果为真的属性 (attr)）和其中定义的 method。如果在外部调用 class 中的私有变量（前面加 __ 的变量）或者某个 method 中前面不带 self. 前缀的变量，都会报错。
6、若要在外部调用 class 中的私有变量，可以通过 method 中的 return 来返回结果，例如书中例子里的 is_active(self) 中的 return self.__active。
7、如果一定要从外部调用 class 中的私有变量，通过函数装饰器实现。
8、在外部运行 hasattr(Golem, attr) 时，如果 attr 是 class Golem 中的 method 定义的带有 self. 前缀的属性（变量），结果为真。
5.22 学习心得
1、官方文档中示例：
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

经测试能正常运行，x.counter 这个 attribute 并没有在 MyClass 中声明（declare），为什么也能被调用？官方文档中做了明确解释：
 Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. 
 官方文档中说 class 的两个主要 attribute 是 data attribute 和 method，对应于《手艺》中讲的属性和方法（attribute 和 method）。
 其中 data attribute 可以未经 declare 就使用，比如上面的 x.counter。但 method 就必须 declare 之后才能用。上例中 x.f 可以用，因为有 def f(self)，但 x.a 就不行。

 2、class 中的公共变量不宜使用可变类型，否则如果后面的 method 对该变量进行修改后，再有其他的 instance 引用该变量，会引用改变后的变量。
 官方文档示例：
 class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)               # unexpectedly shared by all dogs
print(e.tricks) 

结果：
['roll over', 'play dead']
['roll over', 'play dead']

因为公共变量 tricks 是个 list，这是可变类型。要想避免这种情况，将公共变量变成每个 method 中的私有变量：
class Dog:
             
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks = []  
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)             
print(e.tricks)  

《手艺》中举的 population 变量，因为通过 population = 0 这个赋值确定了 population 的类型是 int 整数，而数值都是不可变类型，因此可以用作整个 class 的公共变量。

5.23 学习心得
1、函数装饰器，通常至少有两层函数嵌套，外层以被装饰函数为参数，内层定义对被装饰函数进行的操作。外层（装饰器）函数 return 的就是内层函数，注意返回的是函数本身（不带括号）。如果带括号就是函数运行的结果，这二者有区别：
def a_decorator(func):
    def wrapper():
        print('We can do sth. before calling a_func...')
        func()
        print('... and we can do sth. after it was called...')
    return wrapper

@a_decorator
def a_func():
    print("Hi, I'm a_func!")

a_func()
5.27 学习心得
1、在使用 yagmail 库的时候，一定要加上 host 这个参数的赋值，否则会报错：
yag = yagmail.SMTP(username,passport,host = 'smtp.qq.com')
yag.send(recipient,subject,contend)
其中 username 和 passport 是发送邮件的邮箱的用户名和密码。recipient,subject,contend 是接收邮箱、邮件主题和正文。
上述参数的类型均为 str。
2、正则表达式
边界原子
我们可以用边界原子指定边界。也可以称作 “定位操作符”。

^ 匹配被搜索字符串的开始位置；

$ 匹配被搜索字符串的结束位置；

\b 匹配单词的边界；er\b，能匹配 coder 中的 er，却不能匹配 error 中的 er；

\B 匹配非单词边界；er\B，能匹配 error 中的 er，却不能匹配 coder 中的 er。
$ = EOS，也就 End Of String 的首字母缩写。
\b 匹配单词的边界；也就是说 er\b 表示 er 之后就要到达单词的边界，否则就不匹配。最终搜索到的结果呈现为 er。
5.31 学习心得
1、关于正则表达式(er)+的问题：
正则表达式中的圆括号表示捕获，+表示一个或多个，(er)+ 匹配 wonderer 这个单词时，返回结果是 er，而非一开始我想象的 erer。在自学营提了 issue，有高人回答我才弄明白：(er)+ 将 wonderer 中的两个 er 都捕获到了，但后一次捕获将前一次捕获的结果覆盖掉了。捕获返回的结果，永远都是括号内的内容。
a = re.findall(r'(er)\d','er2')
结果也是 ['er']，而非['er2]
以后有问题想不明白，应该去自学营提 issue 求助。
6.2 学习心得
今天读《Think Python》时遇到这样一道习题：编一个打印田字格的程序。一开始想了很久思绪都不清楚，试着写出的代码运行也不正确。后来换了一个思路，先打印出由+组成的11*11矩阵，然后一步步通过条件语句替换，用坐标的思维来接近目标，结果调试几次之后很顺利地得出了结果。学习编程果然是锻炼人逻辑思维能力的好方法，只有自己的思考到位了，才能写出正确的代码。就好比只有有了高质量的思考成果，再用文字体现出来才是一篇好文章一样。代码和文字都只是工具而已，真正有价值的是人的思考和创造。后来进一步优化，对每个交叉点的坐标用抽象的表达式来表达，而非列出具体的数字，并且通过输入控制每行和每列打印出的格子数量。
6.3 学习心得
今天《Think Python》的作业是通过turtle画多边形和圆。通过自己亲手敲出来的代码，再看着运行结果，才切身体会到计算机是无法画出曲线的。难怪游戏画面里的曲线都呈现出锯齿状，因为这些曲线都是通过小的线段近似模拟出来的。模拟得越平滑，需要消耗的系统资源也就越多。
在编写绘制图形函数的时候，把类 turtle 的一个对象 t 作为函数的一个参数，但是在函数内部却并不用导入 turtle 模块，只需在调用函数之前，导入模块并创建对象 bob 即可，这点比较意外。
6.6 学习心得
1、使用多重括号时一定要注意，不能多了或者少了括号，否则会在“下一行”报语法错误！而往往下一行的语句本身并没有语法错误，因此很难找出问题原因，切记！
今天就犯了这个错误，一直以为是编译器出问题了，其实还是自己的错误。
2、math 中的三角函数，输入参数为弧度，结果范围是 +1 至 -1，可能为负值。
3、如果是需要再循环中多次使用的常量，应在计算后赋给一个变量，然后循环中直接使用该变量，这样可以减少计算量。
4、在函数内部不应使用 import，而应在包含该函数的模块一开始使用 import。例如 import math,import 。
5、同一个模块中的多个函数，如果彼此间存在引用关系，可直接引用，无需 import，而且函数的先后顺序无妨。可以这样理解：在某个函数中如果要调用其他函数，编译器会默认从本 py 文件中寻找具有该名称的函数，找到了就直接调用，找不到就报错。
6.7 学习心得
1、函数的关键字参数，实际上也就是位置参数，只不过在编写函数的时候对它赋了一个默认值。因此在调用函数的时候，位置参数因为没有默认值，所以必须赋值，否则会报错。但关键字参数可以不赋值，此时就使用其默认值。
2、如果一些参数的变动范围很大，并且对最终的运行结果有很明显的影响，可以将其设置为关键字参数，提供默认值。比如螺旋线绘制函数中的螺旋线疏密度 b 以及近似弧线的角度 angle。在最初调试时因为设置值不当，一直出不来效果。
3、r = b*theta，theta 初始值为 0 ，对初始值的赋值应在 for 循环开始之前！
4、x % 10 可以得到 x 的最后一位数，x % 100 可以得到 x 的最后两位数。
5、if 和 elif 组成的分支，从上到下按顺序检查，满足条件则执行相关语句，执行完毕后会跳过后面的分支。即最多只执行一个分支。
6.8
一、递归函数
1、最适合应用在多层重复任务当中，比如科赫曲线。这种类型的任务如果用 for 循环嵌套来实现，会显得非常复杂，可读性差，用递归函数就显得简洁多了。
2、在调用自身函数之前，必须设定终止条件,并同时明确需要完成的动作。例如，算阶乘就要明确计算动作，倒计时就是打印当前数字，科赫曲线就是画一条线段（也就是 0 阶科赫曲线）。如果要停止运行，可用 return，因为函数中一旦运行 return ，后面的部分就不会再运行了。
3、在要出现重复的时候调用自身，同时要调整参数。比如科赫曲线的原理是把上一层的每条线段再变成一条科赫曲线，从而形成下一层，因此在画上一层的线段时调用自身，即将原本的 t.fd(lenth/3) 变成 koch(t.m,n-1)，其中 m 为原线段长度的三分之一。n-1 体现的是分型阶数减一，同时也是递归指标向终止点靠近一步，该参数的变化是实现递归的关键！
4、典型应用：科赫曲线，阶乘，倒计时。
5、在阅读递归函数时，应该采用“信仰之跃”方法，看到调用自身函数时，不要按顺序阅读，而应该假设调用自身后产生了有用的输出。例如，阶乘函数：
return n*f(n-1)
在调用 f(n-1) 时，不要再从头去看 f(n-1) 的内部代码，只把它当成 (n-1) 的阶乘，而 n*f(n-1) 也就是 n 的阶乘。
6.9 
1、while 循环中的判断条件不一定非要紧跟在 while 之后，也可以用 while True 开头，后面用条件判断 + break 的方式来结束循环。例如《Think Python》中的求平方根函数。
6.12
凯撒密码编程过程心得：
1、将大小写字母 a 和 A 设置为起点，再加上变化值 % 26（对 26 求余），可以避免繁琐的分情况讨论。类似的循环移位情况，都可以用这个方法来处理。
2、负数求余和之前想象的不一样：-24 % 26 = 2，而非之前想象的 -24！也就是说求余的结果一定是非负数。
3、自己的思路可能存在思考不完善、繁琐、表达代码可读性差的问题，参考更优解决方案后，不应敝帚自珍，而应该果断博采众长。
6.13
1、读取文件之后，可以用将每行作为一个元素，对文件进行遍历。
with open(file.tex) as f:
    for line in f:
        ....
2、
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False

同样内容的字符串，是一个对象，而同样内容的列表则是两个对象。

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b[0] = 42
>>> a
[42, 2, 3]

赋值产生同一个对象，改变其中一个会影响另一个。

>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None
list 的 del、append、切片等方法都会直接改变原 list，t2 = t1.append(3) 或者 t2 = t1[1:3] 都是错误的。对于所有的可变类型，要慎用此种语句！
大多数关于 list 的函数都会改变作为参数传入的 list，例如，sort，如果要保留原 list，应提前做好备份。
6.17 
1、对字典的 key 值进行遍历，for i in dic，这种方法的销量比对 list 中的元素进行遍历要快。通过 rotate pairs 程序亲测有效，比 is_bisection 速度快很多！根据 Think Python 书中的说法，似乎是字典通过哈希方法构造，效率更高。
2、遍历字典时的 keyerror 是因为 key 值并不在字典当中。
6.18
1、建立只包含一个元素的元组，必须加逗号：
t = 'a', 
或者
t = ('a',)
建立空元组：
t = ()
而 t = ('a') 是一个字符串！
2、如果要将一个序列（列表、元组、集合、字典等）作为参数传递到函数中，这个参数必须前面带*，即 arbitrary argument。
>>> t = (7, 3)
>>> divmod(t)
TypeError: divmod expected 2 arguments, got 1 #错误

>>> divmod(*t)
(2, 1) # 正确

3、如果被迭代对象的每个元素是一个元组，可以用两个变量来遍历：
for x, y in zip(t1,t2):
4、几个元素之间用逗号分隔，外部没有括号，也是元组。元组可用作字典的 key，但列表不行，因为元组不可变，字典可变。
5、zip 本身只是输出一个对象，结合list使用，得出一个元素为元组的列表：list（zip（t，s））。
6、通过寻找所有单词列表中的 anagrams，以及之前寻找 interlock 单词的例子，可以证明两层 for 循环嵌套来遍历整个单词列表的效率是非常低的，不可用！应该尽量找到每个单词只用处理一次的方法。比如 anagrams，书中的答案是为每个单词计算出一个 signature，然后把所有 signature 相同的单词合并到一个列表中即可。
7、在实现对 anagrams 进行排序时，是将列表长度和列表本身组合成一个两个元素的元组，然后再以多个此类元组组成一个嵌套列表。排序时针对元组的第一个元素（即列表长度）进行排序：list.sort()。
6.19
1、今天完成 Think Python 第 12 章最后一道练习题，第一次从头到尾独立完成了一个递归函数，很有成就感！之前的思路都没问题，base case 识别得很准确，但就是卡在最后一步递归调用的地方，每次测试都出不来正确结果，只得出一个 None。最后经过反复调试，先想到加 print，出现一个正确结果后面加上几个 None，后来把 print 改成 return，就得出正确结果了！其中的原理还不是很清楚，但至少也是有了一定心得。不过自己编的程序虽然得出了正确结果，但运行效率还是比书中的参考答案慢不少。我用秒表掐了一下，参考答案得出结果大约四秒左右，而我自己的程序要十秒左右，明天再看他的方法吧。
代码片段如下：
def is_remove1(word_list): #此方法用递归方式实现
    if 'a' in word_list or 'i' in word_list:
        return True    
    elif word_list == []:
        return False
    else:
        return is_remove1(list_child(word_list)) # 这里一定要加 return！否则输出结果为 None

2、还发现一个问题：
if 'a' or 'i' in word_list:
如果 word_list 是个列表，那么这个条件判断的结果永远为 True！
改成：
if 'a' in word_list or 'i' in word_list:
才对。

6.20
1、在函数定义之前已经出现的变量，可以在函数定义的过程中被使用：
a = 1
def add(t):
    s = a + t
    return s
print(add(2))

运行结果为 3

6.22
str.strip()
这个函数可以在括号中传递参数，类型为字符串，这样可以将前面 str 末尾处包含的参数中所包含的字符去除，如果不传递参数，将默认清除白空格。
t='-ab-cd-('
s = '-,:('
print(t.strip(s))
结果：
ab-cd
统计词频时，可用此方法清除标点符号和空格。
2、list.extend() 方法类似于 append，差别在于前者的参数是序列，而后者的参数是单个变量或常量。
6.23
读取 txt 文件时的注意要点：
1、用 for line in fin： 一行行读取，然后将每行的结果汇总。
2、用 str.replace('-',' ')将 - 替换为空格
3、用 
strippables = string.punctuation + string.whitespace
str.strip(strippables) 
去除所有白空格和标点符号。
4、用 str.lower()统一变成小写字母。
6.24
1、虽然元祖是不可变数据类型，但可以进行加法运算
s = (1,2,3)
s= s + (4,)
print(s)
结果为 (1,2,3,4)，注意加法算式中的 4 后面有个逗号，表示这是一个元素数量为 1 的元祖。这种方法类似于列表的 append() 方法，可以通过遍历一个序列后得到一个元祖。
7.12
如果定义类 A 的时候出现了嵌套现象，即该类的参数中出现了另一个类 B，那么在实例化 A 的时候，应先将 B 而非 B 的实例作为参数传入，然后再定义一个 B 的实例，否则会出错。
例如 Think Python 15 章的练习，在调用矩形类 Rectangle 时应该这样，其中 Point 是表示点的类：
r1 = Rectangle(150,100,Point)
r1.corner = Point(-100,100)
而以下方式是错的，无论将矩形顶点（corner）的坐标设为多少，编译器都只会将其视为（0，0）：
corner = Point(-100,100)
r1 = Rectangle(150,100,corner)
7.14
用 datetime 模块处理时间的基本介绍：
https://www.cnblogs.com/hello-wei/p/9540765.html
7.16
1、Think Python 第 17 章的作业中出现以下这个函数
def __str__(self):
        t = [self.name + ' has following content:']
        for obj in self.pouch_content:
            t.append(object.__str__(obj))
        return '\n'.join(t)
object.__str__(obj) 这个 method 应该是返回 obj 这个对象的 str。经测试发现，如果 obj 是一个字符串、字典、列表、元祖，，object.__str__(obj) 会返回变量本身。
2、该作业中，bad kangaroo 和 good kangaroo 的区别在于 __init__ 函数：
good：
def __init__(self,name,content = None):
        self.name = name
        if content == None:
            content = []
        self.pouch_content = content
bad:
def __init__(self,name,content = []):
        self.name = name
        self.pouch_content = content
bad 的问题在于，将关键字参数 content 设为了一个可变类型——列表，后期如果调用该函数会导致 content 发生变化。而 __init__ 函数只有在实例化时才会读取默认值。
运行 bad 程序时，先实例化了 roo，此时 roo.pouch_content 等于 content，此时是一个空列表。然后后面调用函数后，将 content 这个列表中加入了元素，所以导致  roo.pouch_content 也随之发生变化，使得 roo.pouch_content 不再是一个空列表。
此时 roo.pouch_content 和 kanga.pouch_content 是同一个变量，roo.pouch_content is kanga.pouch_content 的结果为 True，可以视为一种联动效应。例如：
a = [1,2]
b = a
a.append(3)
此时 b = [1，2，3]
而且 a is b 的结果为 True

而 good 程序将 content 这个关键字参数设置成一个不可变类型 None（这里设置为数值或者字符串类型也可以，只要是不可变类型就行），在实例化过程中对每一个对象进行初始化时，先检查这个不可变类型，满足条件后将一个空列表赋值给 self.pouch_content。这个例子的目的是告诉大家，不可将 __init__ 函数中的关键字参数设置为可变类型，否则会出错。
后来自己想出改进的方法，就是去掉 content 这个关键字参数：
def __init__(self,name):
        self.name = name
        self.pouch_content = []
运行结果也是正确的。
7.19
1、如果类内部定义的 method 的参数只有本类的对象，那么在调用时应该用类名，Think Python 第 18 章
__eq__(self,other)
调用时应为 Card.__eq(c1,c2),其中 c1 c2 是 Card 的对象。
2、obj 为一个对象：
str(obj) 就会返回该对象的__str__()结果，类型为字符串
7.30
1、
L1.extend(L2) 会将列表 L2 附接在 L1 之后，
L1.append(L2) 则将 L2 作为一个元素加在 L1 末尾（嵌套）。
2、在对列表进行迭代的过程中，一定不能将该列表进行修改，否则迭代过程无法正常进行，也就是说，不能对列表进行 remove、append 等操作。
3、可用 copy 方法解决上述问题，以下代码可找出两个列表中重叠的元素。
L1 = [1,2,3]
L2 = [2,3,4,5,6]
l1 = L1.copy()
for i in l1:
    if i not in L2:
        L1.remove(i)
print(L1)
结果：
[2,3]
8.4
1、class 中的 __lt__ method 会替代 < 的功能，定义次函数后，如果出现 self < other，就会调用该函数。
MIT 课程第 8 章例子：
print(him < her) 结果：
False
后续如果有sort()方法，在排序时也会根据上述 __lt__ method 规定的顺序来进行排序。同理，__eq__ method 代替 ==
8.4
list1 = list2[:] 可用于copy列表。
2、类的属性和实例的属性并不相同
class A():
    b = 1
    def __init__(self):
        self.b = 2
a = A()
print(A.b,a.b)

运行结果为
1 2
3、类的属性可以发生变化
class A():
    b = 0
    def __init__(self):
        self.b = 2
        A.b += 1
a1 = A()
a2 = A()
print(A.b)
运行结果为
2
每次生成一个 A 的实例，都会把 A.b 加 1，因此生成两个实例（a1、a2）之后，A.b 就变成了 2。
注意 A.b += 1 这个语句一定要放在 __init__ method 中，这样初始化一个实例时，就会运行该语句。
8.7
1、类的属性通常在__init__ 初始函数中定义。
2、类通常包括写入和提取数据的 method，比如 MIT 教材第八章中的的例子，有 addStudents addGrades 和 getStudents getGrades。
8.16
MIT 教材第九章提出一种穷举列表中各个元素排列组合的方法，就是一串长度为 n 的二级制代码，其中 n 为列表中元素的个数，每一位的 0 或 1 来代表该位置所在的元素是否出现，举例：
L = ['x','y','z']
那么代码 011 就表示 ['y','z'],101 就表示 ['x','z']，000 表示空列表 []。
8.19
L = [3,5,2]
D = {'a':12, 'c':5, 'b':'dog'}
print(sorted(L))
print(L)
L.sort()
print(L)
print(sorted(D))
D.sort()
运行结果为：
[2, 3, 5]
[3, 5, 2]
[2, 3, 5]
['a', 'b', 'c']
AttributeError: 'dict' object has no attribute 'sort'
说明以下特性：
sorted(L) 不改变原列表
而 L.sort() 会改变原列表
字典没有 .sort() 方法。

9.12
调用 pylab 库进行数据可视化的时候，一定要在最后加上一个语句 pylab.show()，否则图形会显示不出来。
前面最好调用 import numpy，否则可能报错：
ImportError:
Importing the multiarray numpy extension module failed.  Most
likely you are trying to import a failed build of numpy.
If you're working with a numpy git repo, try `git clean -xdf` (removes all
files not under version control).  Otherwise reinstall numpy.

Original error was: DLL load failed: 找不到指定的模块。

10.9
1、timeit 模块可用来计算某段代码的执行时间，目前知道的用途是检测函数的执行效率。《Problem Solving with Algorithms and Data Structures》一书中53页内容。
自己调试了以下代码，比较两种求最大公约数函数的执行效率：
def gcd_1(m,n):
    if m % n ==0:
        return n
    else:
        return gcd_1(n,m % n)
def gcd_2(m,n):
    while m % n != 0:
        m , n = n, m % n
    return n
m, n = 21, 28

import timeit
from timeit import Timer
t1 = Timer("gcd_1(21,28)", "from __main__ import gcd_1")
print('gcd_1',t1.timeit(number=1000000), "milliseconds")
t2 = Timer('gcd_2(21,28)', 'from __main__ import gcd_2')
print('gcd_2',t2.timeit(number=1000000), 'milliseconds')
print(gcd_1(m,n))
print(gcd_2(m,n))

这里出现的问题是，t1 = Timer("gcd_1(21,28)", "from __main__ import gcd_1")，这一语句中必须给函数提供明确的参数，
如果写gcd_1(m,n)，则会报错：
Could not load source '<timeit-src>': Source unavailable.

2、还可以用repeat方法来进行重复，输出结果是一个list
from timeit import repeat
t1 = repeat("gcd_1(21,28)", "from __main__ import gcd_1",repeat = 2)
print('gcd_1',t1, "milliseconds")

综合考虑似乎repeat方法更简洁，其中 number 和 repeat 两个关键字参数默认值为 1000000 和 5：
def gcd_1(m,n):
    if m % n ==0:
        return n
    else:
        return gcd_1(n,m % n)
def gcd_2(m,n):
    while m % n != 0:
        m , n = n, m % n
    return n


import timeit
from timeit import repeat
t1 = repeat("gcd_1(21,28)", "from __main__ import gcd_1",number = 10000, repeat = 3)
print('gcd_1',t1, "milliseconds")
t2 = repeat("gcd_2(21,28)", "from __main__ import gcd_2",number = 10000, repeat = 3)
print('gcd_2',t2, "milliseconds")
10.16
建立一个class之后，可以在其他文件中通过 import “Class名称”来进行引用。
10.18
可使用 eval(str) 函数将字符串形式的表达式计算结果。
复制 PDF 格式的书籍中的一段代码，其中有一个符号是‘−’，想当然的以为是减号，但导致运行结果不正确，最后把这个符号换成减号后，得出了正确的结果。我在键盘上找了个遍，都没能打出这个符号来。类似的情况还有乘方符号 ˆ ，也是不对的，正规的符号是 ^。估计是 PDF 的字体问题。可能其他运算符号也会出现这种问题。原则就是，自己用英语输入法通过键盘打出来的符号才是正确的。
解决这个问题的方法是在每个重要循环后用 print 语句打出中间结果，发现在应该出现减号的那个循环缺失了，因此定位出问题。这种 debug 的方法很重要，应该善加利用。
10.25
赋值语句：
a = b
的实质，是让变量 a 指向变量 b 的值所占用的内存空间里的值。
测试代码如下，用函数 id(obj) 显示对象 obj 所在的内存位置：
a = 1
b = 2
print('1\'s location is', id(1))
print('2\'s location is', id(2))
print('a\'s location is', id(a))
print('b\'s location is', id(b))
print()
c = a
print('1\'s location is', id(1))
print('2\'s location is', id(2))
print('a\'s location is', id(a))
print('b\'s location is', id(b))
print('c\'s location is', id(c))
print()
a = b
print('1\'s location is', id(1))
print('2\'s location is', id(2))
print('a\'s location is', id(a))
print('b\'s location is', id(b))
print('c\'s location is', id(c))
print()
b = c
print('1\'s location is', id(1))
print('2\'s location is', id(2))
print('a\'s location is', id(a))
print('b\'s location is', id(b))
print('c\'s location is', id(c))
print()

运行结果为
1's location is 140724695970640
2's location is 140724695970672
a's location is 140724695970640
b's location is 140724695970672

1's location is 140724695970640
2's location is 140724695970672
a's location is 140724695970640
b's location is 140724695970672
c's location is 140724695970640

1's location is 140724695970640
2's location is 140724695970672
a's location is 140724695970672
b's location is 140724695970672
c's location is 140724695970640

1's location is 140724695970640
2's location is 140724695970672
a's location is 140724695970672
b's location is 140724695970640
c's location is 140724695970640
仔细体会！数值 1 和 2 的内存位置始终不变，变量 a 和 b 指向的数值对调了。注意赋值语句 c = a，之后尽管 a 的数值和内存位置都发生了变化，但 c 指向的还是 a 发生变化之前的内存位置和数值，并没有随 a 的变化而变化。
Problem solving 一书中 Unordered list 对象的 add 方法，就是通过这一点实现的：
def add(self,item):
    temp = Node(item)        
    temp.set_next(self.head)        
    self.head = temp
表面看这个函数似乎存在循环引用，但第三行 temp.set_next(self.head) 意思是将 temp 所指向的内存位置中保存的 Node 对象的下一个节点设置为 self.head 所指向的内存位置中保存的 Node 对象，下一句中虽然 self.head 所指向的内存位置中保存的 Node 对象发生了变化，但不影响第三行中的 self.head。也就是说虽然第四行中的赋值语句改变了 self.head，但并不影响之前（第三行）中的 self.head。
以下简单代码及运行结果可说明上述问题：
def minus(n):
    return -n
a = 1
b = a
print('a\'s old location is',id(a))
print('b\'s old location is',id(b))
a = 2
print('function minus(b)\'s operstion result is',minus(b))
print('a\'s new location is',id(a))
print('b\'s new location is',id(b))

结果：
a's old location is 140724734767952
b's old location is 140724734767952
function minus(b)'s operstion result is -1
a's new location is 140724734767984
b's new location is 140724734767952
10.28
递归过程中，如果只有 if 而没有 else，则 if 语句块中必须有可作为 base case 的动作，例如 problem solving 一书中的绘制树形和 sierpinski 三角形图案，前者的 base case 是画一条直线（主干或分支），后者是画一个三角形。
10.30
在调试 problem solving 一书中的迷宫程序时，一开始已经得出正确结果了，可是调整输入文件 maze2.txt 后报错“除以零”。几经调试报错行的代码都无果，判断问题应该出在输入文件里，最后发现是在现有行之下因使用回车键出现了空行，系统检测这些行的长度为0，所以出现“除以零”错误，删除这些空行之后解决问题。
11.3
用 locals 函数可以实现用循环方式创建多个对象实例，每个对象实例的名字依次排列，以下代码可以一次性创建 4 个 turtle 对象，名字分别为 t1 至 t4，然后依次添加进入一个列表中:
import turtle
tl = []
for i in range(1,5):
    name = 't' + str(i)
    locals()[name] = turtle.Turtle()
    tl.append(locals()[name])  
print(tl)

此处的 locals()[name] 实际上就是分别指代了 t1 至 t4,把迭代产生的实例放入列表有个好处，后期需要调用时可以用 list[i] 的索引方式进行调用。
11.6 
1、每个 class 可以设置该 class 下所有实例共用的属性。赋值方法是：
Dog.kind = 'canidae'
11.16
1、debug 时，要善用 print 语句输出中间结果，根据显示出的相关信息处理异常情况。
2、如果列表中没有某个索引，通过索引调用某个元素就会报错。
3、列表经过 slice 操作后，自身会发生变化，如果需要进行两次以上的 slice，应该用临时变量保留原始值。
4、可以用 done = False 变量来控制 while 循环，详见 problem solving 一书中的快速排序程序代码。
11.17
1、自己实现的快速排序方法，当需排序数字大于 160 时就会卡死，对比教材代码发现，在比较 a_list[0] 和 a_list[left_mark]  a_list[right_mark] 时，应该用 <= 或 >=，而不能只用 >,<，否则当列表中出现三个及以上重复数字的时候，就会陷入死循环。
2、
def search(item, a):
    print(a)
    if a[0] == item:
        print('a')
        return True
    else:
        return search(item, a[1:])
    return False
这段用递归方法实现的搜索代码中，倒数第二行必须有 return，因为最终目的是要输出 True 或者 False。
11.22
标准库 operator 可提供各种数学运算的函数，并且将这些函数赋值给变量：

import operator
fn = operator.add
print(fn(2,3))

结果为 4
12.1
try except 组合处理异常时，try 中出现错误后，可继续执行，而不会导致整个程序崩溃。这样可以有利程序的调试过程。
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
运行结果：
21.0
3.5
Error: Invalid argument.
None
42.0

def spam(divideBy):
return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
运行结果：
21.0
3.5
Error: Invalid argument.
因为出错后直接跳到 except 语句，而不会再返回，因此 print(spam(1)) 这个语句不会被执行！

Python uses references whenever variables must
store values of mutable data types, such as lists or dictionaries. For values
of immutable data types such as strings, integers, or tuples, Python vari-
ables will store the value itself.
对于可变类型（例如，列表和字典），会有以下效果
>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello!'
>>> spam
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
对可变类型的修改会造成连带变化，如果想避免，可以用以下方式复制原列表：
a=[1,2]
b=a[:]
a.append(3)
print(b)
结果是
[1,2]

或者使用 copy 模块：
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']

a=[1,2]
b=a.append(3)
print(b)
结果是
None
12.3
Using the  keys() ,  values() , and  items() methods, a  for loop can iterate
over the keys, values, or key-value pairs in a dictionary, respectively. Notice
that the values in the  dict_items value returned by the  items() method are
tuples of the key and value.