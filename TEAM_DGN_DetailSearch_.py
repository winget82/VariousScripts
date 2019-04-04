#http://cyluun.github.io/blog/manipulating-python-oswalk
import os
from datetime import datetime
import subprocess
from colorama import init
init()
from colorama import Fore, Back, Style

fileToSearch = ''
loop = True

while loop == True:
    folderToSearch = input("please enter the Division/Subdivision you would like to open from: ")
    rootFldr = 'Y:\\team\\' + folderToSearch.title()
    suffix = '.DGN'
    fileToSearch = input("Please enter the DGN file page ### to open (last 3 digits of file name {leave empty for all}): ") + suffix
    filepaths = []
    folderpaths = []

    for root, dirs, files in os.walk(rootFldr):

        #to get list of files with filepath:
        for name in files:
            #print(os.path.join(name))
            if fileToSearch in name.upper():
                filepaths.append(os.path.join(root, name))

    #print list of detail pages in directory
    print(Fore.GREEN + '\n')
    print(filepaths)
    print('\n')

    #last modified times
    index = 0
    for i in filepaths:
        try:
            mtime = os.path.getmtime(i)
        except OSError:
            mtime = 0
        last_modified_date = datetime.fromtimestamp(mtime)
        print(Fore.CYAN + str(index) + ' - ' + i + ' - ' + str(last_modified_date))
        index += 1

    print(Style.RESET_ALL)

    t = True
    x = []
    while t == True:
        x = input("\nwhich index would you like to open? (or 999 to exit...) ")
        x = x.split(',')

        if x == '999':
            exit()
        else:
            for i in x:
                ii = int(i)
                print('\nOpening ' + filepaths[ii])
                subprocess.call(["C:\\Program Files (x86)\\Bentley\\MicroStation V8i (SELECTseries)\\MicroStation\\ustation.exe",
    				 "-wr\\\\pat to Workspace", filepaths[ii]])
            
        z = input("Would you like to open another from the current list? (Y/N)\n")
        if z.upper() == 'Y':
            t = True
        else:
            t = False
