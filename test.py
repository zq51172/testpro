# result=0
# for i in range(101):
#     print(i)
#     result=result+i
# print(result)

# result=0
# for i in range(101):
#     if i%2==0:
#        result=result+i
# print(result)


# result=0
# for i in range(2,101,2):
#     print(i)
#     result=result+i
# print(result)


# def method(a):
#
#     print(a)
#
#     return a+2
#
# print(method(1))

import pytest
from hamcrest import *


def test_hamcrest():
    # assert_that(10, equal_to(9),"这是一个提示")

    # assert_that(13,close_to(10,2))

     assert_that("contains some string",contains_string("string"))