import os
import pathlib
import argparse
from enum import Enum

"""
VS Code Snippet Generator
Usage:
python snippet_generator.py [input_dir] [output_dir]

input_dir: path to the directory where the cpp snippets are stored
output_dir: path to the directory where the VS Code snippets based on the cpp files in input_dir are supposed to be created

Description:
VS Code Snippet Generator reads every cpp file in the input_dir and creates a VS Code Snippet based on the same

CPP File Structure Expected:
/*
Details for snippet generator program:
title       : Snippet Title
prefix      : vs_code_import_prefix
description : Snippet Description
*/
#ifndef SOME_SNIPPET
#define SOME_SNIPPET
// ...
// Snippet Code
// ...
#endif

"""

SOURCE_EXTENSION=".cpp"
TARGET_EXTENSION=".code-snippets"
TAB="    "

class Details(Enum):
    TITLE       = 'title'
    PREFIX      = 'prefix'
    DESCRIPTION = 'description'

def parse_args(args=None):
    parser = argparse.ArgumentParser(description ='VS Code Snippet Generator')
    parser.add_argument('input_dir', metavar ='ID', type=str, nargs='?',\
                        default="/Users/anavp/home/programming/competitive-programming/algo/snippets_code",\
                        help='path to the directory where all the snippets in cpp files are stored')
    parser.add_argument('output_dir', metavar='OD', type=str, nargs='?',\
                        default="/Users/anavp/home/programming/competitive-programming/.vscode",\
                        help='path to the directory where the vs code snippets are supposed to be written')
    args = parser.parse_args()
    return args

def get_files(dir_path : str) -> 'list[str]':
    files = os.listdir(dir_path)
    cpp_files = list()
    for file in files:
        file_path = os.path.join(dir_path,file)
        if not os.path.isfile(file_path) or pathlib.Path(file_path).suffix != SOURCE_EXTENSION:
            continue
        cpp_files.append(file_path)
    return cpp_files

def get_snippet_details(file_path : str) -> 'tuple[dict[Details,str],list[str]]':
    file = open(file_path,'r')
    lines = file.readlines()
    ind = next((ind for ind,line in enumerate(lines) if line.startswith("#ifndef")),None)
    assert ind >= 3, "The details for VS Code snippets (title, prefix, description) seems to be missing in the beginning of the cpp file."
    lines, rest = lines[:ind], lines[ind:]
    details_list = tuple(["title", "prefix", "description"])
    details = dict()
    for line in lines:
        line = line.strip()
        if not line.startswith(details_list): continue
        detail = Details(line.split(' ',1)[0])
        value = line.split(':',1)[1].strip()
        details[detail] = value
    assert len(details) == 3, "All details (title, prefix, description) were not there in the beginning of the cpp file"
    return details, rest

def process_file(file_path : str, write_dir : str) -> None:
    details, lines = get_snippet_details(file_path)
    
    write_path = os.path.join(write_dir, os.path.splitext(os.path.basename(file_path))[0] + TARGET_EXTENSION)
    write_file = open(write_path,'w')
    space = ""
    
    write_file.write(space + "{\n")
    
    space += TAB
    write_file.write(space + f'"{details[Details.TITLE]}": {{\n')
    
    space += TAB
    write_file.write(space + f'"prefix": "{details[Details.PREFIX]}",\n')
    write_file.write(space + '"body": [\n')
    
    space += TAB
    for line in lines[:-1]:
        line = line.strip('\n')
        write_file.write(space + f'"{line}",\n')
    write_file.write(space + f'"{lines[-1].strip()}"\n')
    
    space = space[:-len(TAB)]
    write_file.write(space + '],\n')
    write_file.write(space + f'"description": "{details[Details.DESCRIPTION]}"\n')
    
    space = space[:-len(TAB)]
    write_file.write(space + "}\n")
    
    space = space[:-len(TAB)]
    write_file.write(space + "}")

if __name__ == '__main__':
    args = parse_args()
    assert args.input_dir != "", "path to the source directory of snippets cannot be empty!"
    assert args.output_dir != "", "path to destination directory where the vs code snippets are supposed to be store cannot be empty!"
    
    files = get_files(args.input_dir)
    for file in files:
        process_file(file,args.output_dir)
