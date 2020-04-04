#coding=utf-8

from string import Template

class BuildTask:

    def Init(self, wp, td, ur, iu = '', filePath = './new_task.js'):
        
        class_file = open(filePath, 'w')

        task_code = []

        template_file = open('./templates/gloria_task.tmpl', 'r')
        tmpl = Template(template_file.read())

        task_code.append(tmpl.substitute(
            DOLLAR_CHAR = '$',
            WEB_PAGE    = wp,
            TARGET_DIR  = td,
            URL_ROOT    = ur,
            ICON_URL    = iu
        ))

        class_file.writelines(task_code)
        class_file.close()

        print('done')

class BuildReducer:

    def Init(self, fetch_urls, filePath = './new_reducer.js'):

        class_file = open(filePath, 'w')
        reducer_code = []
        fetch_code   = []

        reducer_template_file = open('./templates/gloria_reducer.tmpl', 'r')
        fetch_template_file = open('./templates/fetch_url.tmpl', 'r')
        reducer_template = Template(reducer_template_file.read())
        fetch_template = Template(fetch_template_file.read())

        for url in fetch_urls:
            fetch_code.append(fetch_template.substitute(
                URL = url
            ))

        reducer_code.append(reducer_template.substitute(
            CODE = ''.join(fetch_code)
        ))

        class_file.writelines(reducer_code)
        class_file.close()

        print('done')

if __name__ == '__main__':
    code_type = input('请选择生成代码的类别(1.task / 2.reducer): ')
    if code_type == '1': 
        build = BuildTask()
        wp = input('请输入目标页面地址: ')
        td = input('请输入目标通知栏盒子模型的位置: ')
        ur = input('请输入目标通知链接的前缀(默认为空): ')
        iu = input('请输入Gloria推送通知的图标地址(默认为空): ')
        file_path = input('请输入生成代码的存放位置及文件名(默认为./new_task.js):')
        if file_path == '': file_path = './new_task.js'
        build.Init(wp, td, ur, iu, file_path)
    else: 
        build = BuildReducer()
        fu = input('请输入用于提交请求的链接，多个链接用空格分开: ')
        urls = fu.split(' ')
        file_path = input('请输入生成代码的存放位置及文件名(默认为./new_task.js):')
        if file_path == '': file_path = './new_reducer.js'
        build.Init(urls, file_path)
