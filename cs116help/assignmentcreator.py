#!/usr/bin/env python3

import os
import re
import sys
from string import Template

regex_a_no = re.compile('(?<=[aA])[0-9]{2}')
header_file_name = "headingcs116.txt"

# It is making sure that the user is inputing the right file
def create(interface_name):
	if regex_a_no.search(interface_name) == None:
		print("Invalid File input - Make sure it is the Interface file")
	else:
		a_no = regex_a_no.search(interface_name).group(0)
		contents = extract_fileinfo(interface_name)
		create_files(contents,a_no)

# cont_list[0] has all the global variables and import files.
# cont_list contains the contents of each questions
def extract_fileinfo(interface_name):
	with open(interface_name,'r') as temp_file:
		cont_list = re.split('#+ Question [0-9]',temp_file.read(),
				flags=re.IGNORECASE)
	return cont_list

def create_files(cont_list, a_no):
	for q_no, q_cont in enumerate(cont_list[1:],1):
		filename = "a{0}q{1}.py".format(a_no,q_no)
		create_afile(filename,a_no,q_no,q_cont,cont_list[0])

def create_afile(filename,a_no,q_no,q_cont,importation):
	if os.path.isfile(filename):
		print("{} - File Exists".format(filename))
	else:
		with open(header_file_name,'r') as headerfile:
			headerobj = Template(headerfile.read())	
			header = headerobj.substitute(a_no=a_no,q_no=q_no)
		with open(filename,'a') as newfile:
			newfile_content = header + importation + q_cont	
			newfile.write(newfile_content)
			print("{} has been successfully created".format(filename))


