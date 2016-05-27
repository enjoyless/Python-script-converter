# -*- coding:utf-8 -*-
from tools import *
import os
import sys

file_name = sys.argv[0]

content = text_read(file_name)


def add(content, file_name):
    # Import os and sys respectly

    import_os_key = 1
    import_sys_key = 1

    for i in content:
        if i == 'import os':
            import_os_key = 0
        if i == 'import sys':
            import_sys_key = 0

    for i in content:
        if i.find('import')==0 or i.find('#')==0:
            pass
        elif import_os_key:
            content.insert(content.index(i) , 'import os')
            import_os_key = 0
        elif import_sys_key:
            content.insert(content.index(i) , 'import sys')
            import_sys_key = 0

    # Add header
    if content[0] != '#!/usr/bin/env python':
        content.insert(0, '#!/usr/bin/env python')

    # Add path
    if content[len(content)-2] != '# Prevent path error.By ZYunH.':

        list_path = ['# Prevent path error.By ZYunH.', '_path = os.path.dirname(sys.argv[0])', 'os.chdir(_path)']

        content.insert(len(content),'')
        for i in range(len(list_path)):
            content.insert(len(content), list_path[i])

    text_save(content, file_name[:-3] + '_temp' + '.py', mode='w')


def change(name):
    name_change = name[:-8] + '.command'

    os.rename(name, name_change)

    os.system('chmod +x %s' % name_change)


add(content=content, file_name=file_name)

change(file_name[:-3] + '_temp' + '.py')
