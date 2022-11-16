import re

def splitLaTeX(s:str):
    return s

def split_comment(lines:list):
    lines = [line.split('%') for line in lines]
    res = [line[0] for line in lines]
    comments = [None if len(line)==1 else '%'.join(line[1:]) for line in lines]
    return (res,comments)


