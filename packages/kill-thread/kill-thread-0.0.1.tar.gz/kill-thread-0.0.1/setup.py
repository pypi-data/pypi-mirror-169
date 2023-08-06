from setuptools import setup

'''
安装Twine： 
    # pip install twine

打包发布：
    1.修改setup.py文件版本号
    2.删除历史发布目录dist、build
    3.使用setuptools打包: 
        # python setup.py sdist
        # python setup.py install 
    4.使用twine发布到pypi:
        # python -m twine upload dist/* 
    
参考文档：
    https://setuptools.readthedocs.io/en/latest/references/keywords.html
    https://packaging.python.org/tutorials/packaging-projects/#setup-args
    https://blog.csdn.net/xujing19920814/article/details/80374360

备注：
    需要setuptools工具配合twine工具才能使用markdown文档

快速上传：
    python pypi.py
'''

desc_doc = 'README.md'

setup(
    name='kill-thread',
    version='0.0.1',
    author='Jinghe Lee',
    author_email='jinghe_lee@163.com',
    url='https://github.com/JingheLee/KillThread.git',
    py_modules=['.kill_thread'],
    # packages=['ljh_example'],
    # scripts=['ljh_example.py'],
    # entry_points={
    #     'console_scripts': ['adb_init = ljh_example:init']
    # },
    # install_requires=[
    #     'requests'
    # ],
    description='只有一个功能，杀死线程！',
    long_description_content_type='text/markdown',
    long_description=open(desc_doc, encoding='utf-8').read(),
)
