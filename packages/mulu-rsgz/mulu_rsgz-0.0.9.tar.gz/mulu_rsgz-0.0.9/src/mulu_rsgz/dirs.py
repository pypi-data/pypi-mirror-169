import os
from files import get_base_name




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
     目录比较目录
    返回 父列表比子列表多出的一部分  返回 多出的部分列表
    1 子列表是父列表一部分

    """
    fu_set = set(get_base_name(get_dirs(dir_fu)))
    zi_set = set(get_base_name(get_dirs(dir_zi)))
    diff = list(fu_set.difference(zi_set))
    return diff

def mulu_jiegou(path, indent = 0, maxi = -1):
    '''
        按文件类型递归输出目录结构
        :param path:   str 文件路径
        :param indent: int 首次缩进空格(默认为 0，一般不用改变)
        :param maxi:   int 最大展开层数(默认为 -1，表示全部展开)
    '''
    if maxi != 0:
        try:
            lsdir = os.listdir(path)
        except PermissionError:   # 权限不够的文件  不处理
            pass
        else:
            dirs = [item for item in lsdir if os.path.isdir(os.path.join(path, item))]
            files = [item for item in lsdir if os.path.isfile(os.path.join(path, item))]
            for item in dirs:
                print(' ' * indent, '+', item)
                mulu_jiegou(os.path.join(path, item), indent + 4, maxi - 1)
            for item in files:
                print(' ' * indent, '-', item)

if __name__ == '__main__':
    path = r"C:\Users\Administrator\Desktop\111"
    mulu_jiegou(path, indent = 0, maxi = -1)

