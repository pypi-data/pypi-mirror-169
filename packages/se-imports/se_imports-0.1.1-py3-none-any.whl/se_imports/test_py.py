# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:42
# @Author  : wyw
import shutil


#package_name 如果制作.whl , 自定义设置包，否则默认为包含代码的最近目录名
def test_se_project(src_dir = '/home/project',dst_dir = '/home/project_se' , package_name='serving'):
    from se_imports import se_project_crypto
    #目标文件夹存在则自动删除
    autoremove_dst_exists = False
    #删除空目录
    autoremove_dst_empty_dir = True
    #忽略复制文件，文件对工程运行没有用
    ignore = shutil.ignore_patterns('test','.git','.idea','setup.py')

    #package_name
    # 如果是pypi包，package_name 需要设置包名,否则可以设置None

    #加密接受规则
    accept_rules = ['serving/utils/*', 'serving/run*', 'serving/http_client/http*']


    se_project_crypto(
        src_dir,
        dst_dir,
        is_use_root_name=False,
        autoremove_dst_exists=False,
        autoremove_dst_empty_dir=True,
        ignore = ignore,
        rules = accept_rules,
        key=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        iv=bytes([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    )

def run():

    # demo
    import sys,os
    from se_imports import se_register_module
    #root_dir='/home/project_se'

    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))
    se_register_module(root_dir=root_dir)


    from serving.runner import main
    main()
