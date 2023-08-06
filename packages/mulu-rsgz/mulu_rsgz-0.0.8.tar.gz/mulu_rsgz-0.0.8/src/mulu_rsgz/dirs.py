import os
from .files import get_files, get_base_name

def get_dirs(dir_path):
    r"""
    返回所有的目录列表
    """
    dir_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for dirname in dirnames:
            the_dir = os.path.join(dirpath, dirname)
            dir_list.append(the_dir)
    return dir_list

def compare_dir(dir_fu, dir_zi):
    r"""
    返回 父列表比子列表多出的一部分
    子目录之间不能有重复的文件
    1 子列表是父列表一部分
    返回 多出的部分列表
    """
    fu_set = set(get_base_name(get_files(dir_fu)))
    zi_set = set(get_base_name(get_files(dir_zi)))
    diff = list(fu_set.difference(zi_set))
    return diff