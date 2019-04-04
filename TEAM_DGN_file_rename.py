#Rename files in TEAM folder - copy the files to your computer
#and rename the copies, incase a mistake happens
import os
import re
#copy this file to the folder that you are renaming files in so that
#the filepath is set correctly
filepath = os.getcwd()
#print(filepath)

page_difference = int(input('what is your page difference for renumbering? '))
start_page = int(input('What is your starting page? '))

def hasNumbers(filename):
	return any(char.isdigit() for char in filename)

if page_difference > 0:

	for filename in reversed(os.listdir(filepath)):
		if filename.endswith(".dgn") or filename.endswith(".DGN"):
			if hasNumbers(filename) == True:
				if int(filename[-7:-4]) >= int(start_page):
					print('Old filename: ' + filename)
					alpha = ''.join(filter(str.isalpha, filename[0:5]))#or you can do ''.join(x for x in s if x.isalpha())
					number = (re.findall("\d+", filename) or ['000'])[0]
					number = int(number) + int(page_difference)
					#print(alpha)
					#print(number)
					new_num = "{:05}".format(number)
					new_filename = alpha + new_num + '.DGN'
					print('Your new filename is: ' + new_filename)
					os.rename(filename, new_filename)
					with open('file_rename_log.txt', 'a+', encoding='utf-8') as log_file:
						log_file.write('Old filename: ' + filename + '\n' + 
						'Your new filename is: ' + new_filename +'\n')


if page_difference < 0:

	for filename in os.listdir(filepath):
		if filename.endswith(".dgn") or filename.endswith(".DGN"):
			if hasNumbers(filename) == True:
				if int(filename[-7:-4]) >= int(start_page):
					print('Old filename: ' + filename)
					alpha = ''.join(filter(str.isalpha, filename[0:5]))#or you can do ''.join(x for x in s if x.isalpha())
					number = (re.findall("\d+", filename) or ['000'])[0]
					number = int(number) + int(page_difference)
					#print(alpha)
					#print(number)
					new_num = "{:05}".format(number)
					new_filename = alpha + new_num + '.DGN'
					print('Your new filename is: ' + new_filename)
					os.rename(filename, new_filename)
					with open('file_rename_log.txt', 'a+', encoding='utf-8') as log_file:
						log_file.write('Old filename: ' + filename + '\n' + 
						'Your new filename is: ' + new_filename +'\n')

#need to make a try except for issues
#figure out a way to renumber the text within dgns
