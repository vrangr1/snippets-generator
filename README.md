# VS Code Snippet Generator

Usage:  
```python snippet_generator.py [input_dir] [output_dir]```
  
input_dir: path to the directory where the cpp snippets are stored  
output_dir: path to the directory where the VS Code snippets based on the cpp files in input_dir are supposed to be created  
  
Description:  
VS Code Snippet Generator reads every cpp file in the input_dir and creates a VS Code Snippet based on the same  

CPP File Structure Expected:  
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

For reference ```sample_snippet.cpp``` and ```sample_snippet.code-snippets``` are present in the repository.  