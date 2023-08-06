import os

def get_files(dir_path):
    r"""
    dir_path = C:\Users\Administrator\Desktop\rsgz
    返回文件列表
    """
    files_list = []
    for dirpath, dirnames, filenames in os.walk():
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            files_list.append(file)
    return files_list

def get_base_name(the_list):
    r"""
    the_list 是文件或者文件夹列表
    返回最简短文件列表或者文件夹列表
    """
    short_name_list = []
    for i in range(len(the_list)):
        short_name = the_list[i].split(os.sep)[-1]
        short_name_list.append(short_name)
    return short_name_list


if __name__ == '__main__':
    path = r"\\Mgkj\e\1金芒果DIY图片集"