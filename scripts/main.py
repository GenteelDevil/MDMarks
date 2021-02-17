import time
import datetime
import os
import re

# 1. find all md file
def findAllMDFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.md'):
                fullname = os.path.join(root, f)
                yield fullname

# 2. judge modify time of file
def judgeModifyTime(path):
    today = datetime.date.today()
    modifytime = os.path.getatime(path)
    modifytime = datetime.datetime.fromtimestamp(modifytime)
    modifytime = modifytime.strftime("%Y-%m-%d")
    print(modifytime)

# 3. get mark list and pend to file
def pendMDMark(path):
    oldfopen = open(path, 'r')
    newfopen = open(path, 'a')
    for eachline in oldfopen:
        if re.match("([Qu：]|[Cm：])", eachline.strip()):
            newfopen.write(eachline)

if __name__ == '__main__':
   for i in findAllMDFile('./'):
       print(i)
       pendMDMark(i)