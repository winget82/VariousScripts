"""Copy file path from address bar then run script to move
every file from the Downloads folder to that filepath.
Remove file from downloads if already exists in destination."""

import shutil as s
import os
import pyperclip as p
import fitz #PyMuPDF for highlighting "maint" in pdf files that are moved

source = 'C:\\Users\\username\\Downloads\\'
destination = p.paste()

sourceFiles = os.listdir(source) # get list of all files in downloads folder
destFiles = os.listdir(destination) # get list of any files in destination folder

text = "maint"

def mark_word(page, text):
    """Highlight each word that contains 'maint'."""
    found = 0
    wlist = page.getTextWords()        # make the word list
    for w in wlist:                    # scan through all words on page
        if text in w[4]:               # w[4] is the word's string
            found += 1                 # count
            r = fitz.Rect(w[:4])       # make rect from word bbox
            page.addHighlightAnnot(r)  # highlight
    return found

for fname in sourceFiles:
    if '.pdf' in fname:
        doc = fitz.open(source + fname)

        new_doc = False                        # indicator if anything found at all

        for page in doc:                       # scan through the pages
            found = mark_word(page, text)      # mark the page's words
            if found:                          # if anything found ...
               new_doc = True

        doc.save(destination + '\\' + fname, garbage=4, clean=1, deflate=1)
        doc.close()
        os.remove(source + fname)

sourceFiles = os.listdir(source) # get updated list of all files in downloads folder
                                 # after pdf files have been saved over and deleted

# Move any remaining files in source to destination
for f in sourceFiles:
    if f not in destFiles:
        s.move(source + f, destination)
    else:
        os.remove(source + f)
