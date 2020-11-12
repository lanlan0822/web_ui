# 自建装饰器  可方便用例封装
from base.base_option import BaseOption
''' 只要用例运行  不检测是否正常始终截图'''
def get_image_all(func):
    def get_image1(self,*args,**kwargs):
        func(self,*args,**kwargs)
        BaseOption(self.dr).base_get_image(func.__name__)
    return get_image1
