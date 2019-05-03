import fitz
import pyperclip as p
import os
import datetime
from datetime import datetime as dt

"""
This is a script to copy PDFs for a page range from GISTOM folder into TEAM manual PDF while deleting
that same page range from the TEAM manual.  Then the script will save the PDF and make a copy of it
renaming the archive copy with the same filename followed by todays date YYYY-MM-DD ex: 'Lakes 2019-05-01'.

FROM PyMuPDF docs see:
# https://pymupdf.readthedocs.io/en/latest/tutorial/#modifying-creating-re-arranging-and-deleting-pages
# https://github.com/pymupdf/PyMuPDF/wiki/Inserting-Pages-from-other-PDFs
"""
print("Please copy file path of GISTOM folder to your clipboard now...")

daysAgo = int(input("How many days (back from today) would you like to insert? "))

# GISTOM folder (from clipboard)
folderGISTOM = p.paste()
os.chdir(folderGISTOM)

# Get today
today = dt.now()

# Get beginning date for files to insert into current PDF
beginDate = today - datetime.timedelta(days=daysAgo)

# GET DESTINATION AND INSERTION PDF FILES - CURRENTLY SET UP FOR ONLY ONE INSERTION PDF
destinationFile = input("What is the PDF DESTINATION file & filepath? ")

# List of files in GISTOM folder
filepaths = []

# List of PDF files to be inserted into destination PDF file (between today's date and begin date)
pdfsToInsert = []

for root, dirs, files in os.walk('.', topdown=True):
    dirs.clear() # with topdown true, this will prevent walk from going into subs
    for name in files:
        if name[-4:].upper() == '.PDF':
            filepaths.append(os.path.join(root, name))
print(filepaths)

# Print out list of files in folderGISTOM with Date Modified
print("\n\nThe following pdfs will be inserted:")

for i in filepaths:
    try:
        mtime = os.path.getmtime(i)
    except OSError:
        mtime = 0

    last_modified_date = dt.fromtimestamp(mtime)

    if last_modified_date > beginDate:
        pdfsToInsert.append(i)
        print(i + ' - ' + str(last_modified_date))
print('\n')

# GET PAGE RANGE
correct = ''
while (correct.upper() != 'Y'):

    pageRangeStart = input("What is the beginning TEAM Manual page of page range to replace? ")
    pageRangeEnd = input("What is the ending TEAM Manual page of page range to replace? ")
    print("Beginning page = " + pageRangeStart + " & Ending page = " + pageRangeEnd)
    correct = input("Is this correct? (Y or N)")

    # Set TEAM pages
    teamPgRngSt = int(pageRangeStart)
    teamPgRngEn = int(pageRangeEnd)

    if teamPgRngSt<teamPgRngEn and correct.upper() == 'Y':
        print('Yes')

    elif correct.upper() == 'N':
        print('No')

    else:
        correct = 'N'
        print('Check your page numbers...')

# Open destination PDF
destinationPDF = fitz.open(destinationFile) # must be a PDF

# This loops through pdfsToInsert List and sets current page to the final 3 digits from pdf File then deletes that page
# from the destination pdf then inserts that page into the destination pdf
for insertFile in pdfsToInsert:
    if (int(insertFile[-7:-4]) >= teamPgRngSt) and (int(insertFile[-7:-4]) <= teamPgRngEn): # verify inside page range
        currentTEAMpage = int(insertFile[-7:-4]) # sets current page #
        destinationPDF.deletePageRange(from_page=currentTEAMpage, to_page=currentTEAMpage) # delete the current page from destination TEAM Manual PDF
        pdfToInsert = fitz.open(insertFile) # must be a PDF
        destinationPDF.insertPDF(pdfToInsert, from_page=0, start_at=currentTEAMpage, rotate=90, links=True) # inserts pdf file at current page #

# Save the files
destinationPDF.save(destinationFile, incremental=True)
archiveCopy = destinationFile[:-4] + ' ' + dt.today().strftime('%Y-%m-%d') + '.pdf'
destinationPDF.save(archiveCopy)

print("Complete!\nFile saved.\nAdditional file saved as " + archiveCopy)
