# -*- coding:utf-8 -*-
import os
import sys

def text_read(filename):
    result = []

    with open(filename, 'r') as content:
        for line in content:
            if line[-1] == '\n':
                line = line[0:-1]
            result.append(line)

    return result


def text_save(content, filename, mode='a'):
    file = open(filename, mode)

    for index, item in enumerate(content):
        file.write(str(content[index]) + '\n')

    file.close()


def add(content, file_name):
    # Check os and sys respectly.

    import_os_key = 1
    import_sys_key = 1

    for i in content:
        if i.replace(' ','') == 'importos':
            import_os_key = 0
        if i.replace(' ','') == 'importsys':
            import_sys_key = 0

    if import_os_key or import_sys_key:
        for index, item in enumerate(content):
            # Ignore comments and import modules.
            if item.find('import') == 0 or item.find('#') == 0:
                pass
            elif import_os_key:
                content.insert(index, 'import os')
                import_os_key = 0
            elif import_sys_key:
                content.insert(index, 'import sys')
                import_sys_key = 0
            else:
                break

    # Add header.
    if content[0] != '#!/usr/bin/env python':
        content.insert(0, '#!/usr/bin/env python')

    # Add path.
    for i in content:
        if i.find('import') == 0 or i.find('#') == 0:
            pass
        else:
            list_path = [
                '# Prevent path error.By ZYunH.',
                'CIC_path = os.path.dirname(sys.argv[0])',
                'os.chdir(CIC_path)'
            ]

            for j in list_path:
                content.insert(content.index(i), j)
            break

    # Save a temp file.
    text_save(content, file_name.replace('.py', '') + '_temp' + '.py', mode='w')

    return file_name.replace('.py', '') + '_temp' + '.py'


def modify_permissions(name):
    # Modify primissions and rename temp filename to orginal name.
    name_change = name.replace('_temp.py', '') + '.command'

    os.rename(name, name_change)

    os.system('chmod +x %s' % name_change)

def introduction():
    print 'Introduction:'
    print 'CIC is a tiny tool used to convert a python script into a executable file.'
    print '1.It will not change your original  script at the same time(only for mac)'
    print '2.Before use it, please make sure the python on your system is same version as on your scripts!'

try:
    file_name = sys.argv[1]
except IndexError:
    introduction()
    file_name = raw_input('Please input filename :').replace(' ','')

content = text_read(file_name)

temp_name = add(content=content, file_name=file_name)

modify_permissions(temp_name)
