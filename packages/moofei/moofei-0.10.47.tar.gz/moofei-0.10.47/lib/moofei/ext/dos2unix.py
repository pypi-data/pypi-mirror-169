#! /usr/bin/env python
# coding=utf-8
 
import os
import sys
import time
_py = list(sys.version_info)
from moofei._find import _get_chardet_detect as detect
 
try:
    input = raw_input
except:
    pass
 
def usage():
    print('Usage:')
    print('\t  %s' % ('unix2dos.py {unix2dos|dos2unix} {dirname|filename}'))
 
def format_file(file, toformat='dos2unix'):
    print('Formatting %s:\t%s' % (toformat, file))
    if not os.path.isfile(file):
        print('ERROR: %s invalid normal file' % file)
        return
    if toformat == 'unix2dos':
        line_sep = '\r\n'
    else:
        line_sep = '\n'
        
    content=open(file,'rb').read()
    encoding = detect(content)[0]
    try:    
        content = content.decode(encoding)
    except:
        if encoding=='gb18030':
            encoding = "utf-8"
            content = content.decode(encoding)
        else:
            raise
    if _py[0]==2:
        import io
        fd = io.open(file, mode='r',encoding=encoding)
        tmpfile = io.open(file+toformat, mode='w',encoding=encoding)
    else:
        fd = open(file, 'r', encoding=encoding)
        tmpfile = open(file+toformat, mode='w',encoding=encoding)
        
    with fd:
        for line in fd:
            line = line.replace('\r', '')
            line = line.replace('\n', '')
            tmpfile.write(line+line_sep)
        tmpfile.close()
    os.remove(file)    
    os.rename(file+toformat, file)
 

 
if __name__ == '__main__':
    if len(sys.argv) == 3:
        toformat=sys.argv[1]
        filename=sys.argv[2]
    elif len(sys.argv) == 2:
        toformat='dos2unix'
        filename=sys.argv[1]
    else:
        usage()
        filename = input('Please write filePath: ')
        toformat='dos2unix'
    format_file(filename, toformat)
