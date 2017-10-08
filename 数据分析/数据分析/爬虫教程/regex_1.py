# coding:UTF-8
#废话
import re

pattern = re.compile(r'\d+')
print pattern.findall('one1two2three3four4')  # return a result with a list
for m in re.finditer(pattern,'one1two2three3four4'):
    print m.group(),  # use a common to avoid to switch a new line