# regular expression
# regex expression: https://regex101.com/
import re

'''
正規表示比對流程
1. import re 
2. re.compile建立Regex物件
3. Regex.search('str') 找到符合條件字串回傳 match 物件；沒找到 回傳 noneType 物件
4. 呼叫 Match 的 group method 回傳符合條件的字串，只能回傳第一組找到的字串。
'''

# sent string into re.compile() and then return Regex pattern object.
# build a regular expression
'''
r: raw string
'''
phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d')


# compare Regex object
# Regex search method.
# search method return match object
mo = phoneNumRegex.search('My number is 2366-8685.')

# return phone number
print('Phone number found: ' + mo.group())

print('\n')
# use the bracket to classify and then use group to get the result
# 在正則式中用括號分組，再用group取各組使用
# 括號在正則式中為保留字
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')

# group usage
print(mo.group(1))

print(mo.group(2))

print(mo.group(0))

print(mo.group())

print('\n')

testAlphaRegex = re.compile(r'[my]')

str1 = 'sss  ddd'
mo1 = testAlphaRegex.search(str1)
print(mo1)
print()

str2 = 'aaaa 1234 bbbb cccc'
testAlpha = re.compile(r'\D\D\D\D')
mo2 = testAlpha.search(str2)
print(mo2)
print(mo2.group())
'''
print(mo2.group(0))
print(mo2.group(1))
print(mo2.group(2))
'''

print()

'''
用groups取得所有分組
'''

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('my number is 415-555-4114.')
print(mo.groups())

areaCode, mainNumber = mo.groups()
print('area code is ' + areaCode)
print('main code is ' + mainNumber)
print()

# 在正則式中，. ^ $ * + ? { } [ ] \ | ( ) 有特殊涵義
# 要加上轉義符號\ 才能當一個字元使用


'''
|字元稱作pipe (管道)，進行多個表示式比對
'''
print('pipe'.center(21, '='))
print()
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('123 Batman and Tina Fey. 456')
print(mo1.group())
mo2 = heroRegex.search(r'123 Tina Fey and Batman. 456')
print(mo2.group())
print()
'''
使用管道設定多個模式比對
'''
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
# group(1) return the first match string
print(mo.group(1))
print(mo.group(0))
'''
在index放 2 會出現index error
print(mo.group(2))
'''
print('\n')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search('Batmobile lost a wheel.Batman lost his mind.')
print(mo1.group())
print(mo1.group(1))

print('\n')
print(mo1.groups())


'''
問號為可選擇性比對
'''
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventure of Batman.')
print(mo1.group(), '\n')
mo2 = batRegex.search('The adventure of Batwoman.')
print(mo2.group(), '\n')


'''
自製範例
'''
diyRegex = re.compile(r'abc(def)?ghi')
mo_self1 = diyRegex.search('1111 abc')
print(mo_self1)
print(type(mo_self1))
mo_self2 = diyRegex.search('222 abc123ghi 555')
print(mo_self2)

'''
用*字號比對符合零次或多次
'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventure of Batman.')
print(mo1.group(), '\n')
mo2 = batRegex.search('The adventure of Batwoman.')
print(mo2.group(), '\n')
mo3 = batRegex.search('The adventure of Batwowowowoman.')
print(mo3.group(), '\n')

'''
用+號比對符合一次或多次， +號搜尋字串至少要出現一次
'''
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventure of Batman.')
# 用+號，mo1就會出noneType
print(mo1, '\n')
# -----------------------
mo2 = batRegex.search('The adventure of Batwoman.')
print(mo2.group(), '\n')
mo3 = batRegex.search('The adventure of Batwowowowoman.')
print(mo3.group(), '\n')


'''
用大括弧指定比對符合次數
'''
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('15555555555555HaHaHa')
print(mo1.group())

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('15555555555555HaHaHaHa4444Ha')
print(mo1.group())

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('Ha')
print(mo1)


