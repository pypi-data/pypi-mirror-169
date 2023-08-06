# @Time    : 2021/11/10 20:23
# @Author  : tk
# @FileName: py_code.py

import os
import shutil
import se_import
from pathlib import PurePath
import pickle
from pprint import pprint


__all__ = ["se_project_crypto"]

def rm_empty_folder(path):
    if os.path.isdir(path):
        path_list=os.listdir(path) # 列出该目录的文件和目录，如果目录为空返回空列表
        while path_list:
            item = path_list.pop()
            # print(os.path.join(path,item)) # 拼接 路径
            rm_empty_folder(os.path.join(path,item))
        if not os.listdir(path): # 删除空目录
            os.rmdir(path)
            print(f"del empty folder{path}")

'''
    src_dir 源工程路径
    dst_dir 加密工程路径
    package_name 最顶层python模块
    autoremove_dst_exists 目标路径存在是否自动删除
    autoremove_dst_empty_dir 生成的目标路径空文件夹是否自动删除
    ignore 复制忽略文件  shutil.ignore_patterns('test','.git','.idea','setup.py')
    accept_rules 加密规则，起始必须是根模块名
        例子 ['serving/utils/*','serving/run*','serving/http_client/http*']
        None 则接受所有
    key des key
    iv des iv
'''
def se_project_crypto(
    src_dir,
    dst_dir,
    is_use_root_name,
    accept_rules=None,
    autoremove_dst_exists=False,
    autoremove_dst_empty_dir=True,
    ignore = shutil.ignore_patterns('test','.git','.idea','setup.py'),
    key=bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    iv=bytes([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
):


    src_dir = os.path.abspath(src_dir)
    dst_dir = os.path.abspath(dst_dir)


    if autoremove_dst_exists and os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)

    shutil.copytree(src_dir,dst_dir,ignore=ignore)

    file_list = []
    filemeta_map = {}
    fp_pos = 0



    package_name = os.path.split(dst_dir)[-1]



    for root,dirs,filename_list in os.walk(dst_dir):
        for filename in filename_list:
            if not filename.endswith('.py'):
                continue
            file_src = os.path.join(root, filename)

            if accept_rules is not None:
                p = PurePath(file_src)
                flag = False
                for item in accept_rules:
                    if p.match(item):
                        flag = True
                        break
                if not flag:
                    continue
            b = se_import.dump_module_to_desfile(file_src,key,iv)
            if not b:
                print('warning ' ,file_src, ' maybe an empty file')
            file_list.append((file_src,b))

            my_file_src = os.path.abspath(file_src)
            my_file_src = my_file_src[len(dst_dir)+1:]

            my_file_src = my_file_src[0:-3]
            my_file_src = my_file_src.replace('\\','/')
            name = my_file_src.replace('/', '.')

            if is_use_root_name:
                name = package_name + '.' + name


            is_package = name.endswith('.__init__')
            if is_package:
                name = name[:-9]
            filemeta_map[name] = {
                'name': name,
                'src': my_file_src + '.py',
                'size': len(b) if b else 0,
                'pos': fp_pos,
                'is_package': is_package
            }
            fp_pos += len(b) if b else 0

    print('package_name:', package_name)
    for k,v in filemeta_map.items():
        print(k,v)


    with open(os.path.join(dst_dir,'.__data__.pys'), mode='wb') as f:
        hdr = pickle.dumps((package_name, accept_rules, filemeta_map))
        hdr_size = len(hdr)
        b_hdr_size = hdr_size.to_bytes(4,byteorder='little',signed=False)
        f.write(b_hdr_size)
        f.write(hdr)

        for item in file_list:
            file_src = item[0]
            b = item[1]
            if b:
                f.write(b)
            os.remove(file_src)


    if autoremove_dst_empty_dir:
        rm_empty_folder(dst_dir)