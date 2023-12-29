#!/bin/env python

# import sys
from pypdf import PdfWriter, PdfReader

dokument = "/home/devja318/Pulpit/styleguidebash.pdf"
reader = PdfReader(dokument)

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
input = open(dokument, "rb")

print(book_pages)
for i in book_pages:
	try:
		merger.append(input, [i-1])
	except:
		merger.append(input, [0])

output = open("document-output.pdf", "wb")
merger.write(output)

merger.close()
output.close()

