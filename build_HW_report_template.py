# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:33:47 2021
@author: M Powers
"""
import os, re
import nbformat as nbf


#%% Initialize variables
DATA_DIR = 'questions'
WEEK = 4
CLASS_NAME = '**MITx 6.419x  Data Analysis: Statistical Modeling and Computation in Applications**  '
STUDENT_NAME = 'Student Name'
STUDENT_USERNAME = 's_name'
COLLABORATORS = 'none'
REPORT_DATE = '4/10/21'

#%% Read questions
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open(f'{DATA_DIR}/HW_{WEEK}.md', 'r') as question_file:
	question_blocks = question_file.read()

question_blocks.replace('||| ', '|||')
questions = re.split(r'\|\|\|', question_blocks)

#%% create the notebook
nb = nbf.v4.new_notebook()
nb['cells'] = []

#%% Format the header cell
header_lines = []
header_lines.append(CLASS_NAME)
header_lines.append(f'Written report -- Homework {WEEK}  ')
header_lines.append(f'{STUDENT_NAME} ({STUDENT_USERNAME})  ')
if COLLABORATORS != 'none':
    header_lines.append(f'Collaborators: {COLLABORATORS}  ')
header_lines.append(f'{REPORT_DATE}  ')
header_lines.append('---')

header_text = '\n'.join(header_lines)
nb['cells'].append(nbf.v4.new_markdown_cell(header_text))

#%% add the homework questions, interleaved with blank markdown cells
for q in questions:
    nb['cells'].append(nbf.v4.new_markdown_cell(q))
    nb['cells'].append(nbf.v4.new_markdown_cell(' '))

#%% write out the notebook
fn = f'HW{WEEK}_report_template.ipynb'
print (f'Writing {fn}')
nbf.write(nb, fn)