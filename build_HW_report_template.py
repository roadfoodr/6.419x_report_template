# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:33:47 2021
@author: M Powers
"""
import os, re
import nbformat as nbf


#%% Initialize variables
TEMPLATE_STYLE = 'jbook'  # options: 'jbook' or 'classic'
DATA_DIR = 'questions'
WEEK = 4
CLASS_NAME = 'MITx 6.419x  Data Analysis: Statistical Modeling and Computation in Applications'
STUDENT_NAME = 'Student Name'
STUDENT_USERNAME = 's_name'
COLLABORATORS = 'none'
REPORT_DATE = '5/14/21'

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
if TEMPLATE_STYLE == 'jbook':
    header_lines.append('````{panels}')
    header_lines.append(':column: col-10')
    header_lines.append(f'***{CLASS_NAME.replace("MITx ", "")}***  ')
    header_lines.append('^^^')
    header_lines.append('```{image} mitx_zoom_background.jpg')
    header_lines.append(':alt: MITx\n:width: 300px\n:align: left\n```\n')

    header_lines.append('**Written report -- Homework {{week}}**  ')
    header_lines.append('{{author}} ({{author_sname}})  ')
    if COLLABORATORS != 'none':
        header_lines.append(f'Collaborators: {COLLABORATORS}  ')
    header_lines.append('{{report_date}}  ')
    header_lines.append('+++\n````')
else:
    header_lines.append(f'**{CLASS_NAME}**  ')
    header_lines.append(f'Written report -- Homework {WEEK}  ')
    header_lines.append(f'{STUDENT_NAME} ({STUDENT_USERNAME})  ')
    if COLLABORATORS != 'none':
        header_lines.append(f'Collaborators: {COLLABORATORS}  ')
    header_lines.append(f'{REPORT_DATE}  ')
    header_lines.append('---')

header_text = '\n'.join(header_lines)
nb['cells'].append(nbf.v4.new_markdown_cell(header_text))

#%% add the homework questions, interleaved with blank markdown cells
current_problem = 0
for q in questions:
    pointsum, words, subproblem, question_name = 0, 0, '', ''
    q = q.lstrip()

    # https://stackoverflow.com/questions/17779744/regular-expression-to-get-a-string-between-parentheses-in-javascript
    points = re.findall(r'\((\d+) point[s]*[\.]*\)', q)
    pointsum = sum([int(i) for i in points if type(i)==int or i.isdigit()])

    words = re.search(r'\([Mm]aximum (\d+) words[\.]*\)', q)
    words = words if words else (
        re.search(r'\((\d+) word limit[\.]*\)', q))
    words = words.group(1) if words else 0

    problem = re.search(r'Problem (\d+):', q)
    problem = problem.group(1) if problem else ''
    current_problem = problem if problem else current_problem
    
    subproblem = re.match(r'^\>? ?\*\*([a-zA-Z0-9]\.?[a-zA-Z0-9]?)\.?\*\*', q)
    subproblem = subproblem.group(1).rstrip('.') if subproblem else ''
    if current_problem and subproblem:
        question_name = f'{current_problem}.{subproblem}'

    if TEMPLATE_STYLE == 'jbook':
        q = re.sub('^##', '#', q, count=1)  #move all headers up one level
        q = re.sub(r'\(\d+ point[s]*[\.]*\)\s?', '', q) #remove points from q body
        
        q = re.sub(r'\([Mm]aximum (\d+) words[\.]*\)', '', q) #remove words from q body
        q = re.sub(r'\((\d+) word limit[\.]*\)', '', q)

        q = re.sub(r'^\>? ?\*\*[a-zA-Z0-9]\.?[a-zA-Z0-9]?\.?\*\*',
                   '', q) #remove problem names from q body

    else:
        pass
    
    new_cell = nbf.v4.new_markdown_cell(q)
    new_cell['metadata']['tags'] = []
    if question_name:
        new_cell['metadata']['tags'].append(f'question:{question_name}')
    if pointsum:
        new_cell['metadata']['tags'].append(f'points:{pointsum}')
    if words:
        new_cell['metadata']['tags'].append(f'words:{words}')
    nb['cells'].append(new_cell)
    nb['cells'].append(nbf.v4.new_markdown_cell(' '))

#%% write out the notebook
jbook_suffix = '_jbook' if TEMPLATE_STYLE == 'jbook' else ''
fn = f'HW{WEEK}_report_template{jbook_suffix}.ipynb'
print (f'Writing {fn}')
nbf.write(nb, fn)
if TEMPLATE_STYLE == 'jbook':
    print(f'To build: jupyter-book build ./{fn}')