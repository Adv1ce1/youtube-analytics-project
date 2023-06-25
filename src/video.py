from src.channel import Channel


class Video:
    """
    Класс для представления видео.
    """

    def __init__(self, video_id: str) -> None:
        """
        Инициализирует экземпляр класса Video.
        """
        self.__video_id = video_id
        self.__title = None
        self.__url = None
        self.__view_count = None
        self.__like_count = None
        self.fetch_video_data()

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Video.
        """
        return self.__title

    def fetch_video_data(self) -> None:
        """
        Получает данные о видео с помощью YouTube API и обновляет соответствующие атрибуты объекта.
        """
        try:
            youtube = Channel.get_service().videos().list(
                part='snippet,statistics', id=self.video_id
            ).execute()
            video_data = youtube.get('items')[0]
            self.__title = video_data.get('snippet').get('title')
            self.__url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.__view_count = int(video_data.get('statistics').get('viewCount'))
            self.__like_count = int(video_data.get('statistics').get('likeCount'))
        except IndexError:
            print('Неверная ссылка!')

    @property
    def video_id(self) -> str:
        return self.__video_id

    @video_id.setter
    def video_id(self, value) -> None:
        self.__video_id = value


class PLVideo(Video):
    """
    Класс для представления видео в плейлисте.
    """

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """
        Инициализирует экземпляр класса PLVideo.
        """
        self.__playlist_id = playlist_id
        super().__init__(video_id)