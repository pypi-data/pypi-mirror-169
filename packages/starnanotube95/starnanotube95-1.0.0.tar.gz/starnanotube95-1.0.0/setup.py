from distutils.core import setup


setup(
    name='starnanotube95',  # 对外模块的名字
    version='1.0.0',  # 版本号
    description='碳纳米管手性解析模块',  # 描述
    author='Spectre Lee',  # 作者
    url="http://skyfalco.xyz/lrm",
    author_email='lxwk1spectre@pku.edu.cn',
    py_modules=['starnanotube95.nt'],  # 要发布的模块
)