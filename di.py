import os
import difflib
first_file=input("File1:")
second_file=input("File2:")
g=open(first_file).readlines()
h=open(second_file).readlines()
difference=difflib.HtmlDiff().make_file(g,h,first_file,second_file)
difference_report=open('difference_report.html','w')
difference_report.write(difference)
difference_report.close()

