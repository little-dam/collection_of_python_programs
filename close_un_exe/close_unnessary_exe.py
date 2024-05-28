import psutil
import subprocess
import os
import sys

###################################################
# 假设文件名为 'file.txt'
filename = 'New Text Document.txt'

# 初始化一个空列表来存储提取的信息
extracted_info = []

# 打开文件并逐行读取
with open(filename, 'r') as file:
    for line in file:
        # 使用 split 方法按空格分割每一行，并获取第二部分
        parts = line.split()
        if len(parts) >= 2:
            extracted_info.append(parts[1])
#####################################################

#获取目前正在运行的列表
def get_non_system_processes():
    # 获取所有进程信息
    processes = [(p.pid, p.name()) for p in psutil.process_iter(['pid', 'name'])]
    # 过滤掉系统进程，并只提取进程名称
    non_system_processes = [name for pid, name in processes if not name.startswith('System')]
    return non_system_processes
# 关闭不在列表extracted_info中的程序
def close_processes(list_A, extracted_info):
    for exe in list_A:
        if exe not in extracted_info:
            try:
                subprocess.check_call(['taskkill', '/F', '/IM', exe])
                print(f'Closed process: {exe}')
            except subprocess.CalledProcessError as e:
                print(f'Failed to close process: {exe}, error: {e}')

########################################################################
# 获取正在运行的非系统exe程序列表A
list_A = get_non_system_processes()

# 关闭那些只在A中但不在B中的程序
close_processes(list_A, extracted_info)


