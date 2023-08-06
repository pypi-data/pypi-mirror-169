import os.path

import yaml
import pytest
# from get_path import GetPath


def run():
    project_name = input("请输入项目名称：")
    username = input("请输入撰写人：")
    origin_di = input("请输入预估di值，若无预估di值，请输入数字0：")
    path = input("请指定报告生成的路径，若不指定，请按回车键（注意：在输入路径时，请不要使用反斜杠）：")
    if path in ('None', 'none', 'NONE', 'null', 'Null', 'NULL') or path == '':
        report_path = 'D:'  # 生成的测试报告默认存放在D盘中
    elif path.find(r'\\') or path.find('//'):
        step_one = path.replace(r'\\', '/')
        report_path = step_one.replace('//', '/')
    else:
        report_path = path.replace(r'//', '/')
    data = {"info":
            {
                    'project_name': f'{project_name}',
                    'writer': f'{username}',
                    'di': f'{origin_di}',
                    'path': f'{report_path}'
            }}
    file_path = os.path.dirname(os.path.abspath(__file__))
    project_data = f'{file_path}/project_data.yml'
    # 清除文件
    with open(project_data, mode='w', encoding='utf-8') as f:
        f.truncate()
    # 写入文件
    with open(project_data, mode='w', encoding='utf-8') as f:
        f.write(yaml.dump(data, allow_unicode=True))
    pytest.main(['-vs', f'{file_path}/test_report.py'])

