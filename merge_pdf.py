#!/bin/env python
import os
from pypdf import PdfWriter

path='/home/devja318/Dokumenty/PROG2023/EPAM/DevOps - Fundamentals/awk&sed/'

files = os.listdir(path)
files.sort()
os.chdir(path)
merger=PdfWriter()

for file in files:
  merger.append(file)

merger.write('merged.pdf')
merger.close() 