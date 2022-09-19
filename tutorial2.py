import re
'''
貪婪比對 vs 非貪婪比對
greedy預設返回最長符合比對的字串
non greedy預設返回最短符合比對的字串
Regex預設greedy
non-greedy
'''

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# 在大括弧後面加上?，即改為non greedy
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
print()

'''
findall返回所有match物件
'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# findall return list
mo1 = phoneNumRegex.findall('Cell: 415-555-99999 Work: 212-555-0000')
print(mo1)


# 加上括弧，return tuple
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   # have a group
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-666-0000')
print(mo2)
print()

'''
自建字元分類
[]
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
print()
'''
^字元和$字元 比對文字起始處 比對文字結束處
'''
beginWithHello = re.compile(r'^Hello')
print(beginWithHello.search('Hello World!'))
print(beginWithHello.search('He said hello'))
print()

# 比對最末尾是否是數字
endWithHello = re.compile(r'\d$')
mo3 = endWithHello.search('Your number is 42')

print(mo3.group())
print()


'''
^字元中間放\類型，最末尾再加上 + $，才能用作找開頭跟結尾
'''
wholeStringIsNum = re.compile(r'^\d+$')
mo4 = wholeStringIsNum.search('13579xyz246810')
print(mo4, '\n')

str1 = '12345678'
mo5 = wholeStringIsNum.search(str1)
print(mo5, '\n')
print(type(mo5.group()))
print(mo5.group(), '\n')


testPlusUsage = re.compile(r'^\w+$')
mo6 = testPlusUsage.search('abc555abc')
print(mo6)


'''
萬用字元
.*
'''

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo7 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo7.group())

'''
.* 預設貪婪比對
.*? 非貪婪比對
'''
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<to serve man> for dinner.>')
print(mo.group(), '\n')

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<to serve man> for dinner.>')
print(mo.group(), '\n')

'''
運用.字元找出換行符號外之字串
'''
noNewlineRegex = re.compile(r'.*')
mo8 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo8.group(), '\n')

'''
re.DOTALL
比對時找出所有內容
'''
newlineRegex = re.compile(r'.*', re.DOTALL)
mo9 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\n')
print(mo9.group(), '\n')


'''
不區分大小寫
'''
robocop = re.compile(r'robocop', re.I)
mo10 = robocop.search('Robocop is part man, part machine, all cop.')
print(mo10.group(), '\n')

mo11 = robocop.search('ROBOCOP protects the innocent.')
print(mo11.group(), '\n')

print(robocop.search('Al, why does your programming book talk about robocop so much?').group(), '\n')


'''
sub()取代字串
'''
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
agentNamesRegex = re.compile(r'Agent (\w)\w*')
subInstance = agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a '
                                            'double agent.')
print(subInstance, '\n')


'''
管理複雜正規式
多行呈現 加上註解
'''
phoneRegex = re.compile(r'''
    (\d{3}|(\d{3}\))?    # area code
    (\s|-|\.)?           # separator
    \d{3}                # first 3 digits
    (\s|-|\.)            # separator
    \d{4}                # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  #extension
    )''', re.VERBOSE)


'''
re.IGNORECASE
re.DOTALL
re.VERBOSE
|管道字元 組合
'''

# 正規式不區分大小寫 比對時包含換行符號
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)


someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
