import psutil
import os

def lock_all_apps():
    for proc in psutil.process_iter():
        try:
            proc_name = proc.name()
            if proc_name.endswith(".exe"):
                os.system(f'taskkill /F /IM {proc_name}')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == '__main__':
    lock_all_apps()
