# VS Code Snippet Generator
## Description:
VS Code Snippet Generator reads every cpp file in the ```input_dir``` and creates a VS Code Snippet based on the same and writes it to ```output_dir```.

## Usage:
```
usage: snippet_generator.py [-h] [input_dir] [output_dir]

VS Code Snippet Generator

positional arguments:
  input_dir   path to the directory where all the cpp snippets are stored
  output_dir  path to the directory where the VS Code Snippets are supposed to be written

optional arguments:
  -h, --help  show this help message and exit
```
  

## CPP File Structure Expected:
```
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
```

## Sample
For reference, ```sample/sample_snippet.cpp``` and ```sample/sample_snippet.code-snippets``` are present in the repository.  