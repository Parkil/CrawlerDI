
from dependency_interface import SaveData


class SaveDataImpl(SaveData):

    def __init__(self):
        print('SaveDataImpl init')

    def save(self, parse_html_result: dict):
        print('save called : ', parse_html_result)





