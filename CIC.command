#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
# Prevent path error.By ZYunH.
CIC_path = os.path.dirname(sys.argv[0])
os.chdir(CIC_path)

def text_read(filename):
    try:
        file = open(filename, 'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        if content[i][len(content[i]) - 1] == '\n':
            content[i] = content[i][:len(content[i]) - 1]

    file.close()
    return content


def text_save(content, filename, mode='a'):
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]) + '\n')
    file.close()


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
        if i.find('import') == 0 or i.find('#') == 0:
            pass
        elif import_os_key:
            content.insert(content.index(i), 'import os')
            import_os_key = 0
        elif import_sys_key:
            content.insert(content.index(i), 'import sys')
            import_sys_key = 0

    # Add header
    if content[0] != '#!/usr/bin/env python':
        content.insert(0, '#!/usr/bin/env python')

    # Add path
    for i in content:
        if i.find('import') == 0 or i.find('#') == 0:
            pass
        else:
            list_path = ['# Prevent path error.By ZYunH.', 'CIC_path = os.path.dirname(sys.argv[0])', 'os.chdir(CIC_path)']

            for j in range(len(list_path)):
                content.insert(content.index(i), list_path[j])
            break

    text_save(content, file_name[:-3] + '_temp' + '.py', mode='w')


def change(name):
    name_change = name[:-8] + '.command'

    os.rename(name, name_change)

    os.system('chmod +x %s' % name_change)


file_name = raw_input('Filename :')

content = text_read(file_name)

add(content=content, file_name=file_name)

change(file_name[:-3] + '_temp' + '.py')
