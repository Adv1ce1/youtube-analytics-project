import json
import googleapiclient.discovery
from googleapiclient.discovery import build, Resource
from src.config import API_KEY_YOUTUBE
from functools import total_ordering


@total_ordering
class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Инициализирует экземпляр класса Channel с указанным идентификатором канала.
        Данные о канале будут получены с помощью YouTube API.
        """
        self.__channel_id = channel_id
        self.__youtube = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__channel_title = self.__youtube['items'][0]['snippet']['title']
        self.__channel_description = self.__youtube['items'][0]['snippet']['description']
        self.__channel_url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.__subscriber_count = int(self.__youtube['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__youtube['items'][0]['statistics']['videoCount'])
        self.__view_count = int(self.__youtube['items'][0]['statistics']['viewCount'])

    def __str__(self) -> str:
        """
               Возвращает строковое представление объекта Channel.
               Формат: Название канала (URL канала)
        """
        return f"{self.__channel_title} ({self.__channel_url})"

    def __eq__(self, other) -> bool:
        """
              Проверяет, равен ли данный объект Channel другому объекту по количеству подписчиков.
        """
        return self.__subscriber_count == other.__subscriber_count

    def __lt__(self, other) -> bool:
        """
                Проверяет, является ли данный объект Channel "меньшим" по количеству подписчиков, чем другой объект.
        """
        return self.__subscriber_count < other.__subscriber_count

    def __add__(self, other) -> int:
        """
                Складывает количество подписчиков данного объекта Channel с количеством подписчиков другого объекта.
        """
        return self.__subscriber_count + other.__subscriber_count

    def __rsub__(self, other) -> int:
        """
                Вычитает количество подписчиков данного объекта Channel из количества подписчиков другого объекта.
        """
        return other.__subscriber_count - self.__subscriber_count

    def __sub__(self, other) -> int:
        """
                Вычитает количество подписчиков другого объекта Channel из количества подписчиков данного объекта.
        """
        return self.__subscriber_count - other.__subscriber_count

    @property
    def channel_id(self) -> str:
        return self.__channel_id

    def print_info(self) -> None:
        print(json.dumps(self.__youtube, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> googleapiclient.discovery.Resource:
        return build('youtube', 'v3', developerKey=API_KEY_YOUTUBE)

    def to_json(self, file_path: str) -> None:
        """
               Сохраняет информацию о канале в JSON-файл.
        """
        channel_data = {
            'channel_id': self.__channel_id,
            'channel_title': self.__channel_title,
            'channel_description': self.__channel_description,
            'channel_url': self.__channel_url,
            'subscriberCount': self.__subscriber_count,
            'videoCount': self.__video_count,
            'viewCount': self.__view_count
        }
        with open(file_path, 'w') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)