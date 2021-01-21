import yaml
import os
# yaml_str = """
# name: 一条大河
# age: 1956
# job: Singer
# """
#os.mkdir("d:/testpro/b/yaml_test.yaml")

#os.removedirs("d:/testpro/b/yaml_test.yaml")

# y = yaml.load(yaml_str, Loader=yaml.SafeLoader)
# print(y)


# with open("d:/testpro/yaml_test.yaml", 'r', encoding='utf-8') as ymlfile:
#     cfg = yaml.load_all(ymlfile, Loader=yaml.SafeLoader)
#     for data in cfg:
#         print(data)


# json_data = {'name': '一条大河',
#              'age': 1956,
#              'job': ['Singer','Dancer']}
#
# y = yaml.dump(json_data, default_flow_style=False).encode('utf-8').decode('unicode_escape')
# print(y)

json_data = {'name': '一条大河',
             'age': 1956,
             'job': ['Singer', 'Dancer']}
with open('d:/testpro/yaml_test.yaml', 'w',encoding='utf-8') as f:
    y = yaml.dump(json_data ,f)
    print(y)