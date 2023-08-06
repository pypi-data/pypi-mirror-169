import setuptools #导入setuptools打包工具
 
from distutils.core import setup
 
setup(
    name='qiaotest2022',  # 对外模块的名字
    version='1.0.0',  # 版本号
    description='测试本地发布模块',  # 描述
    author='dgwqqqqq',  # 作者
    author_email='aaaa@qq.com',
    py_modules=['qiaotest2022.example'],  # 要发布的模块
)

