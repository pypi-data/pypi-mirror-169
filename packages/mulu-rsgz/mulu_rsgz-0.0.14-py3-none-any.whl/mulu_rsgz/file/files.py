import os,re



def get_files(dir_path):
    r"""
    dir_path = C:\Users\Administrator\Desktop\rsgz
    返回文件列表
    """
    files_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
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

def compare_file(dir_fu, dir_zi):
    r"""
    文件比较文件
    返回 多出的部分列表
    """
    fu_set = set(get_base_name(get_files(dir_fu)))
    zi_set = set(get_base_name(get_files(dir_zi)))
    diff = list(fu_set.difference(zi_set))
    return diff

def paixu_file(file_list, jiangxu):
    r"""
    对文件列表 进行排序
    file_list = ['1.jpg', '10.jpg', '11.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']
    jiangxu = 1  降序
    jiangxu = 0  升序
    """
    if jiangxu:
        file_list.sort(key=lambda x: int(re.findall("\d+", x)[0]), reverse=True)  # 降序
    else:
        file_list.sort(key=lambda x: int(re.findall("\d+", x)[0]), reverse=False)  # 升序
    return file_list

def get_num_from_file(file_list):
    r"""
    获取文件列表中的数字
    file_list = ['32293black.jpeg', '32294blue.jpeg', '32295green.jpeg', '32296light blue.jpeg', '32297light green.jpeg', '32298orange.jpeg', '32299purple.jpeg', '32300red.jpeg', '32301white.jpeg', '32302yellow.jpeg']
    """
    return list(map(lambda x: re.findall("\d+", x)[0], file_list))

def get_not_number(file_list):
    r"""
    获取文件列表中 非数字部分
    file_list = ['32293black.jpeg', '32294blue.jpeg', '32295green.jpeg', '32296light blue.jpeg', '32297light green.jpeg', '32298orange.jpeg', '32299purple.jpeg', '32300red.jpeg', '32301white.jpeg', '32302yellow.jpeg']
    """
    return list(map(lambda x: re.findall("\D+", x)[0], file_list))

def remove_str(file_list , houzhui):
    r"""
    去除文件列表对应部分字符串
    file_list = ['black.jpeg', 'blue.jpeg', 'green.jpeg', 'light blue.jpeg', 'light green.jpeg', 'orange.jpeg', 'purple.jpeg', 'red.jpeg', 'white.jpeg', 'yellow.jpeg']
    """
    return list(map(lambda x:x.replace(houzhui, ""), file_list))

def get_bianhao_yanse(file_list, houzhui):
    r"""
    参数
    file_list = ['32293black.jpeg', '32294blue.jpeg', '32295green.jpeg', '32296light blue.jpeg',
                 '32297light green.jpeg', '32298orange.jpeg', '32299purple.jpeg', '32300red.jpeg', '32301white.jpeg',
                 '32302yellow.jpeg']
    调用：
    bianhao, yanse = get_bianhao_yanse(file_list, houzhui=".jpeg")

    """
    bianhao = get_num_from_file(file_list)
    new_list = get_not_number(file_list)
    yanse = remove_str(new_list, houzhui)
    return  bianhao, yanse

if __name__ == '__main__':
    path = r"\\Mgkj\e\1金芒果DIY图片集"
    file_list = ['1.jpg', '10.jpg', '11.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']
    print(paixu_file(file_list, jiangxu=0))
    file_list = ['32293black.jpeg', '32294blue.jpeg', '32295green.jpeg', '32296light blue.jpeg',
                 '32297light green.jpeg', '32298orange.jpeg', '32299purple.jpeg', '32300red.jpeg', '32301white.jpeg',
                 '32302yellow.jpeg']
    bianhao, yanse = get_bianhao_yanse(file_list, houzhui=".jpeg")
    print(bianhao)
    print(yanse)