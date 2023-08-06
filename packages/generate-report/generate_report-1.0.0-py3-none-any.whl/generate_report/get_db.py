import logging
import os
import yaml
from generate_report.db_connect import DBConnect


file_path = os.path.dirname(os.path.abspath(__file__))


def get_db(project_name):
    path = f'{file_path}/config.yml'
    with open(path, encoding="utf-8") as f:
        config = yaml.full_load(f)['db']
    logging.info(config)
    return DBConnect(config.get(project_name).get("dbinfo"))

