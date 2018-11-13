#message
print("This will extract AFE #'s from pdf file: \n")

#get filename
fn = input('What is the filename to extract from? (with .pdf extension\n\
and escaped \\\ or / filepath if not in the same folder as this script):')

#import PyPDF2 and set extracted text as the page_content variable
import PyPDF2
pdf_file = open(fn,'rb')#Change this to ask for filepath & filename before making executable with pyinstaller
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

#Define variable for using in loop
page_content = ""

#for loop to get number of pages and extract text from each page
for page_number in range(number_of_pages):
    page = read_pdf.getPage(page_number)
    page_content += page.extractText()

#initialize the user_input variable
user_input = ""

#function to get the AFE numbers from the pdf document
def get_afenumbers(Y):

    #initialize the afe and afelist variables
    afe = "A"
    afelist = ""
    x = ""

    #while loop to get only 6 digits after the "A"
    while True:

        if user_input.upper().startswith("Y") == True:


                #Return a list of AFE's
                import re
                afe = re.findall('[A][0-9]{6}', page_content)
                set(afe)
                print(set(afe))
                afe_csv = str(set(afe))
                afe_final = afe_csv[1:-1]
                original = afe_final
                removed = original.replace("'", "")
                removed2 = removed.replace(" ", "")
                
                #Convert set to string and write .csv file
                with open("afelist.csv", "w") as fp:
                    fp.write(removed2)
                    break

        elif user_input.upper().startswith("N") == True:
            print("HAVE A GREAT DAY - GOODBYE!!!")
            break
            
        else:
            afe = "No AFE numbers found..."

#while loop for initial question prompt (when Y or N is not True):
while user_input != "Y" and user_input != "N":
    user_input = input('List AFE numbers? Y or N: ').upper()

    if user_input not in ["Y","N"]:
        print('"',user_input,'"','is an invalid input')
        
#run function
get_afenumbers(user_input)
