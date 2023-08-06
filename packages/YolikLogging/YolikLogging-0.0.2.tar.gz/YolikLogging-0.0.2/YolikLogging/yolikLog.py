import time
import inspect
from colorama import init, Fore
import leveldb

class YolikLog(object):
    def __init__(self,islog=False):
        self.db = leveldb.LevelDB("../scripts/log") if islog else None

    def toLog(self,content):
        self.db.Put(content.split("19")[0].encode(),content.encode())

    def yolikLog(self,content,level="INFO",tolog=False):
        if level=="INFO":
            TN = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            init(autoreset=True)
            prefix = Fore.LIGHTCYAN_EX + TN + Fore.RESET + " "
            #打印所在方法名
            prefix += Fore.LIGHTYELLOW_EX + inspect.stack()[1][3]  + Fore.RESET + " "
            prefix += Fore.LIGHTGREEN_EX + level + Fore.RESET + " "
            print(prefix + content)
        elif level=="ERROR":
            TN = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            init(autoreset=True)
            prefix = Fore.RED + TN + Fore.RESET + " "
            #打印所在方法名
            prefix += Fore.RED + inspect.stack()[1][3] + Fore.RESET + " "
            prefix += Fore.RED + level + Fore.RESET + " "
            content = Fore.LIGHTRED_EX + content + Fore.RESET
            print(prefix + content)
        else:
            print(content)
        if tolog:
            self.yolikLog(content,level=level,tolog=False)
            self.toLog(content)


def func():
    yoliklog("test","INFO")

yoliklog = YolikLog().yolikLog



