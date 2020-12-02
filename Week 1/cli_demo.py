import json
import os

welcome_msg = ' 欢迎来到中药记录系统 v0.1 '
print(welcome_msg.center(80, '='))

result = {}

# Questions
name = input('中药名：')
pinyin = input('拼音：')
prop_taste = input('性味：')
jingluo = input('归经：')

result['name'] = name
result['name_pinyin'] = pinyin
result['property_taste'] = prop_taste
result['jingluo'] = jingluo

print(' 保存数据 '.center(80, '-'))
path = input('储存位置：')
data = json.dumps(result)

with open(os.path.join(path, 'data.json'), 'w') as f:
    f.write(data)
    print('保存成功')

print(' 结束 '.center(80, '='))
