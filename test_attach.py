import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段html body块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

def test_attch_photo():
    allure.attach.file("D:/testpro/b/1.jpg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)




