#coding=utf-8

from string import Template

class BuildTask:

    def Init(self):
        filePath = './new_task.js'
        class_file = open(filePath, 'w')

        task_code = []

        template_file = open('./templates/gloria_task.tmpl', 'r')
        tmpl = Template(template_file.read())

        task_code.append(tmpl.substitute(
            DOLLAR_CHAR = '$',
            WEB_PAGE    = 'https://www.cea.gov.cn/cea/xwzx/369242/index.html',
            TARGET_DIR  = '.listNews.pagelib ul li',
            URL_ROOT    = 'https://www.cea.gov.cn',
            ICON_URL    = 'https://pic1.zhimg.com/50/v2-c66d7a89ec2cae81fd27e021111129f7_qhd.jpg'
        ))

        class_file.writelines(task_code)
        class_file.close()

        print('done')

if __name__ == '__main__':
    build = BuildTask()
    build.Init()