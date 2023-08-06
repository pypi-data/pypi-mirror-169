# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 14:25
# @Author  : wyw
import copy
import os
import sys
import se_import
from pathlib import PurePath
import pickle

'''
   注册运行解析器
        register_module(root_dir)
        root_dir 加密工程所在目录，如下所示 /home/project_se
        1.
        /home/project_se
                    script
                          run.sh #启动脚本
                          ...
                    serving # 源码模块所在目录
                                ...
                          utils
                                ...
                          runner.pys
'''

from collections import namedtuple

class SE_Importer:
    def __init__(self,root_dir):
        root_dir = os.path.abspath(root_dir)
        self.root_dir = root_dir
        with open(os.path.join(self.root_dir, '.__data__.pys'),mode='rb') as f:
            b_hdr_size = f.read(4)
            hdr_size = int.from_bytes(b_hdr_size,byteorder='little',signed=False)
            b_hdr = f.read(hdr_size)

        package_name,rules,filemeta_map = pickle.loads(b_hdr)

        self.hdr_size = hdr_size + 4

        for idx in range(len(rules)):
            rules[idx] = rules[idx].replace('/', '.')
            rules[idx] = rules[idx].replace('\\', '.')
        self.package_name = package_name
        self.se_accept_rules = rules
        self.filemeta_map = filemeta_map
        self.mapper = {}

    def get_file_info(self,fullpath, path):
        is_sub_object =False
        if fullpath in self.filemeta_map:
            filemeta = self.filemeta_map[fullpath]
        else:
            path_item = fullpath.rpartition('.')
            base_item = path_item[0]
            l_item = path_item[-1]
            if l_item == '':
                return None
            if base_item not in self.filemeta_map:
                return None
            filemeta = self.filemeta_map[base_item]
            if not filemeta["is_package"]:
                return None
            is_sub_object = True

        return  {
            'name' : filemeta["name"],
            'file': os.path.join(self.root_dir, '.__data__.pys'),
            'src':  self.root_dir + '/' + filemeta["src"],
            'pos': filemeta['pos'] + self.hdr_size,
            'size': filemeta['size'],
            'is_package' : filemeta["is_package"],
            'is_sub_object': is_sub_object,
        }
    def find_from_cache(self, fullpath, path):
        if fullpath not in self.mapper:
            p = path._path if path is not None and hasattr(path, '_path') else path
            real_path = p[0] if p and len(p) else self.root_dir
            file_info = self.get_file_info(fullpath, real_path)
            if file_info is None:
                return None
            self.mapper[fullpath] = file_info
        else:
            file_info = self.mapper[fullpath]
        return file_info

    def find_module(self, fullpath , path=None):

        if self.se_accept_rules is not None:
            p = PurePath(fullpath)
            p1 =  PurePath(self.package_name +'.' + fullpath) if self.package_name is not None else None
            p2 = PurePath(fullpath + '.__init__')
            p3 = PurePath(fullpath.rpartition('.')[0] + '.__init__') if fullpath.rfind('.') > 0 else None
            flag = False
            for item in self.se_accept_rules:
                if p.match(item) or p2.match(item) or (p3 and p3.match(item)) :
                    flag = True
                    break
                if p1 and p1.match(item):
                    flag = True
                    break


            if not flag:
                return None
        file_info = self.find_from_cache(fullpath,path)
        if self.package_name and not file_info:
            file_info = self.find_from_cache(self.package_name +'.' + fullpath, path)
        return self if file_info is not None else None


    def load_module(self, fullpath):
        base_item = fullpath.rpartition('.')[0]
        l_item = fullpath.rpartition('.')[-1]
        if fullpath in sys.modules:
            return sys.modules[fullpath]
        if l_item !='' and base_item in sys.modules:
            if l_item in sys.modules[base_item].__dict__:
                return sys.modules[base_item].__dict__[l_item]

        if fullpath in self.mapper:
            filemeta = self.mapper[fullpath]
        else:
            filemeta = self.mapper[self.package_name +'.' + fullpath]

        name = filemeta['name']
        file = filemeta['file']
        src = filemeta['src']
        file_size = filemeta['size']
        file_pos = filemeta['pos']
        is_package = filemeta['is_package']
        is_sub_object = filemeta['is_sub_object']
        if file_size > 0:
            with open(file, mode='rb') as f:
                f.seek(file_pos, 0)
                file_data = f.read(file_size)
        else:
            file_data = bytes("", encoding='utf-8')

        final_module = None
        if is_package:
            module = se_import.load_module(name, "", src)
            module.__path__ = name.replace('.', '/')
            sys.modules[fullpath] = module

        if is_package and is_sub_object:
            if file_size > 0:
                module = se_import.load_module_from_aesfile(name, file_data, src)
                if module is None:
                    raise Exception(filemeta)
                module.__path__ = name.replace('.', '/')
                sys.modules[base_item] = module
            if l_item in module.__dict__:
                sub_module = module.__dict__[l_item]
                sys.modules[fullpath] = sub_module
                final_module = sub_module
            else:
                if module is None:
                    module = se_import.load_module_from_aesfile(name, file_data, src)
                sys.modules[fullpath] = module
        else:
            if file_size > 0:
                module = se_import.load_module_from_aesfile(name, file_data, src)
                if module is None:
                    raise Exception(filemeta)
                if is_package:
                    module.__path__ = name.replace('.', '/')
            sys.modules[fullpath] = module

        if final_module is None:
            final_module = sys.modules.get(fullpath,None)
        return final_module
'''
root_dir 所在目录
'''
def se_register_module(root_dir : str):
    sys.meta_path.insert(0,SE_Importer(root_dir))