import logging

from dependency_interface import SaveData


class SaveDataImpl(SaveData):

    logger = logging.getLogger('detail')

    def __init__(self):
        self.logger.info('SaveDataImpl init')

    def save(self, parse_html_result: dict):
        self.logger.info('save called : %s', parse_html_result)





