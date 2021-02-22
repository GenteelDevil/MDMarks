# -*- coding: utf-8 -*-
import time
import datetime
import os
import re

mdpath = "./"

# 1. find all md file
def findAllMDFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.md'):
                fullname = os.path.join(root, f)
                yield fullname

# 2. judge modify time of file
def judgeModifyTime(path):
    modifytime = os.path.getatime(path)
    modifytime = datetime.datetime.fromtimestamp(modifytime)
    modifytime = modifytime.strftime("%Y-%m-%d")
    print(modifytime)

# 3. get mark list and pend to file
def pendMDMark(path):
    orign = []
    marks = []
    marks_flag = False
    with open(path, "r") as f_r:
        lines = f_r.readlines()
        
    with open(path, "w") as f_w:
        for line in lines:
            f_w.write(line)
            if re.match("(Qu：)|(Cm：)|(Td：)", line):
                marks.append("- " + line.strip() + "\n")
                continue
            if re.match("## Marks*", line):
                marks_flag = True
                break
        
        if marks_flag == False:
            f_w.write("\n## Mark\n")
        f_w.writelines(marks)



# main
def main():
    today = datetime.date.today()
    print(today)
    for each in findAllMDFile(mdpath):
        print(each)
        pendMDMark(each)
    

if __name__ == '__main__':
    main()