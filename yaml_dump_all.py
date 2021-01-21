import yaml

obj1 = {"name": "river", "age": 2019}
obj2 = ["Lily", 1956]
obj3 = {"gang": "ben", "age": 1963}
obj4 = ["Zhuqiyu", 1994]

with open('D:/testpro/yaml_write_all.yaml', 'w', encoding='utf-8') as f:
    y = yaml.dump([obj1, obj2, obj3, obj4], f)
    print(y)

with open('D:/testpro/yaml_write_all.yaml', 'r') as r:
    y1 = yaml.load(r, Loader=yaml.SafeLoader)
    print(y1)