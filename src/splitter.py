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
        print(line)
