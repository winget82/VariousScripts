import win32com
from win32com import client
import re
import os

filepath = os.getcwd()

file = input('What is the filepath and name and extension of your excelfile?\n')
page_difference = int(input('what is your page difference for renumbering?\n'))
start_page = int(input('What is your starting page number (3 digits)?\n'))
visible = input('Do you want to see the changes as they happen? (Y/N)')
excel = win32com.client.Dispatch('Excel.Application')

if visible.upper() == 'Y':
    excel.Visible = True
else:
    excel.Visible = False

wb = excel.Workbooks.Open(file)

def numberThere(sheetname):
    return any(char.isdigit() for char in sheetname)

direction = 'forward'

if page_difference > 0:
    direction = 'backwards'

shtlst = []

for sh in wb.Sheets:
    oldName = sh.Name
    shtlst.append(oldName)
    excel.Worksheets(oldName).Activate()

    if page_difference < 0:
        if numberThere(oldName[-3:]) == True:
            oldNameUPPER = oldName.upper()
            if oldNameUPPER.find('(OLD)') <= 0 == False:
                if int(oldName[-3:]) >= int(start_page):
                    alpha = ''.join(filter(str.isalpha, oldName[0:5]))#or you can do ''.join(x for x in s if x.isalpha())
                    pgnumber = (re.findall("\d+", oldName) or ['000'])[0]#if this doesn't work do pgnumber = oldName[-5:]
                    #print(alpha + '-' + twonumber + '-' + pgnumber)
                    newpgnum = int(pgnumber) + int(page_difference)
                    formatted_newpgnum = "{:05}".format(newpgnum)
                    newName = (str(alpha) + str(formatted_newpgnum))
                    excel.ActiveSheet.Name = newName
                    excel.Worksheets(newName).Range('P54').Value = str(newpgnum)[-3:]
                    print("Old sheet name: " + oldName + "\tNew sheet name: " + newName)
                    #log file
                    with open('ws_rename_log.txt', 'a+', encoding='utf-8') as log_file:
                        log_file.write('Old filename: ' + oldName + '\t' + 
                        'New filename: ' + newName +'\n')

# THIS IS FOR RENAMING THE SHEETNAMES IN BACKWARDS ORDER:
print("The following pages are being passed to rename:\n(If error look here for issue)\n" + str(shtlst))
print("Removing 'Module1'")
shtlst.remove('Module1')

if direction == 'backwards':
    for oldName in reversed(shtlst):
        print("Sheetname being passed is: " + oldName) #here's the problem, the first thing returned is "Module1" wtf???
        excel.Worksheets(oldName).Activate()
        
        if numberThere(oldName[-3:]) == True:
            oldNameUPPER = oldName.upper()
            if oldNameUPPER.find('(OLD)') <= 0 == False:
                if int(oldName[-3:]) >= int(start_page):
                    alpha = ''.join(filter(str.isalpha, oldName[0:5]))#or you can do ''.join(x for x in s if x.isalpha())
                    pgnumber = (re.findall("\d+", oldName) or ['000'])[0]#if this doesn't work do pgnumber = sheetname[-5:]
                    #print(alpha + '-' + twonumber + '-' + pgnumber)
                    newpgnum = int(pgnumber) + int(page_difference)
                    formatted_newpgnum = "{:05}".format(newpgnum)
                    newName = (str(alpha) + str(formatted_newpgnum))
                    excel.ActiveSheet.Name = newName
                    excel.Worksheets(newName).Range('P54').Value = str(newpgnum)[-3:]
                    print("Old sheet name: " + oldName + "\tNew sheet name: " + newName)
                    #log file
                    with open('ws_rename_log.txt', 'a+', encoding='utf-8') as log_file:
                        log_file.write('Old filename: ' + oldName + '\t' + 
                        'New filename: ' + newName +'\n')

saveDoc = input("Would you like to save your changes? (Y/N):\n")

if saveDoc.upper() == 'Y':
    wb.Save()

closeDoc = input("Would you like to close the excel document and exit? (Y/N):\n")

if closeDoc.upper() == 'Y':
    wb.Close()
    excel.Quit()

print('DONE')
exit()
