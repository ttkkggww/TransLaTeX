import re

def remove_comment(lines:list):
    res = []
    comments = []
    for line in lines:
        for i in range(len(line)+1):
            if(len(line)==i):
                res.append(line)
                comments.append('')
                break
            if(line[i]=='%'):
                if i==0:
                    res.append('')
                    comments.append(line[i:])
                    break
                elif(line[i-1]!='\\'):
                    res.append(line[:i])
                    comments.append(line[i:])
                    break
    return (res,comments)

def split_begin_end(lines:list,stack:list):
    res = []
    for line in lines:
        while(True):
            result = re.search(r"\\begin *?{ *?(.*?) *?}",line,re.S)
            if result:
                tag = result.group(1)
                result = re.search(r"\\begin *?{ *?"+tag+" *?}.*?"+r"\\end *?{ *?"+tag+" *?}",line,re.S)
                num_str = str(len(stack)).zfill(5)
                stack.append([result.group(),num_str])
                line = line.replace(result.group(),num_str)
            else:
                break
        res.append(line)
    return (res,stack)

def split_re(lines:list,stack:list):
    with open("./escape_regular_expression.txt",'r') as esc_res:
        esc_re_lines = esc_res.read().splitlines()
        for esc_re in esc_re_lines:
            res = []
            for line in lines:
                while(True):
                    result = re.search(esc_re,line,re.S)
                    if result:
                        num_str = str(len(stack)).zfill(5)
                        stack.append([result.group(),num_str])
                        line = line.replace(result.group(),num_str)
                    else:
                        break
                res.append(line)
            lines = res
    return (res,stack)

def warning_backslash(lines:list,filename:str):
    for line in lines:
        for l in line.splitlines():
            if(l.find('\\')!=-1):
                print("Warning! A special command are not escaped!",filename,l)

def restore_escape(lines:list,stack:list,filename:str):
    while(len(stack)!=0):
        top = stack.pop()
        exist = False
        res = []
        for line in lines:
            if(line.find(top[1])!=-1):
                line = line.replace(top[1],top[0])
                exist = True
            res.append(line)
        lines = res;
        if(exist==False):
            print("Faild to restore:",filename,top)
    return lines
