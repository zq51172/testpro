# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5

#
#


import requests

# r= requests.get("http://www.baidu.com")
#
# print(r.status_code)
#
# print(r.text)
#
r= requests.post("http://httpbin.org/post",data={'key':'value'})
print(r.text)

