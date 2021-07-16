import PyPDF2  as p

document = open("PDF_Extraction doc.pdf", "rb")              #rb-reading in bytes mode opens the file in binary format for reading
pd = p.PdfFileReader(document)
pages = pd.getNumPages()                                                                           #getNumPages will return an integer value
wish1 = input("Do you wish to know how many pages are there in this document? ")
if wish1 == "yes":
    print("This document has " + str(pages) + " pages")                                            #variable pages has to be converted to string datatype for concatenation
else:
    print()
wish2 = input("Do you wish to print the document? ")
if wish2 == "yes":
    page_number = 1
    page_index = 0
    desired_pages = int(input("Enter the number of pages you want to print: "))
    while page_number <= desired_pages:
        page = pd.getPage(page_index)
        print(page.extractText())
        page_number += 1
        page_index += 1
else:
    print()
document.close()