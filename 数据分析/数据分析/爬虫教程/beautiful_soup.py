# coding: UTF-8
from bs4 import BeautifulSoup
import bs4
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,"lxml")
# print soup.prettify()  # 这个是美化的意思

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#
# Tag
# NavigableString
# BeautifulSoup
# Comment

# 1.这个是其中的Tag一种结构
# print type(soup.p)
# print soup.a
# print soup.html
# print soup.p.attrs
# print type(soup.p.attrs)
# print soup.p.get("class")
# print soup.p['class']
# # we can change these attributes!
# soup.p['class'] = "hh"
# print soup.p
# del soup.p['class']
# print soup.p

# 2.navigableString
# we can use this to get that content easily
# print soup.p.string
# print type(soup.p.string)  # note that NavigableString instead of  typical string

# 3.Beautiful soup BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型
# print soup.name
# print soup.attrs
# print type(soup.name)

# 4.Comment omment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
print soup.a
print soup.a.string
print type(soup.a.string)
# 另外我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下

if type(soup.a.string)== bs4.element.Comment:
    print soup.a.string
