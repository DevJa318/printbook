#!/bin/env python

"""
Print books from pdf file on home printer.
It creates new pdf file with changed order of pages.
For example: if you have pdf with eight pages, 
the new pdf pages order will be 8,1,6,3,4,5,2,7
So when you print two pages on one site of A4,
first 1-4 from new pdf, then turn around the paper and print 5-8,
and you bind it in the middle, you can read it as a book.
It works even when pages are not divided by 4.


Input:

pdf_to_print variable - path to pdf you want to make book of

Output:
pdf file
	final_pdf variable - path to pdf file to print
It print in console which pages print first and after rotating paper.



"""

from pypdf import PdfWriter, PdfReader

pdf_to_print = "/home/devja318/Dokumenty/AWKSED.pdf"
final_pdf = "./do_druku.pdf"

reader = PdfReader(pdftoprint)
number_of_pages  = len(reader.pages)

if number_of_pages%4 == 0:
	pod4 = number_of_pages
else:
	mod4 = 4-number_of_pages%4
	pod4 = number_of_pages+mod4

x = [i+1 for i in range(pod4)]

do_until = int(len(x)/4)
book_pages = []

pages_back = len(x)-1
pages_front = 0
for i in range(do_until):
	book_pages.append(x[pages_back])
	book_pages.append(x[pages_front])
	pages_back = pages_back - 2
	pages_front = pages_front + 2

pages_front = int(len(x)/2-1)
pages_back = int(len(x)/2)
for i in range(do_until):
	book_pages.append(x[pages_front])
	book_pages.append(x[pages_back])
	pages_front = pages_front - 2
	pages_back = pages_back + 2 

merger = PdfWriter()
input = open(pdf_to_print, "rb")

for i in book_pages:
	try:
		merger.append(input, [i-1])
	except:
		merger.append(input, [0])

output = open(final_pdf, "wb")
merger.write(output)

merger.close()
output.close()

print("First print: 1-", str(int(len(x)/2))), "pages"
print("Then turn around the paper and print: ", str(int((len(x)/2+1)), "-", str(len(x)))