import json
import os
from googleapiclient.discovery import build


class Channel:
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    @staticmethod
    def __printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.__printj(self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute())

    @staticmethod
    def to_json(name):
        with open(name, 'w') as outfile:
            json.dump(name, outfile)

