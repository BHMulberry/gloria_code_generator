#coding=utf-8

from string import Template

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
    build = BuildReducer()
    build.Init(['https://pushbear.ftqq.com/sub']) # your urls here