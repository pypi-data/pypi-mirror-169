import os
import subprocess



pro_dir = str(input("请输入pyproject.toml文件同级目录："))
pan_fu = pro_dir.split(os.sep)[0]

dabao_str = r"""
执行了以下命令：
{}
cd {}
py -m build
twine upload dist/*
""".format(pan_fu, pro_dir)

def dabao():
    os.system("{}".format(pan_fu))
    os.system("cd {}".format(pro_dir))
    os.system(r"py -m build")
    os.system(r"twine upload dist/*")

def dabao_v2():
    subprocess.run("{}".format(pan_fu), shell=True, stdout=subprocess.PIPE)
    subprocess.run("cd {}".format(pro_dir), shell=True, stdout=subprocess.PIPE)
    subprocess.run(r"py -m build", shell=True, stdout=subprocess.PIPE)
    subprocess.run(r"twine upload dist/*", shell=True, stdout=subprocess.PIPE)

def dabao_v3():
    import subprocess

    cmd = "{}".format(pan_fu)
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()  # 等待子进程结束，并返回状态码；
    print(return_code)

    cmd = "cd {}".format(pro_dir)
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()  # 等待子进程结束，并返回状态码；
    print(return_code)

    cmd = "py -m build"
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()  # 等待子进程结束，并返回状态码；
    print(return_code)

    # cmd = "twine upload dist/*"
    # p = subprocess.Popen(cmd, shell=True)
    # return_code = p.wait()  # 等待子进程结束，并返回状态码；
    # p.terminate()

if __name__ == '__main__':
    print(dabao_str)
    # dabao_v2()
    dabao_v3()
    # subprocess.run("type nul>123.txt".format(pan_fu), shell=True, stdout=subprocess.PIPE)

# print(dabao_str)
# dabao_v3()