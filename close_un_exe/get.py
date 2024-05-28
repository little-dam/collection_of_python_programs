import psutil
import os
import sys

def get_non_system_processes():
    # 获取所有进程信息
    processes = [(p.pid, p.name()) for p in psutil.process_iter(['pid', 'name'])]
    # 过滤掉系统进程
    non_system_processes = [pid_name for pid_name in processes if not pid_name[1].startswith('System')]
    return non_system_processes

def print_processes(processes):
    # 打印进程及其标号
    for idx, (pid, name) in enumerate(processes, start=1):
        print(f"{idx}. {name} ({pid})")

processes = get_non_system_processes()
print_processes(processes)
